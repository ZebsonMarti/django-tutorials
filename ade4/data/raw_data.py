from random import randint, random, choice

# Address

raw_addresses = [
    "Rue de la gare, 1/1, 1348 LLN",
    "Avenue Marcelo DJ, 50/12, 2206 Liège",
    "Mountain Street, 15/68, 22568 London",
    "Boulevard du président, 68/1, 7854 Montreal",
    "Place F4, 8/115, 59098 ESCH-Sur-Alzette",
    "Rue du stade, 36/2, 4000 Mons",
    "Passage du Mapan, 28/118, 1058 BXL",
    "Chez Maa Poh, 799/215, 965 YDE",
    "Carrefour 3 Bordelles, 1/618, 1369 DLa",
    "Carrefour mission, 251/135, 954 Toula",
    "Messeh Nzideng, 985 /754, 1568 Tsinkou",
    "85018 Helena Avenue, PL, USA",
    "0217 Holy Cross Parkway, CA France",
    "475 Bertillon Drive, DLA, Cameroun",
    "554 Ronald Regan Terrace, Dschang",
    "4 5th Plaza, New York, USA",
]

# Constants
constants = [
    ("Secours par membre", 50),
    ("Aide malheur", 350),
    ("Aide bonheur", 100),
    ("Inscription", 10),
    ("Fond de roulement", 15),
]

# Skill
skills = [
    "Infirmier",
    "Informaticien",
    "Heraldry",
    "Diagnose",
    "Observation",
    "Laundry",
    "Savoir-faire",
    "Charm Creature",
    "Recreational activities",
    "Explosives",
    "History",
    "Herb Lore",
    "Shadowing",
    "Anatomy",
    "Carpentry",
    "Stoneworking",
    "Taxidermy",
    "Burying",
    "Manual labor",
    "Torture",
    "Gesture",
    "Spot Trap",
]

# Meeting
N = len(raw_addresses)


def mt():
    return "REGULAR" if random() < 0.9 else "EXTRAORDINARY"


meetings = [
    {"date": "2018-02-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2018-04-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2018-06-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2018-08-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2018-10-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2018-12-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2019-02-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2019-04-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2019-06-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2019-08-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2019-10-06", "address": choice(raw_addresses), "type": mt()},
    {"date": "2019-12-01", "address": choice(raw_addresses), "type": mt()},
    {"date": "2020-02-02", "address": choice(raw_addresses), "type": mt()},
    {"date": "2020-04-05", "address": choice(raw_addresses), "type": mt()},
    {"date": "2020-06-07", "address": choice(raw_addresses), "type": mt()},
    {"date": "2020-08-02", "address": choice(raw_addresses), "type": mt()},
    {"date": "2020-10-04", "address": choice(raw_addresses), "type": mt()},
    {"date": "2020-12-06", "address": choice(raw_addresses), "type": mt()},
    {"date": "2021-02-07", "address": choice(raw_addresses), "type": mt()},
    {"date": "2021-04-04", "address": choice(raw_addresses), "type": mt()},
    {"date": "2021-06-04", "address": choice(raw_addresses), "type": mt()},
    {"date": "2021-08-04", "address": choice(raw_addresses), "type": mt()},
    {"date": "2021-10-05", "address": choice(raw_addresses), "type": mt()},
    {"date": "2021-12-05", "address": choice(raw_addresses), "type": mt()},
    {"date": "2022-02-05", "address": choice(raw_addresses), "type": mt()},
    {"date": "2022-04-02", "address": choice(raw_addresses), "type": mt()},
    {"date": "2022-06-05", "address": choice(raw_addresses), "type": mt()},
]

# Member

