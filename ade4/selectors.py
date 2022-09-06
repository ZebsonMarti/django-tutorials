from datetime import datetime
from django.db.models import FilteredRelation, Q, F
from .utils import MemberHistoryLine
from .models import MemberTransaction, Account, AccountType, Aid, Meeting


def get_accounts(*, used_for):
    if used_for.upper() == "MEMBER":
        used_for_list = [Account.MEMBER, Account.BOTH]
    elif used_for.upper() == "ORG":
        used_for_list = [Account.ORG, Account.BOTH]
    else:
        raise ValueError("Wrong argument value. Only Member and Org are allowed!")
    return [
        account.title
        for account in (
            Account.objects.filter(used_for__in=used_for_list).only("title").all()
        )
    ]


class MemberFinance(object):
    def __init__(self, email):
        qs = (
            MemberTransaction.objects.select_related(
                "meeting",
                "member",
                "member__user",
                "account",
            )
            .filter(member__user__email=email)
            .only(
                "meeting__date",
                "account__title",
                "amount",
                "member__id",
                "member__user",
            )
            .all()
        )

        self._member_accounts = [
            AccountType.ASSISTANCE,
            AccountType.SAVINGS,
            AccountType.SCHOLAR_SAVINGS,
            AccountType.PROJECT,
            AccountType.SANCTION,
        ]

        # Logged In Member
        self._member = qs[0].member
        # Transactions
        self._transactions = qs
        # Member's aids
        self._aids = self._member.aids.all() if qs else []

        self._date_format = "%m/%m/%Y"

        # History Table
        history = list(
            Meeting.objects.annotate(
                A=FilteredRelation(
                    "absences", condition=Q(absences__member=self._member.id)
                ),
                S=FilteredRelation(
                    "sanctions", condition=Q(sanctions__member=self._member.id)
                ),
            )
            .filter(date__lte=datetime.today())
            .values(
                "date",
                "A__absence_reason",
                "A__justified",
                "A__sanctioned",
                "S__sanction_reason",
                "S__amount",
                "S__sanction_type",
                "S__title",
                "S__executed_or_paid",
            )
            .all()
        )

        self._history = {}

        for line in history:
            date = line["date"].strftime(self._date_format)
            values = {
                key.split("__")[1]: (value or None)
                for key, value in line.items()
                if key != "date"
            }
            self._history[date] = values

    @property
    def account_balances(self):
        balances = {title: 0.0 for title in self._member_accounts}
        for transaction in self._transactions:
            balances[transaction.account.title] += float(transaction.amount)
        balances["absences"] = len(
            [1 for _, line in self._history.items() if line["absence_reason"]]
        )
        balances["assistance_aid"] = len(
            [1 for aid in self._aids if aid.aid_type == Aid.ASSISTANCE]
        )
        balances["happiness_aid"] = len(
            [1 for aid in self._aids if aid.aid_type == Aid.HAPPINESS]
        )
        return balances

    @property
    def history(self):
        date_format = "%m/%m/%Y"
        base_dict = {title: 0 for title in self._member_accounts}
        base_dict.update(
            {
                "absence": False,
                "absence_reason": "",
                "justified": "",
                "sanctioned": "",
                "sanction_reason": "",
                "amount": "",
                "sanction_type": "",
                "title": "",
                "executed_or_paid": "",
            }
        )
        for transaction in self._transactions:
            date = transaction.meeting.date.strftime(self._date_format)
            if date not in self._history:
                # Normally, this must never happen
                self._history[date] = base_dict.copy()
            self._history[date][transaction.account.title] = float(transaction.amount)

        return (
            self._history.items()
        )  # [MemberHistoryLine(date=date, **values) for date, values in his.items()]


"""
from ade4.selectors import MemberFinance as MF
m = MF(email='johnsmith@f4.com')
q = m.queryset
m.account_balances

for date, vals in d.items():
    print(date)
    for c, v in vals.items():
        print('\t',c,': ',v)

me = Meeting.objects.filter(date__lte=datetime(2022, 6, 21)).all().values('date', 'absences').extra(where=[f"member_id={member.id} OR member_id IS NULL"]).all()
me = Meeting.objects.filter(date__lte=datetime.today()).all().values('date', 'absences').extra(where=[f"member_id={member.id} OR member_id IS NULL"]).all()


SELECT "ade4_meeting"."date", "ade4_absence"."reason", "ade4_absence"."member_id" 
FROM "ade4_meeting" LEFT OUTER JOIN "ade4_absence" ON 
    ("ade4_meeting"."id" = "ade4_absence"."meeting_id") 
WHERE ("ade4_meeting"."date" < 2022-06-21 AND (member_id=1 OR member_id IS NULL)) 
ORDER BY "ade4_meeting"."date" DESC


me = Meeting.objects.annotate(
pizzas_vegetarian=FilteredRelation(
'absences__member_id', condition=Q(absences__member_id=member.id),)
).filter(date__lte=datetime.today()).all().values('date', 'absences').all()

me = Meeting.objects.annotate(
    A=FilteredRelation('absences', condition=Q(absences__member=member.id))
).filter(date__lte=datetime.today()).all().values('date', 'A__reason').all()

me = Meeting.objects.annotate(
    A=FilteredRelation('absences', condition=Q(absences__member=member.id)),
    S=FilteredRelation('sanctions', condition=Q(sanctions__member=member.id))
).filter(date__lte=datetime.today()).all().values('date', 'A__reason', 'S__amount').all()

me = Meeting.objects.annotate(
    A=FilteredRelation('absences', condition=Q(absences__member=member.id)),
    S=FilteredRelation('sanctions', condition=Q(sanctions__member=member.id))
).filter(date__lte=datetime.today()).values('date', 'A__reason', 'S__amount').annotate(
    reason=F('A__reason'), amount=F('S__amount')
)


"""
