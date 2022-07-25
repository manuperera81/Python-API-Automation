from json import dumps
from uuid import uuid4, uuid1

import requests
from assertpy import assert_that

from config import BASE_URI


def test_create_new_user():
    response = create_new_unique_user()
    assert_that(response[0].status_code).is_equal_to(200)

def test_Lgoin_user():
    new_user = create_new_unique_user()
    username = new_user[1]
    password = new_user[2]

    print(username)
    print(password)
    response = login_to_the_system(username,password)
    assert_that(response.status_code).is_equal_to(200)





def login_to_the_system(userName,password):
    parameters = dumps({
        "username": userName ,
        "password": password
    })

    headers = {
        'Accept': 'application/json',
        'Connection': 'keep-alive'
    }
    login_response = requests.get(url=f'{BASE_URI}/user/login', params=parameters, headers=headers)
    return login_response


def create_new_unique_user():
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
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    create_user_response = requests.post(url=f'{BASE_URI}/user', data=payload, headers=headers)
    return create_user_response, unique_userName,password
