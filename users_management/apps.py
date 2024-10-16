from django.apps import AppConfig


class UsersManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_management'

    def ready(self):
        import users_management.signals