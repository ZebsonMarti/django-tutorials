class MemberHistoryLine(object):
    def __init__(
        self,
        *,
        date: str,
        absence: bool,
        reason_absence: str,
        assistance: float,
        project: float,
        savings: float,
        scholar_savings: float,
        sanction: float,
        sanction_reason: str,
        sanction_title: str,
        sanction_amount: float,
        sanction_paid: bool
    ) -> None:
        self.date = date
        self.absence = absence
        self.reason_absence = reason_absence
        self.assistance = assistance
        self.project = project
        self.savings = savings
        self.scholar_savings = scholar_savings
        self.sanction = sanction
        self.sanction_reason = sanction_reason
        self.sanction_title = sanction_title
        self.sanction_amount = sanction_amount
        self.sanction_paid = sanction_paid

    def __str__(self):
        return self.date

    def __repr__(self):
        return self.__str__()
