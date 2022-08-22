from uuid import uuid1, uuid4

import pytest
from assertpy import assert_that
from cerberus import Validator
from faker import Faker

from clients.user.user_client import UserClient
from utils.file_reader import read_file

schema = {
    "id": {'type': 'number'},
    "username": {'type': 'string'},
    "firstName": {'type': 'string'},
    "lastName": {'type': 'string'},
    "email": {'type': 'string'},
    "password": {'type': 'string'},
    "phone": {'type': 'string'},
    "userStatus": {'type': 'number'}
}

client = UserClient()


@pytest.fixture
def create_data():
    payload = read_file("create_person.json")

    fake = Faker()

    custom_payload = {
        "id": int(str(uuid1().node)[:5]),
        "username": f'{fake.first_name()} {str(uuid4())}',
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": int(str(uuid1().node)[:5])
    }

    for key in custom_payload:
        payload[key] = custom_payload[key]

    yield payload


def test_person_get_by_name_has_expected_schema(create_data):
    client.create_person(create_data)

    response = client.get_user_by_userName(create_data)
    person = response.as_dict

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(person)

    assert_that(is_valid, description=validator.errors).is_true()


