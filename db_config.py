import json
from faker import Faker

fake = Faker()

sample_entities = {
    "color": [
        {"id": 1, "color": fake.color()},
        {"id": 2, "color": fake.color()},
        {"id": 3, "color": fake.color()},
    ],
    "person": [
        {"id": 1, "name": fake.name(), "phone_number": fake.phone_number()},
        {"id": 2, "name": fake.name(), "phone_number": fake.phone_number()},
        {"id": 3, "name": fake.name(), "phone_number": fake.phone_number()},

    ],
    "product": [
        {"id": 1, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
        {"id": 2, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
        {"id": 3, "name": fake.word(), "price": fake.random_number(3), "category": fake.word()},
    ],
    "city": [
        {"id": 1, "address": fake.address()},
        {"id": 2, "address": fake.address()},
        {"id": 3, "address": fake.address()},
    ],
    "shop": [
        {"id": 1, "name": fake.company(), "contact_person": fake.name()},
        {"id": 2, "name": fake.company(), "contact_person": fake.name()},
        {"id": 3, "name": fake.company(), "contact_person": fake.name()},
    ],
}

with open('db.json', 'w') as json_file:
    json.dump(sample_entities, json_file, indent=2)