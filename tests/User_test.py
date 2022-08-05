import json
from json import dumps, loads
from uuid import uuid4, uuid1

import pytest
import requests
from faker import Faker
from jsonpath_ng import parse
from assertpy import assert_that

from config import BASE_URI
from utils.file_reader import read_file


def test_create_new_user():
    response = create_new_unique_user(None)
    assert_that(response[0].status_code).is_equal_to(200)


def test_Login_user():
    new_user = create_new_unique_user()
    username = new_user[1]
    password = new_user[2]

    print(username)
    print(password)
    response = login_to_the_system(username, password)
    assert_that(response.status_code).is_equal_to(200)


def test_Logout_current_user():
    headers = {
        'Accept': "application/json",
        'Connection': "keep-alive"
    }
    Logout_response = requests.get(url=f'{BASE_URI}/user/logout', headers=headers)


def test_get_user_details():
    username = 'Christopher 883d1e02-7715-4180-8614-975c84b46551'

    headers = {
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'Accept-Encoding':'gzip, deflate, br'
    }

    userDetail_response = requests.get(url=f'{BASE_URI}/user/{username}', headers=headers)
    print(userDetail_response.text)



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


def test_person_added_with_json_Template(create_data):
    create_new_unique_user(create_data)

    response = get_user_by_userName(create_data)
    person = loads(response.text)

    result = person['firstName']
    expected_first_Name = create_data['firstName']

    assert_that(result).contains(expected_first_Name)

def get_user_by_userName(userdataPayload):
    userPayload = dumps(userdataPayload)
    resp = loads(userPayload)
    userName = resp['username']

    headers = {
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }
    userDetail_response = requests.get(url=f'{BASE_URI}/user/{userName}', headers=headers)

    return userDetail_response

def login_to_the_system(userName, password):
    parameters = dumps({
        "username": userName,
        "password": password
    })

    headers = {
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }
    login_response = requests.get(url=f'{BASE_URI}/user/login', params=parameters, headers=headers)
    return login_response



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
