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


@admin.register(m.Constants)
class ConstantAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount']


@admin.register(m.Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['date', 'get_date', 'address']

    def get_date(self, obj):
        return obj.date.strftime('%d-%m-%Y')


@admin.register(m.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'reg_date', 'address', 'member_skills']


