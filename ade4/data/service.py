"""Insert raw data in the DB"""
from datetime import date
from typing import List, Tuple, Dict

from ..models import *


def insert_addresses(address_list: List[str] = []) -> bool:
    table_empty = Address.objects.all().count() == 0
    if table_empty:
        _ = Address.objects.bulk_create(
            [Address(raw_address=addr) for addr in address_list]
        )
        return True
    return False


def insert_constants(constant_list: List[Tuple[str, float]]) -> bool:
    table_empty = Constants.objects.all().count() == 0
    if table_empty:
        _ = Constants.objects.bulk_create(
            [Constants(title=c[0], amount=c[1]) for c in constant_list]
        )
        return True
    return False


def insert_skills(skill_list: List[str]) -> bool:
    table_empty = Skill.objects.all().count() == 0
    if table_empty:
        _ = Skill.objects.bulk_create([Skill(title=skill) for skill in skill_list])
        return True
    return False


def insert_meetings(meeting_list: List[Dict]) -> bool:
    table_empty = Meeting.objects.all().count() == 0
    if table_empty:
        meetings = []
        for m in meeting_list:
            address, _ = Address.objects.get_or_create(raw_address__iexact=m["address"])
            meetings.append(
                Meeting(
                    date=date.fromisoformat(m["date"]), address=address, type=m["type"]
                )
            )
        _ = Meeting.objects.bulk_create(meetings)
        return True
    return False


def insert_members_and_users(member_list: List[Dict]) -> bool:

    table_empty = Member.objects.all().count() == 0
    if table_empty:
        members = []
        for m in member_list:
            # Create the User
            email = m["email"]
            user, _ = User.objects.get_or_create(email=email)

            # Registration Date
            try:
                meeting = Meeting.objects.get(
                    date=date.fromisoformat(m["registration_date"]["date"])
                )
            except Meeting.DoesNotExist:
                meeting = None

            # Address
            address, _ = Address.objects.get_or_create(raw_address=m["address"])
            members.append(
                Member(
                    user=user,
                    first_name=m["first_name"],
                    last_name=m["last_name"],
                    sex=m["sex"],
                    phone=m["phone"],
                    status="ACTIVE",
                    village=m["village"],
                    address=address,
                    registration_date=meeting,
                    registration_fee=10,
                    operation_fee=15,
                    profession=m["profession"],
                )
            )
        _ = Member.objects.bulk_create(members)
        return True
    return False


def insert_reception_rounds(rounds: List[Dict]) -> bool:
    table_empty = ReceptionRound.objects.all().count() == 0
    if table_empty:
        rr = []
        for r in rounds:
            start_date = r["start"]["date"]
            end_date = r["end"]["date"]
            start_meeting = (
                Meeting.objects.filter(date=date.fromisoformat(start_date)).first()
                if start_date
                else None
            )
            end_meeting = (
                Meeting.objects.filter(date=date.fromisoformat(end_date)).first()
                if end_date
                else None
            )
            rr.append(ReceptionRound(start_date=start_meeting, end_date=end_meeting))
        _ = ReceptionRound.objects.bulk_create(rr)
        return True
    return False


def insert_hosts(host_list: List[Dict]) -> bool:
    table_empty = Hosts.objects.all().count() == 0
    if table_empty:
        hosts = []
        for h in host_list:
            rr = ReceptionRound.objects.get(
                start_date=date.fromisoformat(h["reception_round"]["start"]["date"]),
                end_date=date.fromisoformat(h["reception_round"]["end"]["date"]),
            )
            for meeting in h["meetings"]:
                m = Meeting.objects.get(
                    date=date.fromisoformat(meeting["meeting_date"]["date"])
                )
                for raw_member in meeting["members"]:
                    member = Member.objects.get(
                        first_name__iexact=raw_member["first_name"],
                        last_name__iexact=raw_member["last_name"],
                    )
                    hosts.append(Hosts(reception_round=rr, meeting=m, member=member))
        Hosts.objects.bulk_create(hosts)
        return True
    return False


