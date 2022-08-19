from json import dumps, loads
from uuid import uuid4, uuid1

from clients.base_client import BaseClient
from config import BASE_URI
from utils.request import APIRequest


class UserClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_person(self, body):
        response = self._create_new_unique_user(body)
        return response

    def _create_new_unique_user(self, body):
        if body is None:
            unique_userName = f'User {str(uuid4())}'
            password = "123@com"
            unique_id = uuid1()

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

        create_user_response = self.request.post(url=f'{BASE_URI}/user', payload=payload, headers=self.headers)
        return create_user_response

    def get_user_by_userName(self, userdataPayload):
        userPayload = dumps(userdataPayload)
        resp = loads(userPayload)
        userName = resp['username']

        userDetail_response = self.request.get(url=f'{BASE_URI}/user/{userName}', headers=self.headers)

        return userDetail_response

    def login_to_the_system(self, userName, password):
        parameters = dumps({
            "username": userName,
            "password": password
        })

        login_response = self.request.get_with_parameters(url=f'{BASE_URI}/user/login', parameters=parameters,
                                                          headers=self.headers)
        return login_response




