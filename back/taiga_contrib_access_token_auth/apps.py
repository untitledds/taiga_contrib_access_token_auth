from django.apps import AppConfig

class TaigaContribAccessTokenAuthAppConfig(AppConfig):
    name = "taiga_contrib_access_token_auth"
    verbose_name = "Taiga contrib Access Token auth App Config"

    def ready(self):
        from taiga.auth.services import register_auth_plugin
        from . import services
        register_auth_plugin(
            "access_token_auth",
            services.access_token_login_func,
        )