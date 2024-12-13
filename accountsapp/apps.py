from django.apps import AppConfig


# class AccountsappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'accountsapp'

# from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountsapp'

    def ready(self):
        import accountsapp.signals  # Pastikan sinyal terdaftar