phones = [
    "+32 489 32 18 74",
    "+32 499 57 85 63",
    "+32 474 34 62 57",
    "+32 491 26 16 83",
    "+32 462 89 65 97",
    "+32 470 50 32 74",
    "+32 461 56 24 91",
    "+32 463 11 87 77",
    "+32 468 15 72 07",
    "+32 477 83 63 84",
    "+352 656 168 146",
    "+352 668 548 070",
    "+352 655 641 517",
    "+352 691 725 601",
    "+352 671 714 189",
    "+1 249-820-7574",
    "+1 204-269-9985",
    "+1 306-531-9901",
    "+1 306-853-9734",
    "+1 902-330-2748",
    "+33 6 61 25 08 55",
    "+33 7 47 23 21 45",
    "+33 7 00 83 51 20",
    "+33 6 01 29 21 17",
    "+33 7 95 40 11 53",
]

villages = [
    "FOTETSA",
    "FONGO-NDENG",
    "FOSSONG-WENTCHENG",
    "FONDONERA",
]

members = [
    {
        "email": "johnsmith@f4.com",
        "first_name": "John",
        "last_name": "Smith",
        "sex": "MALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "juliaroberts@f4.com",
        "first_name": "Julia",
        "last_name": "Roberts",
        "sex": "FEMALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "ajolie@f4.com",
        "first_name": "Angelina",
        "last_name": "Jolie",
        "sex": "FEMALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "llongue@f4.com",
        "first_name": "Longue",
        "last_name": "Longue",
        "sex": "MALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "ppays@f4.com",
        "first_name": "Petit",
        "last_name": "Pays",
        "sex": "MALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "tomcruise@f4.com",
        "first_name": "Tom",
        "last_name": "cruise",
        "sex": "MALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "averodjess@f4.com",
        "first_name": "Avero",
        "last_name": "Djess",
        "sex": "MALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "ndusud@f4.com",
        "first_name": "Nyangono",
        "last_name": "Du Sud",
        "sex": "MALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
    },
    {
        "email": "ladyponce@f4.com",
        "first_name": "Lady",
        "last_name": "Ponce",
        "sex": "FEMALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "manudibando@f4.com",
        "first_name": "Manu",
        "last_name": "Dibango",
        "sex": "MALE",
        "registration_date": "2018-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "malhox@f4.com",
        "first_name": "Malhox",
        "last_name": "Le vibeur",
        "sex": "MALE",
        "registration_date": "2019-02-01",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "petitbozard@f4.com",
        "first_name": "Petit",
        "last_name": "Bozard",
        "sex": "MALE",
        "registration_date": "2020-02-02",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "medecindemedelin@f4.com",
        "first_name": "Médecin",
        "last_name": "De Medelin",
        "sex": "MALE",
        "registration_date": "2020-02-02",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "kameni@f4.com",
        "first_name": "La Go",
        "last_name": "Kameni",
        "sex": "FEMALE",
        "registration_date": "2020-06-07",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "daphne@f4.com",
        "first_name": "La Go",
        "last_name": "Daphné",
        "sex": "FEMALE",
        "registration_date": "2020-06-07",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "murielleb@f4.com",
        "first_name": "Murielle",
        "last_name": "Blanche",
        "sex": "FEMALE",
        "registration_date": "2021-02-07",
        "address": choice(raw_addresses),
        "profession": choice(skills),
    },
    {
        "email": "poupi@f4.com",
        "first_name": "Marcelle",
        "last_name": "Poupi",
        "sex": "FEMALE",
        "registration_date": "2021-02-07",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "mitoumba@f4.com",
        "first_name": "Mitoumba",
        "last_name": "Manioc",
        "sex": "MALE",
        "registration_date": "2021-10-05",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
    {
        "email": "takam@f4.com",
        "first_name": "Takam",
        "last_name": "Le Mince",
        "sex": "MALE",
        "registration_date": "2021-10-05",
        "address": choice(raw_addresses),
        "phone": choice(phones),
        "village": choice(villages),
        "profession": choice(skills),
    },
]

# User

# ReceptionRound

# Hosts

# TontineRound

# TontineRecipient

# Board

# BoardPosition

# BoardMember

# Hosts

# TontineRound

# TontineRecipient

# Board

# BoardPosition

# BoardMember

# AccountType

# Transaction

# MemberTransaction

# OrgTransaction

# DocumentType

# DocumentChapter

# DocumentArticle
