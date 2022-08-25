from assertpy import assert_that
from cerberus import Validator

from clients.user.user_client import UserClient

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


def test_person_get_by_name_has_expected_schema(create_data):
    client.create_person(create_data)

    response = client.get_user_by_userName(create_data)
    person = response.as_dict

    validator = Validator(schema, require_all=True)
    is_valid = validator.validate(person)

    assert_that(is_valid, description=validator.errors).is_true()
