import logging
from uuid import uuid1, uuid4

import pytest
import reportportal_client
from faker import Faker
from reportportal_client import RPLogHandler, RPLogger

from utils.file_reader import read_file


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



@pytest.fixture(scope='session')
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.fixture(autouse=True)
def skip_by_mark(request):
    if request.node.get_closest_marker('fixture_skip'):
        pytest.skip('skip by fixture')


@pytest.fixture(scope='session')
def rp_launch_id(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.launch_id


@pytest.fixture(scope='session')
def rp_endpoint(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.endpoint


@pytest.fixture(scope='session')
def rp_project(request):
    if hasattr(request.config, "py_test_service"):
        return request.config.py_test_service.rp.project


@pytest.fixture(scope='function')
def rp_thread_logger(request):
    logger = logging.getLogger("test." + request.node.name)
    handler = RPLogHandler(
        level=logging.DEBUG,
        filter_client_logs=True,
        endpoint=request.config._reporter_config.rp_endpoint,
        ignored_record_names=('reportportal_client',
                              'pytest_reportportal'),
        rp_client=reportportal_client.current())
    logger.addHandler(handler)
    return logger