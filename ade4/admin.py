from django.contrib import admin
from . import models as m

# Register your models here.


# admin.site.register(m.Skill)


@admin.register(m.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "created_at", "updated_at"]


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
    list_display = ["user", "name", "registration_date", "address", "member_skills"]


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


@admin.register(m.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["title", "used_for", "code"]


@admin.register(m.MemberTransaction)
class MemberTransactionAdmin(admin.ModelAdmin):
    list_display = ["transaction"]


@admin.register(m.OrgTransaction)
class OrgTransactionAdmin(admin.ModelAdmin):
    list_display = ["transaction"]


@admin.register(m.DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(m.DocumentHistory)
class DocumentHistoryAdmin(admin.ModelAdmin):
    list_display = ["document_type", "content", "comment"]


@admin.register(m.Sanction)
class SanctionAdmin(admin.ModelAdmin):
    list_display = ["meeting", "member", "sanction_reason", "amount", "sanction_type"]


@admin.register(m.Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ["meeting", "member", "absence_reason", "justified", "sanctioned"]


@admin.register(m.Aid)
class AidAdmin(admin.ModelAdmin):
    list_display = [
        "member",
        "reason",
        "disbursed_amount",
        "disbursal_meeting",
        "recovery_meeting",
        "amount_to_recover_by_member",
    ]


# @admin.register(m.DocumentChapter)
# class DocumentChapterAdmin(admin.ModelAdmin):
#     list_display = ["doc_type", "chapter_number", "title", "created_at", "updated_at"]
#
#
# @admin.register(m.DocumentArticle)
# class DocumentArticleAdmin(admin.ModelAdmin):
#     list_display = ["article_number", "content", "chapter"]
