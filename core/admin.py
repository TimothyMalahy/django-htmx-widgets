from django.contrib import admin
from core.models import People


# Register your models here.
@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age")
