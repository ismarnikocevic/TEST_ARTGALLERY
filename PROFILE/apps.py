from django.apps import AppConfig


class PROFILEConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PROFILE'

    def ready(self):
        import PROFILE.signals  
