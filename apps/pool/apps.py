from django.apps import AppConfig


class PoolConfig(AppConfig):
    name = "apps.pool"

    def ready(self):
        import apps.pool.signals
