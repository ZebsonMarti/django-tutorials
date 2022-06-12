from django.core.management.base import BaseCommand, CommandError
from ade4.data.service import (
    insert_constants,
    insert_skills,
    insert_addresses,
    insert_meetings,
    insert_members_and_users,
)
from ade4.data.raw_data import constants, skills, raw_addresses, meetings, members


class Command(BaseCommand):
    help = "command to insert the data in the database"

    def handle(self, *args, **kwargs):
        i = insert_constants(constant_list=constants)
        sks = insert_skills(skill_list=skills)
        addr = insert_addresses(address_list=raw_addresses)
        meet = insert_meetings(meeting_list=meetings)
        mem = insert_members_and_users(members)
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
