import os

# Включение плагина для аутентификации по токену доступа
ENABLE_ACCESS_TOKEN_AUTH = os.getenv('ENABLE_ACCESS_TOKEN_AUTH', 'False') == 'True'
if ENABLE_ACCESS_TOKEN_AUTH:
    INSTALLED_APPS += [
        "taiga_contrib_access_token_auth",
    ]

    AUTHENTICATION_BACKENDS = list(AUTHENTICATION_BACKENDS) + [
        "taiga_contrib_access_token_auth.services.AccessTokenAuthenticationBackend",
    ]

    # OIDC Settings
    OIDC_OP_USER_ENDPOINT = os.getenv("OIDC_USERINFO_ENDPOINT", "https://your-oidc-provider.com/protocol/openid-connect/userinfo")
    ACCESS_TOKEN_USER_KEY = os.getenv("ACCESS_TOKEN_USER_KEY", "access_token_auth")

# Использование прокси
USE_FORWARDED_HOST = os.getenv('USE_X_FORWARDED_HOST', 'False') == 'True'
if USE_FORWARDED_HOST:
    USE_X_FORWARDED_HOST = USE_FORWARDED_HOST
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')