import json
from uuid import uuid1, uuid4
from json import dumps, loads

import pytest
import requests
from assertpy import assert_that
from cerberus import Validator
from faker import Faker

from config import BASE_URI
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
    create_new_unique_user(create_data)

    response = get_user_by_userName(create_data)
    person = loads(response.text)

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(person)

    assert_that(is_valid, description=validator.errors).is_true()


def get_user_by_userName(userdataPayload):
    userPayload = json.dumps(userdataPayload)
    resp = loads(userPayload)
    userName = resp['username']

    headers = {
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }
    userDetail_response = requests.get(url=f'{BASE_URI}/user/{userName}', headers=headers)

    return userDetail_response


def create_new_unique_user(body):
    if body is None:
        unique_userName = f'User {str(uuid4())}'
        password = "123@com"
        unique_id = uuid1()
        # make dict to json
        payload = dumps({
            "id": unique_id.node,
            "username": unique_userName,
            "firstName": "FirstName",
            "lastName": "LastName",
            "email": "123@gmail.com",
            "password": password,
            "phone": "1234567899",
            "userStatus": 1001
        })
    else:
        payload = dumps(body)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    create_user_response = requests.post(url=f'{BASE_URI}/user', data=payload, headers=headers)
    return create_user_response,
