from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "nft_fetch.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import nft_fetch.users.signals
        except ImportError:
            pass
