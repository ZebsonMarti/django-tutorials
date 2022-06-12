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
            user = User.objects.create(email=email)

            # Registration Date
            try:
                meeting = Meeting.objects.get(
                    date=date.fromisoformat(m["registration_date"])
                )
            except Meeting.DoesNotExist:
                meeting = None

            # Address
            address, _ = Address.objects.get_or_create(raw_address=m["address"])
            members.append(
                Member(
                    user=user,
                    email=email,
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
