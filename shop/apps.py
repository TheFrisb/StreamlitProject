from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    def ready(self): # this function is called when the app is ready
        import shop.signals # this imports the signals.py file when the app is ready ( not included by default )