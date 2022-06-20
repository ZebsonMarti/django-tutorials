from django.db.models import Sum
from .models import MemberTransaction


class MemberFinance:
    def __init__(self, email):
        self.queryset = (
            MemberTransaction.objects.prefetch_related(
                "meeting", "member", "member__user", "account"
            )
            .filter(member__user__email=email)
            .only("meeting__date", "account__title", "amount")
            .all()
        )

    @property
    def account_balances(self):
        pass
