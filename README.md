# Taiga Access Token Authentication Plugin

Этот плагин позволяет аутентифицировать пользователей в Taiga с использованием токенов доступа от OIDC-провайдера.

## Настройка

### Переменные окружения

Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные окружения:

```env
# Константы для аутентификации
ACCESS_TOKEN_USER_KEY=access_token_auth

# Проекты
PROJECTS=SECURITY:1,CVE:2,VENDOR:3,PRON:7

# Поля пользователя
USER_FIELD_GUID=sub
USER_FIELD_USERNAME=preferred_username
USER_FIELD_EMAIL=email
USER_FIELD_FULL_NAME=name
USER_FIELD_GROUPS=groups

# Роль по умолчанию
DEFAULT_ROLE=Member

# Настройка для фильтрации групп
FILTER_GROUPS=False

# Настройка для проекта по умолчанию
DEFAULT_PROJECT_ID=default_project_id

# OIDC Settings
OIDC_USERINFO_ENDPOINT=https://your-oidc-provider.com/protocol/openid-connect/userinfo

# Включение плагина для аутентификации по токену доступа
ENABLE_ACCESS_TOKEN_AUTH=True

# Использование прокси
USE_X_FORWARDED_HOST=False
