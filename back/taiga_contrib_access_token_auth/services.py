import os
import logging
from django.db import transaction as tx
from django.apps import apps
from django.conf import settings
from taiga.base.utils.slug import slugify
from taiga.auth.services import send_register_email, make_auth_response_data, get_membership_by_token
from taiga.auth.signals import user_registered as user_registered_signal
from taiga.base.connectors.exceptions import ConnectorBaseException
from .connector import get_user_info

logger = logging.getLogger(__name__)

USER_KEY = settings.ACCESS_TOKEN_USER_KEY
FILTER_GROUPS = settings.FILTER_GROUPS
PROJECTS = settings.PROJECTS
DEFAULT_ROLE = settings.DEFAULT_ROLE

def determine_role_and_project(groups):
    for group in groups:
        parts = group.split(':')
        if len(parts) == 2:
            role, project = parts
            if project.upper() in PROJECTS:
                return role.upper(), PROJECTS[project.upper()]
    return None, None

@tx.atomic
def access_token_register(
        username: str,
        email: str,
        full_name: str,
        oidc_guid: str,
        groups: list = None,
):
    logger.info(f"Starting registration process for user: {email}")
    auth_data_model = apps.get_model("users", "AuthData")
    user_model = apps.get_model("users", "User")
    membership_model = apps.get_model("projects", "Membership")
    role_model = apps.get_model("users", "Role")  # Исправлено: указываем правильное приложение
    project_model = apps.get_model("projects", "Project")

    try:
        auth_data = auth_data_model.objects.get(key=USER_KEY, value=oidc_guid)
        user = auth_data.user
        logger.info(f"User already exists: {email}")
    except auth_data_model.DoesNotExist:
        try:
            user = user_model.objects.get(email=email)
            auth_data_model.objects.create(user=user, key=USER_KEY, value=oidc_guid, extra={})
            logger.info(f"User found by email: {email}")
        except user_model.DoesNotExist:
            username_unique = slugify(username)
            user = user_model.objects.create(email=email, username=username_unique, full_name=full_name)
            auth_data_model.objects.create(user=user, key=USER_KEY, value=oidc_guid, extra={})
            send_register_email(user)
            user_registered_signal.send(sender=user.__class__, user=user)
            logger.info(f"New user created: {email}")

    role, project_id = determine_role_and_project(groups) if groups else (None, None)

    if FILTER_GROUPS and not role:
        raise ConnectorBaseException({
            "error_message": "Access denied",
            "details": "Required groups not found"
        })

    if not role:
        role = DEFAULT_ROLE
        project_id = settings.DEFAULT_PROJECT_ID

    project = project_model.objects.get(id=project_id)

    role, _ = role_model.objects.get_or_create(
        project=project,
        name=role
    )

    membership_model.objects.get_or_create(
        user=user,
        project=project,
        role=role
    )
    logger.info(f"Role assigned to user: {email}, role: {role}, project_id: {project.id}")

    return user

def access_token_login_func(request):
    try:
        access_token = request.POST['access_token']
        user_info = get_user_info(access_token)
        groups = user_info.get('groups', [])

        user = access_token_register(
            username=user_info['username'],
            email=user_info['email'],
            full_name=user_info['full_name'],
            oidc_guid=user_info['guid'],
            groups=groups,
        )
        data = make_auth_response_data(user)
        return data
    except KeyError as e:
        logger.error(f"Missing required parameter: {e}")
        raise ConnectorBaseException({
            "error_message": "Missing required parameter",
            "details": str(e)
        })
    except ConnectorBaseException as e:
        logger.error(f"Access Token authentication failed: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise ConnectorBaseException({
            "error_message": "Unexpected error",
            "details": str(e)
        })