def insert_tontine_rounds(rounds: List[Dict]) -> bool:
    table_empty = TontineRound.objects.all().count() == 0
    if table_empty:
        tr = []
        for r in rounds:
            start_date = r["start"]["date"]
            end_date = r["end"]["date"]
            start_meeting = (
                Meeting.objects.filter(date=date.fromisoformat(start_date)).first()
                if start_date
                else None
            )
            end_meeting = (
                Meeting.objects.filter(date=date.fromisoformat(end_date)).first()
                if end_date
                else None
            )
            tr.append(
                TontineRound(
                    start_date=start_meeting,
                    end_date=end_meeting,
                    pots=r["buckets"],
                    amount_per_pot=r["amount_pb"],
                )
            )
        _ = TontineRound.objects.bulk_create(tr)
        return True
    return False


def insert_tontine_recipients(recipients_list: List[Dict]) -> bool:
    table_empty = TontineRecipient.objects.all().count() == 0
    if table_empty:
        recipients = []
        for r in recipients_list:
            tr = TontineRound.objects.get(
                start_date=Meeting.objects.get(
                    date=date.fromisoformat(r["tontine_round"]["start"]["date"])
                ),
                end_date=Meeting.objects.get(
                    date=date.fromisoformat(r["tontine_round"]["end"]["date"])
                ),
            )
            for meeting in r["meetings"]:
                m = Meeting.objects.get(
                    date=date.fromisoformat(meeting["meeting"]["date"])
                )
                for raw_member in meeting["recipients"]:
                    member = Member.objects.get(
                        first_name__iexact=raw_member["first_name"],
                        last_name__iexact=raw_member["last_name"],
                    )
                    recipients.append(
                        TontineRecipient(
                            tontine_round=tr,
                            meeting=m,
                            member=member,
                            received_amount=r["tontine_round"]["jackpot"],
                        )
                    )
        _ = TontineRecipient.objects.bulk_create(recipients)
        # for rec in recipients:
        #     print(rec)
        #     rec.save()
        return True
    return False


def insert_board_positions(position_list: List[Dict]) -> bool:
    table_empty = BoardPosition.objects.all().count() == 0
    if table_empty:
        positions = []
        for position in position_list:
            positions.append(BoardPosition(title=position))
        _ = BoardPosition.objects.bulk_create(positions)
        return True
    return False


def insert_boards_and_board_members(board_list: List[Dict]) -> bool:
    table_empty = Board.objects.all().count() == 0
    if table_empty:
        board_members = []
        for b in board_list:
            board = Board.objects.create(
                start_date=Meeting.objects.get(
                    date=date.fromisoformat(b["board"]["start"]["date"])
                ),
                end_date=Meeting.objects.get(
                    date=date.fromisoformat(b["board"]["end"]["date"])
                ),
            )
            for pos in b["positions"]:
                pos_str = pos["position"]
                first_name = pos["member"]["first_name"]
                last_name = pos["member"]["last_name"]
                position = BoardPosition.objects.get(title__iexact=pos_str)
                member = Member.objects.get(
                    first_name__iexact=first_name, last_name__iexact=last_name
                )
                board_members.append(
                    BoardMember(board=board, position=position, member=member)
                )

        _ = BoardMember.objects.bulk_create(board_members)
        return True
    return False


def insert_account_types(account_list: List[str]) -> bool:
    table_empty = AccountType.objects.all().count() == 0
    if table_empty:
        accounts = []
        for account in account_list:
            accounts.append(AccountType(title=account))
        _ = AccountType.objects.bulk_create(accounts)
        return True
    return False


def insert_member_transactions(transaction_list: List[Dict]) -> bool:
    table_empty = MemberTransaction.objects.all().count() == 0
    if table_empty:
        transactions = []
        for mt in transaction_list:
            meeting = Meeting.objects.get(
                date=date.fromisoformat(mt["meeting"]["date"])
            )
            for transaction_type in mt["transactions"]:
                account = AccountType.objects.get(
                    title__iexact=transaction_type["account"]
                )
                for m in transaction_type["members"]:
                    # print("\n", m["name"], '\n')
                    member = Member.objects.get(
                        first_name__iexact=m["name"]["first_name"],
                        last_name__iexact=m["name"]["last_name"],
                    )
                    transactions.append(
                        MemberTransaction(
                            meeting=meeting,
                            member=member,
                            account=account,
                            amount=m["amount"],
                            title=f"{transaction_type['account']}-{m['name']['first_name']} {m['name']['last_name']}",
                        )
                    )
        _ = MemberTransaction.objects.bulk_create(transactions)
        return True
    return False


