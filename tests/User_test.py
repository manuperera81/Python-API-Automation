from assertpy import assert_that

from clients.user.user_client import UserClient

client = UserClient()


def test_create_new_user(create_data,rp_logger):
    """
    Test the User API and create the new user with JSON template
    """
    response = client.create_person(create_data)
    rp_logger.info("User successfully created")
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
