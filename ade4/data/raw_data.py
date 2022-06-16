from random import random, choice

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


m_02_2018 = {"date": "2018-02-01", "address": choice(raw_addresses), "type": mt()}
m_04_2018 = {"date": "2018-04-01", "address": choice(raw_addresses), "type": mt()}
m_06_2018 = {"date": "2018-06-01", "address": choice(raw_addresses), "type": mt()}
m_08_2018 = {"date": "2018-08-01", "address": choice(raw_addresses), "type": mt()}
m_10_2018 = {"date": "2018-10-01", "address": choice(raw_addresses), "type": mt()}
m_12_2018 = {"date": "2018-12-01", "address": choice(raw_addresses), "type": mt()}
m_02_2019 = {"date": "2019-02-01", "address": choice(raw_addresses), "type": mt()}
m_04_2019 = {"date": "2019-04-01", "address": choice(raw_addresses), "type": mt()}
m_06_2019 = {"date": "2019-06-01", "address": choice(raw_addresses), "type": mt()}
m_08_2019 = {"date": "2019-08-01", "address": choice(raw_addresses), "type": mt()}
m_10_2019 = {"date": "2019-10-01", "address": choice(raw_addresses), "type": mt()}
m_12_2019 = {"date": "2019-12-01", "address": choice(raw_addresses), "type": mt()}
m_02_2020 = {"date": "2020-02-01", "address": choice(raw_addresses), "type": mt()}
m_04_2020 = {"date": "2020-04-01", "address": choice(raw_addresses), "type": mt()}
m_06_2020 = {"date": "2020-06-01", "address": choice(raw_addresses), "type": mt()}
m_08_2020 = {"date": "2020-08-01", "address": choice(raw_addresses), "type": mt()}
m_10_2020 = {"date": "2020-10-01", "address": choice(raw_addresses), "type": mt()}
m_12_2020 = {"date": "2020-12-01", "address": choice(raw_addresses), "type": mt()}
m_02_2021 = {"date": "2021-02-01", "address": choice(raw_addresses), "type": mt()}
m_04_2021 = {"date": "2021-04-01", "address": choice(raw_addresses), "type": mt()}
m_06_2021 = {"date": "2021-06-01", "address": choice(raw_addresses), "type": mt()}
m_08_2021 = {"date": "2021-08-01", "address": choice(raw_addresses), "type": mt()}
m_10_2021 = {"date": "2021-10-01", "address": choice(raw_addresses), "type": mt()}
m_12_2021 = {"date": "2021-12-01", "address": choice(raw_addresses), "type": mt()}
m_02_2022 = {"date": "2022-02-01", "address": choice(raw_addresses), "type": mt()}
m_04_2022 = {"date": "2022-04-01", "address": choice(raw_addresses), "type": mt()}
m_06_2022 = {"date": "2022-06-01", "address": choice(raw_addresses), "type": mt()}
m_08_2022 = {"date": "2022-08-01", "address": choice(raw_addresses), "type": mt()}
m_10_2022 = {"date": "2022-10-01", "address": choice(raw_addresses), "type": mt()}
m_12_2022 = {"date": "2022-12-01", "address": choice(raw_addresses), "type": mt()}
m_02_2023 = {"date": "2023-02-01", "address": choice(raw_addresses), "type": mt()}
m_04_2023 = {"date": "2023-04-01", "address": choice(raw_addresses), "type": mt()}
m_06_2023 = {"date": "2023-06-01", "address": choice(raw_addresses), "type": mt()}

meetings = [
    m_02_2018,
    m_04_2018,
    m_06_2018,
    m_08_2018,
    m_10_2018,
    m_12_2018,
    m_02_2019,
    m_04_2019,
    m_06_2019,
    m_08_2019,
    m_10_2019,
    m_12_2019,
    m_02_2020,
    m_04_2020,
    m_06_2020,
    m_08_2020,
    m_10_2020,
    m_12_2020,
    m_02_2021,
    m_04_2021,
    m_06_2021,
    m_08_2021,
    m_10_2021,
    m_12_2021,
    m_02_2022,
    m_04_2022,
    m_06_2022,
    m_08_2022,
    m_10_2022,
    m_12_2022,
    m_02_2023,
    m_04_2023,
    m_06_2023,
]

