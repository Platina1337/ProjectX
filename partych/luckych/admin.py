from django.contrib import admin

from .models import *


# Register your models here.
# class Appoint(admin.ModelAdmin):
#     list_display = [field.name for field in AppointMeeting._meta.fields]
#
#     class Meta:
#         model = AppointMeeting
#
#
# admin.site.register(Appoint, AppointMeeting)
class Appoint(admin.ModelAdmin):
    list_display = [field.name for field in AppointMeeting._meta.fields]

admin.site.register(AppointMeeting, Appoint)
class Cat(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

admin.site.register(Category, Cat)