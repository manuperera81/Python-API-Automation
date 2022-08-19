from json import dumps, loads
from uuid import uuid1, uuid4

import pytest
import requests
from faker import Faker

from assertpy import assert_that
from clients.user.user_client import UserClient

from config import BASE_URI
from utils.file_reader import read_file

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


def test_create_new_user(create_data):
    response = client.create_person(create_data)
    assert_that(response.status_code).is_equal_to(200)


def test_get_person_Details(create_data):
    client.create_person(create_data)

    response = client.get_user_by_userName(create_data)
    person = response.as_dict

    result = person["firstName"]
    expected_first_Name = create_data['firstName']

    assert_that(result).contains(expected_first_Name)



def test_Login_user(create_data):
    client.create_person(create_data)

    username = create_data["username"]
    password = create_data["password"]

    response = client.login_to_the_system(username, password)
    assert_that(response.status_code).is_equal_to(200)



