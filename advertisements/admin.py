from django.contrib import admin

from advertisements.models import Advertisement

admin.site.register(Advertisement)


class AdvertisementAdmin(admin.ModelAdmin):
    pass
