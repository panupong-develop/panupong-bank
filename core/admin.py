# Register your models here.
from django.contrib import admin

from .models import IncomingRequest


class IReqAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ipware",
        "ipinfo",
        "latitude",
        "longitude",
        "track_date",
    )

admin.site.register(IncomingRequest, IReqAdmin)
