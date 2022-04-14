from django.apps import AppConfig


class {{ app_name }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ app_name }}'
