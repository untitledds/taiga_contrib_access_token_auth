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

# Константы для аутентификации
ACCESS_TOKEN_USER_KEY = os.getenv("ACCESS_TOKEN_USER_KEY", "access_token_auth")

# Проекты
PROJECTS = {}
projects_str = os.getenv("PROJECTS", "")
for project in projects_str.split(","):
    name, id = project.split(":")
    PROJECTS[name] = id

# Поля пользователя
USER_FIELDS = {
    "GUID": os.getenv("USER_FIELD_GUID", "sub"),
    "USERNAME": os.getenv("USER_FIELD_USERNAME", "preferred_username"),
    "EMAIL": os.getenv("USER_FIELD_EMAIL", "email"),
    "FULL_NAME": os.getenv("USER_FIELD_FULL_NAME", "name"),
    "GROUPS": os.getenv("USER_FIELD_GROUPS", "groups"),
}

# Настройка для фильтрации групп
FILTER_GROUPS = os.getenv("FILTER_GROUPS", "False").lower() == "true"

# Настройка для проекта по умолчанию
DEFAULT_PROJECT_ID = os.getenv("DEFAULT_PROJECT_ID", "default_project_id")

# Настройка для роли по умолчанию
DEFAULT_ROLE = os.getenv("DEFAULT_ROLE", "Member")
ADMIN_GROUP = os.getenv("ADMIN_GROUP", "Admin")
