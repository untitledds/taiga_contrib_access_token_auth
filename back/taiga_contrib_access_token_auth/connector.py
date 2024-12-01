import requests
import logging
import os
from django.conf import settings
from taiga.base.connectors.exceptions import ConnectorBaseException

logger = logging.getLogger(__name__)

def get_user_info(access_token):
    """
    Получает информацию о пользователе от OIDC-провайдера.

    :param access_token: Токен доступа от OIDC-провайдера.
    :returns: Информация о пользователе.
    """
    userinfo_url = os.get("OIDC_USERINFO_ENDPOINT")

    userinfo_response = requests.get(
        userinfo_url,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    if userinfo_response.status_code != 200:
        logger.error(f"Failed to obtain user info: {userinfo_response.text}")
        raise ConnectorBaseException({
            "error_message": "Failed to obtain user info",
            "status_code": userinfo_response.status_code,
            "response_text": userinfo_response.text
        })

    user_info = userinfo_response.json()

    # Возвращаем информацию о пользователе
    return {
        'guid': user_info.get('sub', None),
        'username': user_info.get('preferred_username', None),
        'email': user_info.get('email', None),
        'full_name': user_info.get('name', None),
        'groups': user_info.get('groups', []),
    }
