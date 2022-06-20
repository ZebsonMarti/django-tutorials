from django.shortcuts import render

# Create your views here.
from .selectors import MemberFinance as MF


def member_finance(request):
    m = MF(email="johnsmith@f4.com")
    ctx = {
        "balances": m.account_balances,
        "his": m.history,
    }
    return render(request, "ade4/member_finance.html", ctx)
