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
    required_fields = ['sub', 'preferred_username', 'email', 'name']
    for field in required_fields:
        if field not in user_info:
            logger.error(f"Missing required field '{field}' in user info response")
            raise ConnectorBaseException({
                "error_message": f"Missing required field '{field}' in user info response",
                "response_text": user_info
            })

    # Возвращаем информацию о пользователе
    return {
        'guid': user_info['sub'],
        'username': user_info['preferred_username'],
        'email': user_info['email'],
        'full_name': user_info['name'],
        'groups': user_info.get('groups', []),
    }
