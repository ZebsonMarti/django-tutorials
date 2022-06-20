from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _t
from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()


def display_date(date):
    return date.strftime("%d-%m-%Y")


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimestampMixin):
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)

    def __str__(self):
        return self.email


class Skill(TimestampMixin):
    title = models.CharField(verbose_name="Skill", max_length=100, unique=True)

    def __str__(self):
        return self.title.upper()


class Address(TimestampMixin):
    raw_address = models.CharField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return self.raw_address.upper()

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Constants(TimestampMixin):
    title = models.CharField(max_length=100, null=False, blank=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )

    def __str__(self):
        return f"{self.title.upper()}: {self.amount}"

    class Meta:
        verbose_name = "Constants"
        verbose_name_plural = "Constants"


class Meeting(TimestampMixin):
    REGULAR = "REGULAR"
    EXTRA = "EXTRAORDINARY"
    MEETING_TYPES = [
        (REGULAR, _t("Séance Ordinaire")),
        (EXTRA, _t("Séance Extraordinaire")),
    ]
    date = models.DateField(verbose_name="Date", unique=True)
    address = models.ForeignKey(to=Address, default="", on_delete=models.SET_DEFAULT)
    hosts = models.ManyToManyField(
        to="Member", related_name="hosted_meetings", through="Hosts"
    )
    tontine_recipients = models.ManyToManyField(
        to="Member", related_name="recipient_dates", through="TontineRecipient"
    )
    type = models.CharField(
        verbose_name=_t("Type Séance"),
        max_length=15,
        choices=MEETING_TYPES,
        default=REGULAR,
    )
    agenda = models.CharField(
        verbose_name=_t("Ordre du jour"), max_length=255, null=True, blank=True
    )
    report = models.TextField(verbose_name=_t("Rapport"), null=True, blank=True)
    finance_ok = models.BooleanField(verbose_name=_t("Finances OK?"), default=False)
    sanction_ok = models.BooleanField(verbose_name=_t("Sanctions OK?"), default=False)
    validated = models.BooleanField(verbose_name=_t("Séance Validée"), default=False)

    class Meta:
        verbose_name = "Meeting"
        ordering = ["-date"]

    def __str__(self):
        return display_date(self.date)

    def meeting_hosts(self):
        h = [host.name for host in self.hosts.all()] if self.hosts else []
        return " / ".join(h)

    MEETING_TYPES_DICT = dict(MEETING_TYPES)

    @property
    def meeting_type(self):
        return Meeting.MEETING_TYPES_DICT.get(self.type)


