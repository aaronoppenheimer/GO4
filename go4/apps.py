from django.contrib.admin.apps import AdminConfig

class Go4AdminConfig(AdminConfig):
    default_site = "go4.admin.Go4AdminSite"
