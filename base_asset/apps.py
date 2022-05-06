from django.apps import AppConfig


class BaseAssetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_asset'