class Member(TimestampMixin):
    MALE, FEMALE, OTHER = "MALE", "FEMALE", "OTHER"
    GENDER = [
        (MALE, _t("Homme")),
        (FEMALE, _t("Femme")),
        (OTHER, _t("Autre")),
    ]
    # Used to render the gender in template
    GENDER_DICT = dict(GENDER)

    ACTIVE, INACTIVE, PENDING = "ACTIVE", "INACTIVE", "PENDING"
    MEMBER_STATUS = [
        (ACTIVE, _t("Actif")),
        (INACTIVE, _t("Inactif")),
        (PENDING, _t("En cours")),
    ]
    # Used to render the member status in template
    STATUS_DICT = dict(MEMBER_STATUS)

    VILLAGES = [
        ("FOTETSA", "Fotetsa"),
        ("FONGO-NDENG", "Fongo-Ndeng"),
        ("FOSSONG-WENTCHENG", "Fossong-Wentcheng"),
        ("FONDONERA", "Fondonera"),
    ]

    user = models.OneToOneField(
        to=User, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    first_name = models.CharField(verbose_name=_t("Prénom"), max_length=255)
    last_name = models.CharField(verbose_name=_t("Nom"), max_length=255)
    sex = models.CharField(verbose_name=_t("Sexe"), max_length=6, choices=GENDER)
    phone = models.CharField(
        verbose_name=_t("N° Téléphone"), max_length=30, null=True, blank=True
    )
    status = models.CharField(
        verbose_name=_t("Statut"), max_length=10, choices=MEMBER_STATUS, default=PENDING
    )
    village = models.CharField(
        verbose_name=_t("Village"), max_length=20, choices=VILLAGES
    )

    # name = models.CharField(verbose_name="Full Name", max_length=100)
    # register_date = models.ForeignKey(
    #     to=Meeting, to_field="date", null=True, on_delete=models.SET_NULL
    # )
    address = models.ForeignKey(
        to=Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        to_field="raw_address",
    )
    registration_date = models.ForeignKey(
        to=Meeting, on_delete=models.DO_NOTHING, null=True, editable=False
    )
    registration_fee = models.DecimalField(
        verbose_name=_t("Montant Inscription"),
        max_digits=10,
        decimal_places=2,
        default=0.0,
        validators=[
            MinValueValidator(
                limit_value=0.0,
                message=_t("Le montant de l'inscription ne peut être négatif"),
            )
        ],
    )
    # Fond de roulement
    operation_fee = models.DecimalField(
        verbose_name=_t("Montant Inscription"),
        max_digits=10,
        decimal_places=2,
        default=0.0,
        validators=[
            MinValueValidator(
                limit_value=0.0,
                message=_t("Le montant de l'inscription ne peut être négatif"),
            )
        ],
    )
    profession = models.CharField(
        verbose_name=_t("Profession"), max_length=100, null=True, blank=True
    )
    skills = models.ManyToManyField(to=Skill)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name

    def member_skills(self):
        s = [skill.title for skill in self.skills.all()] if self.id else []
        return "/".join(s) if s else ""

    def reg_date(self):
        return display_date(self.registration_date.date)

    @property
    def gender(self):
        return Member.GENDER_DICT.get(self.sex)

    @property
    def membership_status(self):
        return Member.STATUS_DICT.get(self.status)


class ReceptionRound(TimestampMixin):
    start_date = models.ForeignKey(
        to=Meeting,
        to_field="date",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="start_reception_round",
    )
    end_date = models.ForeignKey(
        to=Meeting,
        to_field="date",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="end_reception_round",
    )

    def __str__(self):
        return f"START: {self.start}-END: {self.end}"

    @property
    def start(self):
        return display_date(self.start_date.date) if self.start_date else "-"

    @property
    def end(self):
        return display_date(self.end_date.date) if self.end_date else "-"

    class Meta:
        verbose_name = "Reception Round"
        verbose_name_plural = "Reception Rounds"
        ordering = ["-start_date__date"]


class Hosts(TimestampMixin):
    reception_round = models.ForeignKey(
        to=ReceptionRound, on_delete=models.SET_NULL, null=True
    )
    meeting = models.ForeignKey(
        to=Meeting,
        to_field="date",
        on_delete=models.CASCADE,
        null=False,
        related_name="member_list",
    )
    member = models.ForeignKey(
        to=Member, on_delete=models.SET_NULL, null=True, related_name="meeting_list"
    )

    class Meta:
        verbose_name = "Hosts"
        verbose_name_plural = "Hosts"
        ordering = ["-meeting__date", "member__first_name"]
        unique_together = [("reception_round", "meeting", "member")]

    def __str__(self):
        return f"({self.reception_round}, {self.meeting}, {self.member})"


class TontineRound(TimestampMixin):
    start_date = models.ForeignKey(
        to=Meeting,
        on_delete=models.CASCADE,
        related_name="start_tontine_round",
        null=False,
        blank=False,
    )
    end_date = models.ForeignKey(
        to=Meeting,
        on_delete=models.SET_NULL,
        related_name="end_tontine_round",
        null=True,
        blank=True,
    )
    pots = models.FloatField(verbose_name="NB Noms", default=1, null=False, blank=False)
    amount_per_pot = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, null=False, blank=False
    )

    def __str__(self):
        return f"START: {self.start}-END: {self.end}"

    @property
    def start(self):
        return display_date(self.start_date.date) if self.start_date else "-"

    @property
    def end(self):
        return display_date(self.end_date.date) if self.end_date else "-"

    class Meta:
        verbose_name = "Tontine Round"
        verbose_name_plural = "Tontine Rounds"
        ordering = ["-start_date__date"]


class TontineRecipient(TimestampMixin):
    tontine_round = models.ForeignKey(
        to=TontineRound,
        on_delete=models.SET_NULL,
        null=True,
    )
    meeting = models.ForeignKey(
        to=Meeting,
        # to_field="date",
        on_delete=models.CASCADE,
        null=False,
        related_name="recipient_dates",
    )
    member = models.ForeignKey(
        to=Member, on_delete=models.SET_NULL, null=True, related_name="recipient_list"
    )
    received_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )

    class Meta:
        verbose_name = "Tontine Recipient"
        verbose_name_plural = "Tontine Recipients"
        ordering = ["-meeting__date", "member__first_name"]
        # unique_together = [("tontine_round", "meeting", "member")]

    def __str__(self):
        return f"({self.tontine_round}, {self.meeting}, {self.member})"


