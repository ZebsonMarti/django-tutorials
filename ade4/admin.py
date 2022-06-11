from django.contrib import admin
from . import models as m

# Register your models here.


# admin.site.register(m.Skill)


@admin.register(m.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(m.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["raw_address", "created_at", "updated_at"]


@admin.register(m.Constants)
class ConstantAdmin(admin.ModelAdmin):
    list_display = ["title", "amount"]


@admin.register(m.Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ["date", "get_date", "meeting_hosts", "address"]

    def get_date(self, obj):
        return obj.date.strftime("%d-%m-%Y")


@admin.register(m.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "reg_date", "address", "member_skills"]


@admin.register(m.ReceptionRound)
class ReceptionRoundAdmin(admin.ModelAdmin):
    list_display = ["start", "end"]


@admin.register(m.Hosts)
class HostsAdmin(admin.ModelAdmin):
    list_display = ["reception_round", "meeting", "member"]


@admin.register(m.TontineRound)
class TontineAdmin(admin.ModelAdmin):
    list_display = ["start", "end", "pots", "amount_per_pot"]


@admin.register(m.TontineRecipient)
class TontineRecipientAdmin(admin.ModelAdmin):
    list_display = ["tontine_round", "meeting", "member", "received_amount"]


@admin.register(m.Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ["start", "end"]


@admin.register(m.BoardPosition)
class BoardPositionAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(m.BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ["poste", "created_at", "updated_at"]


@admin.register(m.AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "code"]
