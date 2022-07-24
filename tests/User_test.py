from json import dumps
from uuid import uuid4

import requests
from assertpy import assert_that

from config import BASE_URI


def test_create_new_user():
    unique_userName = f'User {str(uuid4())}'
    # make dict to json
    payload = dumps({
        "id": 1001,
        "username": unique_userName,
        "firstName": "FirstName",
        "lastName": "LastName",
        "email": "123@gmail.com",
        "password": "123@com",
        "phone": "1234567899",
        "userStatus": 1001
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url=f'{BASE_URI}/user', data=payload, headers=headers)
    print(response.status_code)
    assert_that(response.status_code).is_equal_to(200)
