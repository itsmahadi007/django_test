from django.apps import apps
from django.contrib import admin

for model in apps.get_app_config('users_management').models.values():
    admin.site.register(model)