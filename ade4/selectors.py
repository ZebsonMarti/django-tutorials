from typing import Dict

from .utils import MemberHistoryLine
from .models import MemberTransaction, Account, AccountType, Aid


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
            .prefetch_related("member__absences", "member__aids", "member__sanctions")
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
        ]  # get_accounts(used_for="Member")

        self._transactions = qs
        self._absences = qs[0].member.absences.all() if qs else None
        self._sanctions = qs[0].member.sanctions.all() if qs else None
        self._aids = qs[0].member.aids.all() if qs else None

    @property
    def account_balances(self):
        balances = {title: 0.0 for title in self._member_accounts}
        for transaction in self._transactions:
            balances[transaction.account.title] += float(transaction.amount)
        balances["absences"] = len(self._absences)
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
                "reason_absence": "",
                "sanction_reason": "",
                "sanction_title": "",
                "sanction_amount": "",
                "sanction_paid": "",
            }
        )
        his = {}
        for transaction in self._transactions:
            date = transaction.meeting.date.strftime(date_format)
            if date not in his:
                his[date] = base_dict.copy()
            his[date][transaction.account.title] = float(transaction.amount)
        for absence in self._absences:
            date = absence.meeting.date.strftime(date_format)
            if date not in his:
                his[date] = base_dict.copy()
            his[date]["absence"] = "Yes"
            his[date]["reason_absence"] = absence.reason
        for sanction in self._sanctions:
            date = sanction.meeting.date.strftime(date_format)
            if date not in his:
                his[date] = base_dict.copy()
            his[date]["sanction_amount"] = float(sanction.amount) or 0
            his[date]["sanction_reason"] = sanction.reason
            his[date]["sanction_title"] = sanction.title
            his[date]["sanction_paid"] = sanction.executed_or_paid

        return [MemberHistoryLine(date=date, **values) for date, values in his.items()]


"""
from ade4.selectors import MemberFinance as MF
m = MF(email='johnsmith@f4.com')
q = m.queryset
m.account_balances

for date, vals in d.items():
    print(date)
    for c, v in vals.items():
        print('\t',c,': ',v)

"""