# Member and User

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
john_smith = {
    "email": "johnsmith@f4.com",
    "first_name": "John",
    "last_name": "Smith",
    "sex": "MALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
julia_roberts = {
    "email": "juliaroberts@f4.com",
    "first_name": "Julia",
    "last_name": "Roberts",
    "sex": "FEMALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
angelina_jolie = {
    "email": "ajolie@f4.com",
    "first_name": "Angelina",
    "last_name": "Jolie",
    "sex": "FEMALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
longue = {
    "email": "llongue@f4.com",
    "first_name": "Longue",
    "last_name": "Longue",
    "sex": "MALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
petit_pays = {
    "email": "ppays@f4.com",
    "first_name": "Petit",
    "last_name": "Pays",
    "sex": "MALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
tom_cruise = {
    "email": "tomcruise@f4.com",
    "first_name": "Tom",
    "last_name": "cruise",
    "sex": "MALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
avero = {
    "email": "averodjess@f4.com",
    "first_name": "Avero",
    "last_name": "Djess",
    "sex": "MALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
nyangono = {
    "email": "ndusud@f4.com",
    "first_name": "Nyangono",
    "last_name": "Du Sud",
    "sex": "MALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
lady_ponce = {
    "email": "ladyponce@f4.com",
    "first_name": "Lady",
    "last_name": "Ponce",
    "sex": "FEMALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
manu_dibango = {
    "email": "manudibando@f4.com",
    "first_name": "Manu",
    "last_name": "Dibango",
    "sex": "MALE",
    "registration_date": m_02_2018,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
malhox = {
    "email": "malhox@f4.com",
    "first_name": "Malhox",
    "last_name": "Le vibeur",
    "sex": "MALE",
    "registration_date": m_02_2019,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
petit_bozard = {
    "email": "petitbozard@f4.com",
    "first_name": "Petit",
    "last_name": "Bozard",
    "sex": "MALE",
    "registration_date": m_02_2020,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
medecein_de_medelin = {
    "email": "medecindemedelin@f4.com",
    "first_name": "Médecin",
    "last_name": "De Medelin",
    "sex": "MALE",
    "registration_date": m_02_2020,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
kameni = {
    "email": "kameni@f4.com",
    "first_name": "La Go",
    "last_name": "Kameni",
    "sex": "FEMALE",
    "registration_date": m_06_2020,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
daphne = {
    "email": "daphne@f4.com",
    "first_name": "La Go",
    "last_name": "Daphné",
    "sex": "FEMALE",
    "registration_date": m_06_2020,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
murielle_blanche = {
    "email": "murielleb@f4.com",
    "first_name": "Murielle",
    "last_name": "Blanche",
    "sex": "FEMALE",
    "registration_date": m_02_2021,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
poupi = {
    "email": "poupi@f4.com",
    "first_name": "Marcelle",
    "last_name": "Poupi",
    "sex": "FEMALE",
    "registration_date": m_02_2021,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
mitoumba = {
    "email": "mitoumba@f4.com",
    "first_name": "Mitoumba",
    "last_name": "Manioc",
    "sex": "MALE",
    "registration_date": m_10_2021,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
takam = {
    "email": "takam@f4.com",
    "first_name": "Takam",
    "last_name": "Le Mince",
    "sex": "MALE",
    "registration_date": m_10_2021,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}
mbatremy = {
    "email": "mbatremy@f4.com",
    "first_name": "Paah",
    "last_name": "Mbatremy",
    "sex": "MALE",
    "registration_date": m_10_2021,
    "address": choice(raw_addresses),
    "phone": choice(phones),
    "village": choice(villages),
    "profession": choice(skills),
}


members = [
    john_smith,
    julia_roberts,
    angelina_jolie,
    longue,
    petit_pays,
    tom_cruise,
    avero,
    nyangono,
    lady_ponce,
    manu_dibango,
    malhox,
    petit_bozard,
    medecein_de_medelin,
    kameni,
    daphne,
    murielle_blanche,
    poupi,
    mitoumba,
    takam,
    mbatremy,
]

# ReceptionRound
tr_1 = {"start": m_02_2018, "end": m_10_2018}
tr_2 = {"start": m_12_2018, "end": m_08_2019}
tr_3 = {"start": m_10_2019, "end": m_08_2020}
tr_4 = {"start": m_10_2020, "end": m_10_2021}
tr_5 = {"start": m_12_2021, "end": m_06_2023}

reception_rounds = [
    tr_1,
    tr_2,
    tr_3,
    tr_4,
    tr_5,
]

# Hosts
hosts = [
    #  TR1
    {
        "reception_round": tr_1,
        "meetings": [
            {
                "meeting_date": m_02_2018,
                "members": [
                    john_smith,
                    tom_cruise,
                ],
            },
            {
                "meeting_date": m_04_2018,
                "members": [
                    julia_roberts,
                    avero,
                ],
            },
            {
                "meeting_date": m_06_2018,
                "members": [
                    angelina_jolie,
                    nyangono,
                ],
            },
            {
                "meeting_date": m_08_2018,
                "members": [
                    longue,
                    lady_ponce,
                ],
            },
            {
                "meeting_date": m_10_2018,
                "members": [
                    petit_pays,
                    manu_dibango,
                ],
            },
        ],
    },
    #  TR2
    {
        "reception_round": tr_2,
        "meetings": [
            {
                "meeting_date": m_12_2018,
                "members": [
                    john_smith,
                    julia_roberts,
                ],
            },
            {
                "meeting_date": m_02_2019,
                "members": [
                    angelina_jolie,
                    longue,
                ],
            },
            {
                "meeting_date": m_04_2019,
                "members": [
                    petit_pays,
                    tom_cruise,
                ],
            },
            {
                "meeting_date": m_06_2019,
                "members": [
                    avero,
                    nyangono,
                ],
            },
            {
                "meeting_date": m_08_2019,
                "members": [
                    lady_ponce,
                    manu_dibango,
                    malhox,
                ],
            },
        ],
    },
    #  TR3
    {
        "reception_round": tr_3,
        "meetings": [
            {
                "meeting_date": m_10_2019,
                "members": [john_smith],
            },
            {
                "meeting_date": m_12_2019,
                "members": [
                    julia_roberts,
                    angelina_jolie,
                ],
            },
            {
                "meeting_date": m_02_2020,
                "members": [
                    longue,
                    petit_pays,
                ],
            },
            {
                "meeting_date": m_04_2020,
                "members": [
                    tom_cruise,
                    avero,
                ],
            },
            {
                "meeting_date": m_06_2020,
                "members": [
                    nyangono,
                    lady_ponce,
                ],
            },
            {
                "meeting_date": m_08_2020,
                "members": [
                    manu_dibango,
                    malhox,
                ],
            },
        ],
    },
    #  TR4
    {
        "reception_round": tr_4,
        "meetings": [
            {
                "meeting_date": m_10_2020,
                "members": [
                    daphne,
                    kameni,
                    medecein_de_medelin,
                ],
            },
            {
                "meeting_date": m_12_2020,
                "members": [
                    petit_pays,
                    malhox,
                ],
            },
            {
                "meeting_date": m_02_2021,
                "members": [
                    manu_dibango,
                    lady_ponce,
                ],
            },
            {
                "meeting_date": m_04_2021,
                "members": [
                    nyangono,
                    avero,
                ],
            },
            {
                "meeting_date": m_06_2021,
                "members": [
                    tom_cruise,
                    petit_pays,
                ],
            },
            {
                "meeting_date": m_08_2021,
                "members": [
                    longue,
                    angelina_jolie,
                ],
            },
            {
                "meeting_date": m_10_2021,
                "members": [
                    julia_roberts,
                    john_smith,
                ],
            },
        ],
    },
    #  TR5
    {
        "reception_round": tr_5,
        "meetings": [
            {
                "meeting_date": m_12_2021,
                "members": [
                    takam,
                    mbatremy,
                ],
            },
            {
                "meeting_date": m_02_2022,
                "members": [
                    poupi,
                    mitoumba,
                ],
            },
            {
                "meeting_date": m_04_2022,
                "members": [
                    daphne,
                    murielle_blanche,
                ],
            },
            {
                "meeting_date": m_06_2022,
                "members": [
                    medecein_de_medelin,
                    kameni,
                ],
            },
            {
                "meeting_date": m_08_2022,
                "members": [
                    malhox,
                    petit_pays,
                ],
            },
            {
                "meeting_date": m_10_2022,
                "members": [
                    lady_ponce,
                    manu_dibango,
                ],
            },
            {
                "meeting_date": m_12_2022,
                "members": [
                    avero,
                    nyangono,
                ],
            },
            {
                "meeting_date": m_02_2023,
                "members": [
                    petit_pays,
                    tom_cruise,
                ],
            },
            {
                "meeting_date": m_04_2023,
                "members": [
                    angelina_jolie,
                    longue,
                ],
            },
            {
                "meeting_date": m_06_2023,
                "members": [
                    john_smith,
                    julia_roberts,
                ],
            },
        ],
    },
]

# TontineRound
tt_1 = {
    "start": m_04_2018,
    "end": m_10_2018,
    "buckets": 8,
    "amount_pb": 200,
    "jackpot": 800,
}
tt_2 = {
    "start": m_02_2020,
    "end": m_12_2020,
    "buckets": 12,
    "amount_pb": 150,
    "jackpot": 900,
}
tt_3 = {
    "start": m_10_2021,
    "end": m_04_2023,
    "buckets": 20,
    "amount_pb": 100,
    "jackpot": 1000,
}

tontine_rounds = [
    tt_1,
    tt_2,
    tt_3,
]

# TontineRecipient
tontine_recipients = [
    # Tontine Round 1
    {
        "tontine_round": tt_1,
        "meetings": [
            {
                "meeting": m_04_2018,
                "recipients": [
                    john_smith,
                    julia_roberts,
                ],
            },
            {
                "meeting": m_06_2018,
                "recipients": [
                    longue,
                    tom_cruise,
                ],
            },
            {
                "meeting": m_08_2018,
                "recipients": [
                    avero,
                    nyangono,
                ],
            },
            {
                "meeting": m_10_2018,
                "recipients": [
                    lady_ponce,
                    manu_dibango,
                ],
            },
        ],
    },
    # Tontine Round 2
    {
        "tontine_round": tt_2,
        "meetings": [
            {
                "meeting": m_02_2020,
                "recipients": [
                    avero,
                    longue,
                ],
            },
            {
                "meeting": m_04_2020,
                "recipients": [
                    julia_roberts,
                    lady_ponce,
                ],
            },
            {
                "meeting": m_06_2020,
                "recipients": [
                    petit_pays,
                    manu_dibango,
                ],
            },
            {
                "meeting": m_08_2020,
                "recipients": [
                    angelina_jolie,
                    tom_cruise,
                ],
            },
            {
                "meeting": m_10_2020,
                "recipients": [
                    nyangono,
                    john_smith,
                ],
            },
            {
                "meeting": m_12_2020,
                "recipients": [
                    malhox,
                    petit_bozard,
                ],
            },
        ],
    },
    # Tontine Round 3
    {
        "tontine_round": tt_3,
        "meetings": [
            {
                "meeting": m_10_2021,
                "recipients": [
                    longue,
                    john_smith,
                ],
            },
            {
                "meeting": m_12_2021,
                "recipients": [
                    julia_roberts,
                    angelina_jolie,
                ],
            },
            {
                "meeting": m_02_2022,
                "recipients": [
                    petit_pays,
                    tom_cruise,
                ],
            },
            {
                "meeting": m_04_2022,
                "recipients": [
                    avero,
                    nyangono,
                ],
            },
            {
                "meeting": m_06_2022,
                "recipients": [
                    lady_ponce,
                    manu_dibango,
                ],
            },
            {
                "meeting": m_08_2022,
                "recipients": [
                    malhox,
                    petit_bozard,
                ],
            },
            {
                "meeting": m_10_2022,
                "recipients": [
                    medecein_de_medelin,
                    kameni,
                ],
            },
            {
                "meeting": m_12_2022,
                "recipients": [
                    daphne,
                    murielle_blanche,
                ],
            },
            {
                "meeting": m_02_2023,
                "recipients": [
                    poupi,
                    mitoumba,
                ],
            },
            {
                "meeting": m_04_2023,
                "recipients": [
                    takam,
                    mbatremy,
                ],
            },
        ],
    },
]

# BoardPosition

board_positions = [
    "Président",
    "Vice-Pésident",
    "Secrétaire",
    "Censeur",
    "Censeur Adjoint",
    "Commissaire aux Comptes",
    "Trésorier",
    "Chargé de Projets",
    "Chargé de Communication",
]

# Board / BoardMember
board_1 = {"start": m_02_2018, "end": m_02_2020}
board_2 = {"start": m_04_2020, "end": m_04_2023}

boards = [
    {
        "board": board_1,
        "positions": [
            {"position": "Président", "member": julia_roberts},
            {"position": "Vice-Pésident", "member": petit_pays},
            {"position": "Secrétaire", "member": longue},
            {"position": "Censeur", "member": manu_dibango},
            {"position": "Commissaire aux Comptes", "member": john_smith},
            {"position": "Trésorier", "member": angelina_jolie},
        ],
    },
    {
        "board": board_2,
        "positions": [
            {"position": "Président", "member": petit_pays},
            {"position": "Vice-Pésident", "member": tom_cruise},
            {"position": "Secrétaire", "member": angelina_jolie},
            {"position": "Censeur", "member": avero},
            {"position": "Commissaire aux Comptes", "member": lady_ponce},
            {"position": "Trésorier", "member": julia_roberts},
            {"position": "Chargé de Projets", "member": john_smith},
        ],
    },
]

# AccountType
secours, epargne = "Secours", "Épargne"
epargne_scolaire, sanction = "Épargne Scolaire", "Sanction"
inscription, fond_roulement = "Inscription", "Fond de Roulement"
project = "Projet"

account_types = [
    secours,
    epargne,
    epargne_scolaire,
    sanction,
    inscription,
    fond_roulement,
    project,
]

# MemberTransaction
member_transactions = [
    # 2018
    {
        "meeting": m_02_2018,
        "transactions": [
            {
                "account": secours,
                "members": [
                    {"name": john_smith, "amount": 50},
                    {"name": julia_roberts, "amount": 50},
                    {"name": angelina_jolie, "amount": 50},
                    {"name": longue, "amount": 50},
                    {"name": petit_pays, "amount": 50},
                    {"name": tom_cruise, "amount": 50},
                    {"name": avero, "amount": 50},
                    {"name": nyangono, "amount": 50},
                    {"name": lady_ponce, "amount": 50},
                    {"name": manu_dibango, "amount": 50},
                ],
            }
        ],
    },
    {
        "meeting": m_04_2018,
        "transactions": [
            {
                "account": epargne,
                "members": [
                    {"name": petit_pays, "amount": 10},
                    {"name": julia_roberts, "amount": 5},
                ],
            }
        ],
    },
    {
        "meeting": m_06_2018,
        "transactions": [
            {
                "account": epargne_scolaire,
                "members": [
                    {"name": lady_ponce, "amount": 15},
                    {"name": angelina_jolie, "amount": 5},
                ],
            }
        ],
    },
    {
        "meeting": m_08_2018,
        "transactions": [
            {
                "account": epargne,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": petit_pays, "amount": 15},
                ],
            }
        ],
    },
    {
        "meeting": m_10_2018,
        "transactions": [
            {
                "account": epargne,
                "members": [
                    {"name": longue, "amount": 10},
                ],
            },
            {
                "account": epargne_scolaire,
                "members": [
                    {"name": manu_dibango, "amount": 10},
                    {"name": lady_ponce, "amount": 15},
                ],
            },
        ],
    },
    {
        "meeting": m_12_2018,
        "transactions": [
            {
                "account": epargne_scolaire,
                "members": [
                    {"name": julia_roberts, "amount": 25},
                    {"name": avero, "amount": 10},
                ],
            }
        ],
    },
    # 2019
    {
        "meeting": m_02_2019,
        "transactions": [
            {
                "account": epargne,
                "members": [
                    {"name": angelina_jolie, "amount": 30},
                    {"name": avero, "amount": 20},
                ],
            },
            {
                "account": epargne_scolaire,
                "members": [
                    {"name": angelina_jolie, "amount": 5},
                    {"name": petit_pays, "amount": 10},
                    {"name": longue, "amount": 10},
                ],
            },
            {
                "account": secours,
                "members": [
                    {"name": malhox, "amount": 25},
                ],
            },
        ],
    },
    {
        "meeting": m_04_2019,
        "transactions": [
            {
                "account": secours,
                "members": [
                    {"name": malhox, "amount": 25},
                ],
            },
            {
                "account": sanction,
                "members": [
                    {"name": john_smith, "amount": 1},
                    {"name": longue, "amount": 2},
                    {"name": lady_ponce, "amount": 2},
                ],
            },
        ],
    },
    {
        "meeting": m_06_2019,
        "transactions": [
            {
                "account": epargne,
                "members": [
                    {"name": malhox, "amount": 10},
                ],
            },
            {
                "account": epargne_scolaire,
                "members": [
                    {"name": malhox, "amount": 10},
                    {"name": avero, "amount": 10},
                    {"name": nyangono, "amount": 10},
                ],
            },
        ],
    },
    {
        "meeting": m_08_2019,
        "transactions": [
            {
                "account": sanction,
                "members": [
                    {"name": malhox, "amount": 1},
                    {"name": petit_pays, "amount": 2},
                    {"name": tom_cruise, "amount": 2},
                ],
            }
        ],
    },
    {
        "meeting": m_10_2019,
        "transactions": [],
    },
    {
        "meeting": m_12_2019,
        "transactions": [],
    },
    # 2020
    {
        "meeting": m_02_2020,
        "transactions": [
            {
                "account": secours,
                "members": [
                    {"name": petit_bozard, "amount": 30},
                    {"name": medecein_de_medelin, "amount": 40},
                ],
            },
            {
                "account": epargne_scolaire,
                "members": [
                    {"name": malhox, "amount": 20},
                    {"name": manu_dibango, "amount": 10},
                ],
            },
        ],
    },
    {
        "meeting": m_04_2020,
        "transactions": [
            {
                "account": sanction,
                "members": [
                    {"name": angelina_jolie, "amount": 5},
                    {"name": nyangono, "amount": 2},
                ],
            }
        ],
    },
    {
        "meeting": m_06_2020,
        "transactions": [
            {
                "account": secours,
                "members": [
                    {"name": petit_bozard, "amount": 20},
                    {"name": medecein_de_medelin, "amount": 10},
                    {"name": kameni, "amount": 50},
                    {"name": daphne, "amount": 50},
                ],
            },
        ],
    },
    {
        "meeting": m_08_2020,
        "transactions": [
            {
                "account": epargne,
                "members": [
                    {"name": john_smith, "amount": 10},
                    {"name": angelina_jolie, "amount": 5},
                ],
            }
        ],
    },
    {
        "meeting": m_10_2020,
        "transactions": [],
    },
    {
        "meeting": m_12_2020,
        "transactions": [],
    },
    # 2021
    {
        "meeting": m_02_2021,
        "transactions": [
            {
                "account": secours,
                "members": [
                    {"name": murielle_blanche, "amount": 50},
                    {"name": poupi, "amount": 50},
                ],
            },
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                ],
            },
        ],
    },
    {
        "meeting": m_04_2021,
        "transactions": [
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                ],
            },
        ],
    },
    {
        "meeting": m_06_2021,
        "transactions": [
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                ],
            },
        ],
    },
    {
        "meeting": m_08_2021,
        "transactions": [
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                ],
            },
        ],
    },
    {
        "meeting": m_10_2021,
        "transactions": [
            {
                "account": secours,
                "members": [
                    {"name": mitoumba, "amount": 50},
                    {"name": takam, "amount": 50},
                    {"name": mbatremy, "amount": 50},
                ],
            },
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                ],
            },
        ],
    },
    {
        "meeting": m_12_2021,
        "transactions": [
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                    {"name": mitoumba, "amount": 5},
                    {"name": takam, "amount": 5},
                    {"name": mbatremy, "amount": 5},
                ],
            },
        ],
    },
    # 2022
    {
        "meeting": m_02_2022,
        "transactions": [
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                    {"name": mitoumba, "amount": 5},
                    {"name": takam, "amount": 5},
                    {"name": mbatremy, "amount": 5},
                ],
            },
        ],
    },
    {
        "meeting": m_04_2022,
        "transactions": [
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                    {"name": mitoumba, "amount": 5},
                    {"name": takam, "amount": 5},
                    {"name": mbatremy, "amount": 5},
                ],
            },
        ],
    },
    {
        "meeting": m_06_2022,
        "transactions": [
            {
                "account": project,
                "members": [
                    {"name": john_smith, "amount": 5},
                    {"name": julia_roberts, "amount": 5},
                    {"name": angelina_jolie, "amount": 5},
                    {"name": longue, "amount": 5},
                    {"name": petit_pays, "amount": 5},
                    {"name": tom_cruise, "amount": 5},
                    {"name": avero, "amount": 5},
                    {"name": nyangono, "amount": 5},
                    {"name": lady_ponce, "amount": 5},
                    {"name": manu_dibango, "amount": 5},
                    {"name": malhox, "amount": 5},
                    {"name": petit_bozard, "amount": 5},
                    {"name": medecein_de_medelin, "amount": 5},
                    {"name": kameni, "amount": 5},
                    {"name": daphne, "amount": 5},
                    {"name": murielle_blanche, "amount": 5},
                    {"name": poupi, "amount": 5},
                    {"name": mitoumba, "amount": 5},
                    {"name": takam, "amount": 5},
                    {"name": mbatremy, "amount": 5},
                ],
            },
        ],
    },
]

# OrgTransaction
org_transactions = [
    # 2018
    {
        "meeting": m_02_2018,
        "balances": [
            {"account": secours, "amount": 500},
        ],
    },
    {
        "meeting": m_04_2018,
        "balances": [
            {"account": epargne, "amount": 15},
        ],
    },
    {
        "meeting": m_06_2018,
        "balances": [
            {"account": epargne, "amount": 20},
        ],
    },
    {
        "meeting": m_08_2018,
        "balances": [
            {"account": epargne, "amount": 20},
        ],
    },
    {
        "meeting": m_10_2018,
        "balances": [
            {"account": epargne, "amount": 10},
        ],
    },
    {
        "meeting": m_12_2018,
        "balances": [
            {"account": epargne_scolaire, "amount": 35},
        ],
    },
    # 2019
    {
        "meeting": m_02_2019,
        "balances": [
            {"account": epargne, "amount": 50},
            {"account": epargne_scolaire, "amount": 25},
            {"account": secours, "amount": 25},
        ],
    },
    {
        "meeting": m_04_2019,
        "balances": [
            {"account": secours, "amount": 25},
            {"account": sanction, "amount": 5},
        ],
    },
    {
        "meeting": m_06_2019,
        "balances": [
            {"account": epargne, "amount": 10},
            {"account": epargne_scolaire, "amount": 30},
        ],
    },
    {
        "meeting": m_08_2019,
        "balances": [
            {"account": sanction, "amount": 5},
        ],
    },
    {
        "meeting": m_10_2019,
        "balances": [],
    },
    {
        "meeting": m_12_2019,
        "balances": [],
    },
    # 2020
    {
        "meeting": m_02_2020,
        "balances": [
            {"account": secours, "amount": 70},
            {"account": epargne_scolaire, "amount": 30},
        ],
    },
    {
        "meeting": m_04_2020,
        "balances": [
            {"account": sanction, "amount": 7},
        ],
    },
    {
        "meeting": m_06_2020,
        "balances": [
            {"account": secours, "amount": 130},
        ],
    },
    {
        "meeting": m_08_2020,
        "balances": [
            {"account": epargne, "amount": 15},
        ],
    },
    {
        "meeting": m_10_2020,
        "balances": [],
    },
    {
        "meeting": m_12_2020,
        "balances": [],
    },
    # 2021
    {
        "meeting": m_02_2021,
        "balances": [
            {"account": secours, "amount": 100},
            {"account": project, "amount": 75},
        ],
    },
    {
        "meeting": m_04_2021,
        "balances": [
            {"account": project, "amount": 85},
        ],
    },
    {
        "meeting": m_06_2021,
        "balances": [
            {"account": project, "amount": 85},
        ],
    },
    {
        "meeting": m_08_2021,
        "balances": [
            {"account": project, "amount": 85},
        ],
    },
    {
        "meeting": m_10_2021,
        "balances": [
            {"account": secours, "amount": 150},
            {"account": project, "amount": 85},
        ],
    },
    {
        "meeting": m_12_2021,
        "balances": [
            {"account": project, "amount": 100},
        ],
    },
    # 2022
    {
        "meeting": m_02_2022,
        "balances": [
            {"account": project, "amount": 100},
        ],
    },
    {
        "meeting": m_04_2022,
        "balances": [
            {"account": project, "amount": 100},
        ],
    },
    {
        "meeting": m_06_2022,
        "balances": [
            {"account": project, "amount": 100},
        ],
    },
]


# DocumentType
statutes = "Statuts"
internal_rules = "Règlement Intérieur"

document_types = [statutes, internal_rules]

# DocumentChapter / DocumentArticle
chapters = [
    {
        "document": "",
        "chapters": [
            {"title": "", "articles": []},
            {"title": "", "articles": []},
        ],
    },
]

# DocumentArticle