class Board(TimestampMixin):
    start_date = models.ForeignKey(
        to=Meeting,
        # to_field="date",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="start_board",
    )
    end_date = models.ForeignKey(
        to=Meeting,
        # to_field="date",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="end_board",
    )

    def __str__(self):
        return f"START: {self.start}-END: {self.end}"

    @property
    def start(self):
        return display_date(self.start_date.date) if self.start_date else "-"

    @property
    def end(self):
        return display_date(self.end_date.date) if self.end_date else "-"

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"
        ordering = ["-start_date__date"]


class BoardPosition(TimestampMixin):
    title = models.CharField(
        verbose_name="Poste", max_length=100, unique=True, null=False, blank=False
    )

    def __str__(self):
        return self.title.upper() if self.title else ""


class BoardMember(TimestampMixin):
    board = models.ForeignKey(
        to=Board, null=True, on_delete=models.SET_NULL, blank=True
    )
    member = models.ForeignKey(
        to=Member, null=True, on_delete=models.SET_NULL, blank=False
    )
    position = models.ForeignKey(
        to=BoardPosition, null=True, on_delete=models.SET_NULL, blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.poste()

    def poste(self):
        return f"Bureau {self.board.id} -> {self.position.title.upper()}: {self.member.name.upper()}"


class AccountType(TimestampMixin):
    ORG, MEMBER, BOTH = 'ORG', 'MEMBER', 'BOTH'
    USED_FOR = [
        (ORG, _t('Réunion Uniquement')),
        (MEMBER, _t('Membres Uniquement')),
        (BOTH, _t('Réunion et Membres')),
    ]

    title = models.CharField(
        verbose_name="Name", max_length=30, unique=True, null=False, blank=False
    )
    code = models.CharField(verbose_name="Code", max_length=5, null=False, blank=False)
    used_for = models.CharField(verbose_name=_t('Pour'), max_length=6, choices=USED_FOR, default=BOTH, null=False, blank=True)

    def __str__(self):
        return self.title.upper()

    class Meta:
        ordering = ["title"]


class Transaction(TimestampMixin):
    transaction = None

    def __str__(self):
        return self.transaction

    class Meta:
        abstract = True

    meeting = models.ForeignKey(
        to=Meeting, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    account = models.ForeignKey(
        to=AccountType, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    title = models.CharField(max_length=255, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


class MemberTransaction(Transaction):
    member = models.ForeignKey(
        to=Member, on_delete=models.DO_NOTHING, null=False, blank=False
    )

    class Meta:
        verbose_name = "Member Transaction"
        verbose_name_plural = "Member Transactions"
        ordering = ["-created_at"]

    @property
    def transaction(self):
        return (
            f"{self.meeting.date},"
            f" {self.member.name}, "
            f"{self.title.upper()}, "
            f"{self.account.title.upper()}, "
            f"{self.amount}"
        )


class OrgTransaction(Transaction):
    @property
    def transaction(self):
        return (
            f"{self.meeting.date},"
            f"{self.title.upper()}, "
            f"{self.account.title.upper()}, "
            f"{self.amount}"
        )


class DocumentType(TimestampMixin):
    title = models.CharField(verbose_name="Intitulé", max_length=255, unique=True)

    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Document Types"

    def __str__(self):
        return self.title.upper()


class DocumentHistory(TimestampMixin):
    document_type = models.ForeignKey(
        to=DocumentType,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="document",
    )
    content = models.TextField()
    comment = models.TextField()

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ["-updated_at"]


class Sanction(TimestampMixin):
    class Meta:
        verbose_name = _t("Sanction")
        verbose_name_plural = _t("Sanctions")
        ordering = ["-meeting"]

    FINANCIAL = "FI"
    NON_FINANCIAL = "NF"
    BOTH = "BO"
    SANCTION_TYPES = [
        (FINANCIAL, _t("Financière")),
        (NON_FINANCIAL, _t("Non Financière")),
        (BOTH, _t("Les deux")),
    ]

    meeting = models.ForeignKey(
        to=Meeting,
        verbose_name=_t("Séance"),
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='sanctions'
    )
    member = models.ForeignKey(
        to=Member,
        verbose_name=_t("Membre"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='sanctions'
    )
    reason = models.CharField(
        verbose_name=_t("Raison"), max_length=255, null=False, blank=False
    )
    sanction_type = models.CharField(
        verbose_name=_t("Type Sanction"),
        max_length=2,
        choices=SANCTION_TYPES,
        default=FINANCIAL,
        null=False,
        blank=False,
    )
    amount = models.DecimalField(
        verbose_name=_t("Montant"),
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name=_t("Sanction"), max_length=200, null=True, blank=True
    )
    executed_or_paid = models.BooleanField(
        verbose_name=_t("Exécutée ou Payée?"), null=False, blank=False, default=False
    )

    def __str__(self):
        return f"{self.meeting}: {self.member}: {self.amount}: {self.title}"

    @property
    def type(self):
        return dict(self.SANCTION_TYPES)[self.sanction_type]


class Absence(TimestampMixin):
    class Meta:
        verbose_name = _t("Absence")
        verbose_name_plural = _t("Absences")
        # ordering = ["-meeting__date"]

    meeting = models.ForeignKey(
        to=Meeting,
        verbose_name=_t("Séance"),
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='absences'
    )
    member = models.ForeignKey(
        to=Member,
        verbose_name=_t("Membre"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='absences'
    )
    reason = models.CharField(
        verbose_name=_t("Raison"), max_length=255, null=False, blank=False
    )
    justified = models.BooleanField(
        verbose_name=_t("Justifiée?"), null=False, blank=False, default=False
    )
    sanctioned = models.BooleanField(
        verbose_name=_t("Sanctionné?"), null=False, blank=False, default=False
    )

    def __str__(self):
        return f"{self.meeting}: {self.member}: {self.reason}"


class Aid(TimestampMixin):
    class Meta:
        verbose_name = _t("Aide")
        verbose_name_plural = _t("Aides")
        # ordering = ["-meeting__date"]

    member = models.ForeignKey(
        to=Member,
        verbose_name=_t("Membre"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='aids'
    )

    reason = models.CharField(
        verbose_name=_t("Motif Aide"), max_length=255, null=False, blank=False
    )

    disbursed_amount = models.DecimalField(
        verbose_name=_t("Montant décaissé"),
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
    )

    amount_to_recover_by_member = models.DecimalField(
        verbose_name=_t("Montant à recouvrer par membre"),
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=True,
    )

    disbursal_meeting = models.ForeignKey(
        to=Meeting,
        verbose_name=_t("Séance Décaissement"),
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='aids'
    )
    recovery_meeting = models.ForeignKey(
        to=Meeting,
        verbose_name=_t("Séance Recouvrement"),
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name='aids_to_recover'
    )

    def __str__(self):
        return f"{self.member}: {self.disbursal_meeting}: {self.disbursed_amount}"


# class DocumentChapter(TimestampMixin):
#     title = models.CharField(verbose_name="Intitulé", max_length=255)
#     chapter_number = models.PositiveSmallIntegerField(
#         verbose_name="N°", null=False, blank=True
#     )
#     doc_type = models.ForeignKey(
#         to=DocumentType,
#         on_delete=models.CASCADE,
#         null=False,
#         blank=False,
#         related_name="chapters",
#     )
#
#     class Meta:
#         verbose_name = "Document Chapter"
#         verbose_name_plural = "Document Chapters"
#         ordering = ["doc_type", "title"]
#
#     def __str__(self):
#         return f"{self.doc_type}: {self.chapter_number} - {self.title.upper()}"
#
#
# class DocumentArticle(TimestampMixin):
#     content = models.CharField(verbose_name="Intitulé", max_length=255)
#     article_number = models.PositiveSmallIntegerField(
#         verbose_name="N°", null=False, blank=True
#     )
#     chapter = models.ForeignKey(
#         to=DocumentChapter,
#         on_delete=models.CASCADE,
#         null=False,
#         blank=False,
#         related_name="articles",
#     )
#
#     class Meta:
#         verbose_name = "Document Article"
#         verbose_name_plural = "Document Articles"
#         ordering = ["chapter__doc_type", "chapter", "article_number"]
#
#     def __str__(self):
#         return f"{self.chapter.doc_type}-{self.chapter}: {self.article_number} - {self.content.title()}"