def insert_org_transactions(transaction_list: List[Dict]) -> bool:
    table_empty = OrgTransaction.objects.all().count() == 0
    if table_empty:
        transactions = []
        for m in transaction_list:
            meeting = Meeting.objects.get(date=date.fromisoformat(m["meeting"]["date"]))
            for balance in m["balances"]:
                account = AccountType.objects.get(title__iexact=balance["account"])
                transactions.append(
                    OrgTransaction(
                        meeting=meeting,
                        account=account,
                        amount=balance["amount"],
                        title=f"{balance['account']}-{m['meeting']['date']}",
                    )
                )
        _ = OrgTransaction.objects.bulk_create(transactions)
        return True
    return False


def insert_document_types(document_type_list: List[str]) -> bool:
    table_empty = DocumentType.objects.all().count() == 0
    if table_empty:
        docs = []
        for doc_type in document_type_list:
            docs.append(DocumentType(title=doc_type))
        _ = DocumentType.objects.bulk_create(docs)
        return True
    return False


def insert_sanctions(sanction_list: List[Dict]) -> bool:
    table_empty = Sanction.objects.all().count() == 0
    if table_empty:
        sanctions = []
        for s in sanction_list:
            if s["members"]:
                meeting = Meeting.objects.get(
                    date=date.fromisoformat(s["meeting"]["date"])
                )
                for m in s["members"]:
                    member = Member.objects.get(
                        first_name__iexact=m["name"]["first_name"],
                        last_name__iexact=m["name"]["last_name"],
                    )
                    sanctions.append(
                        Sanction(
                            member=member,
                            meeting=meeting,
                            reason=m["reason"],
                            amount=m["amount"],
                            executed_or_paid=m["executed_or_paid"],
                        )
                    )
        _ = Sanction.objects.bulk_create(sanctions)
        return True
    return False


def insert_absences(absence_list: List[Dict]) -> bool:
    table_empty = Absence.objects.all().count() == 0
    if table_empty:
        absences = []
        for s in absence_list:
            if s["members"]:
                meeting = Meeting.objects.get(
                    date=date.fromisoformat(s["meeting"]["date"])
                )
                for m in s["members"]:
                    member = Member.objects.get(
                        first_name__iexact=m["name"]["first_name"],
                        last_name__iexact=m["name"]["last_name"],
                    )
                    absences.append(
                        Absence(
                            member=member,
                            meeting=meeting,
                            reason=m["reason"],
                        )
                    )
        _ = Absence.objects.bulk_create(absences)
        return True
    return False


def insert_aids(aid_list: List[Dict]) -> bool:
    table_empty = Aid.objects.all().count() == 0
    if table_empty:
        aids = []
        for aid in aid_list:
            first_name, last_name = (
                aid["member"]["first_name"],
                aid["member"]["last_name"],
            )
            member = Member.objects.get(
                first_name__iexact=first_name,
                last_name__iexact=last_name,
            )
            disbursal_meeting = Meeting.objects.get(
                date=date.fromisoformat(aid["disbursal_meeting"]['date'])
            )
            recovery_meeting = Meeting.objects.get(
                date=date.fromisoformat(aid["recovery_meeting"]['date'])
            )
            reason = f"{aid['reason']} de {first_name} {last_name}"
            aids.append(
                Aid(
                    member=member,
                    reason=reason,
                    disbursed_amount=aid["disbursed_amount"],
                    disbursal_meeting=disbursal_meeting,
                    recovery_meeting=recovery_meeting,
                    amount_to_recover_by_member=aid["amount_to_recover_by_member"],
                )
            )
        _ = Aid.objects.bulk_create(aids)
        return True
    return False
