from django.core.management.base import BaseCommand, CommandError
from ade4.data.service import (
    insert_constants,
    insert_skills,
    insert_addresses,
    insert_meetings,
    insert_members_and_users,
    insert_reception_rounds,
    insert_hosts,
    insert_tontine_rounds,
    insert_tontine_recipients,
    insert_board_positions,
    insert_boards_and_board_members,
    insert_account_types,
    insert_member_transactions,
    insert_org_transactions,
    insert_document_types,
)
from ade4.data.raw_data import (
    constants,
    skills,
    raw_addresses,
    meetings,
    members,
    reception_rounds,
    board_positions,
    hosts,
    tontine_rounds,
    tontine_recipients,
    boards,
    account_types,
    member_transactions,
    org_transactions,
    document_types,
)


class Command(BaseCommand):
    help = "command to insert the data in the database"

    def handle(self, *args, **kwargs):
        _ = insert_constants(constant_list=constants)
        _ = insert_skills(skill_list=skills)
        _ = insert_addresses(address_list=raw_addresses)
        _ = insert_meetings(meeting_list=meetings)
        _ = insert_members_and_users(member_list=members)
        _ = insert_reception_rounds(rounds=reception_rounds)
        _ = insert_hosts(host_list=hosts)
        _ = insert_tontine_rounds(rounds=tontine_rounds)
        _ = insert_tontine_recipients(recipients_list=tontine_recipients)
        _ = insert_board_positions(position_list=board_positions)
        _ = insert_boards_and_board_members(board_list=boards)
        _ = insert_account_types(account_list=account_types)
        _ = insert_member_transactions(transaction_list=member_transactions)
        _ = insert_org_transactions(transaction_list=org_transactions)
        _ = insert_document_types(document_type_list=document_types)

        self.stdout.write(self.style.SUCCESS(f"All data have been inserted"))
        # try:
        #     cts = insert_constants(constant_list=constants)
        #     sks = insert_skills(skill_list=skills)
        #     addr = insert_addresses(address_list=raw_addresses)
        #     meet = insert_meetings(meeting_list=meetings)
        #     mem = insert_members_and_users(members)
        #     self.stdout.write(self.style.SUCCESS(f"All data have been inserted"))
        # except:
        #     self.stdout.write(self.style.ERROR(f"SOMETHING WENT WRONG:"))
