import requests
import logging
from django.conf import settings
from taiga.base.connectors.exceptions import ConnectorBaseException

logger = logging.getLogger(__name__)

def get_user_info(access_token):
    """
    Получает информацию о пользователе от OIDC-провайдера.

    :param access_token: Токен доступа от OIDC-провайдера.
    :returns: Информация о пользователе.
    """
    userinfo_url = settings.OIDC_USERINFO_ENDPOINT

    try:
        userinfo_response = requests.get(
            userinfo_url,
            headers={'Authorization': f'Bearer {access_token}'}
        )
        userinfo_response.raise_for_status()  # Выбрасывает исключение, если статус код не 200
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to obtain user info: {e}")
        raise ConnectorBaseException({
            "error_message": "Failed to obtain user info",
            "details": str(e)
        })

    user_info = userinfo_response.json()

    # Проверка обязательных полей
    required_fields = [settings.USER_FIELDS["GUID"], settings.USER_FIELDS["USERNAME"], settings.USER_FIELDS["EMAIL"], settings.USER_FIELDS["FULL_NAME"]]
    for field in required_fields:
        if field not in user_info:
            logger.error(f"Missing required field '{field}' in user info response")
            raise ConnectorBaseException({
                "error_message": f"Missing required field '{field}' in user info response",
                "response_text": user_info
            })

    # Возвращаем информацию о пользователе
    return {
        'guid': user_info[settings.USER_FIELDS["GUID"]],
        'username': user_info[settings.USER_FIELDS["USERNAME"]],
        'email': user_info[settings.USER_FIELDS["EMAIL"]],
        'full_name': user_info[settings.USER_FIELDS["FULL_NAME"]],
        'groups': user_info.get(settings.USER_FIELDS["GROUPS"], []),
    }
