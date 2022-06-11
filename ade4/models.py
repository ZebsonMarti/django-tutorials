from django.db import models

# Create your models here.


def display_date(date):
    return date.strftime("%d-%m-%Y")


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
    date = models.DateField(verbose_name="Date", unique=True)
    address = models.ForeignKey(to=Address, default="", on_delete=models.SET_DEFAULT)
    hosts = models.ManyToManyField(
        to="Member", related_name="hosted_meetings", through="Hosts"
    )

    class Meta:
        verbose_name = "Meeting"
        ordering = ["-date"]

    def __str__(self):
        return display_date(self.date)

    def meeting_hosts(self):
        h = [host.name for host in self.hosts.all()] if self.hosts else []
        return " / ".join(h)


class Member(TimestampMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(verbose_name="Full Name", max_length=100)
    register_date = models.ForeignKey(
        to=Meeting, to_field="date", null=True, on_delete=models.SET_NULL
    )
    address = models.ForeignKey(
        to=Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        to_field="raw_address",
    )
    skills = models.ManyToManyField(to=Skill)

    def __str__(self):
        return self.email

    def member_skills(self):
        s = [skill.title for skill in self.skills.all()] if self.id else []
        return "/".join(s) if s else ""

    def reg_date(self):
        return display_date(self.register_date.date)


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
        ordering = ["-meeting__date", "member__name"]
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
        to=ReceptionRound, on_delete=models.SET_NULL, null=True
    )
    meeting = models.ForeignKey(
        to=Meeting,
        to_field="date",
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
        ordering = ["-meeting__date", "member__name"]
        unique_together = [("tontine_round", "meeting", "member")]

    def __str__(self):
        return f"({self.tontine_round}, {self.meeting}, {self.member})"


class Board(TimestampMixin):
    start_date = models.ForeignKey(
        to=Meeting,
        to_field="date",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="start_board",
    )
    end_date = models.ForeignKey(
        to=Meeting,
        to_field="date",
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
    title = models.CharField(
        verbose_name="Name", max_length=30, unique=True, null=False, blank=False
    )
    code = models.CharField(verbose_name="Code", max_length=5, null=False, blank=False)

    def __str__(self):
        return self.title.upper()

    class Meta:
        ordering = ["title"]


class Transaction(TimestampMixin):
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

    def transaction(self):
        return f"{self.meeting.date}," \
               f" {self.member.name}, " \
               f"{self.title.upper()}, " \
               f"{self.account.title.upper()}, " \
               f"{self.amount}"

    def __str__(self):
        return self.transaction()
