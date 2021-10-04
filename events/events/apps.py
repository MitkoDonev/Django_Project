from django.contrib.admin import apps


class MyClubAdminConfig(apps.AdminConfig):
    default_site = "events.admin.MyClubAdmin"
