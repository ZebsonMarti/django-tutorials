from django.contrib import admin
from . import models as m
# Register your models here.


# admin.site.register(m.Skill)

@admin.register(m.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']


@admin.register(m.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['raw_address', 'created_at', 'updated_at']