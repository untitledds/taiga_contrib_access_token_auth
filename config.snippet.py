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

# Константы для ролей
ROLES = {
    "OWNER": os.getenv("ROLE_OWNER", "Owner"),
    "ADMIN": os.getenv("ROLE_ADMIN", "Admin"),
    "MEMBER": os.getenv("ROLE_MEMBER", "Member"),
    "WATCHER": os.getenv("ROLE_WATCHER", "Watcher"),
}

# Константы для групп
GROUPS = {
    "SECURITY_ADMINS": os.getenv("GROUP_SECURITY_ADMINS", "Security Admins"),
    "SECURITY_ANALYSTS": os.getenv("GROUP_SECURITY_ANALYSTS", "Security Analysts"),
    "WATCHERS": os.getenv("GROUP_WATCHERS", "Watchers"),
    "CVE_ADMINS": os.getenv("GROUP_CVE_ADMINS", "CVE Admins"),
    "CVE_RESEARCHERS": os.getenv("GROUP_CVE_RESEARCHERS", "CVE Researchers"),
    "CVE_WATCHERS": os.getenv("GROUP_CVE_WATCHERS", "CVE Watchers"),
    "PROJECT_ADMINS": os.getenv("GROUP_PROJECT_ADMINS", "Project Admins"),
    "DEVELOPERS": os.getenv("GROUP_DEVELOPERS", "Developers"),
    "VENDOR_SUPPORT": os.getenv("GROUP_VENDOR_SUPPORT", "Vendor Support"),
}

# Константы для проектов
PROJECTS = {
    "SECURITY": os.getenv("PROJECT_ID_SECURITY", "1"),
    "CVE": os.getenv("PROJECT_ID_CVE", "2"),
    "VENDOR": os.getenv("PROJECT_ID_VENDOR", "3"),
}
