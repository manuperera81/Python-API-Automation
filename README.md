# Python-API-Automation-Framework

This is a full Automation Framework for  API testing with Python. This includes
* Making  HTTP Request
* Assertions
* XML/JSON payload request
* Schema Validation
* Reporting and Parallel Testing

This framework is used on [Petstore API Collection](https://petstore.swagger.io/#/user/updateUser). 

This is built on a custom Python environment. Please refer [here](https://pipenv.pypa.io/en/latest/install/) for setup custom python environment 

```python
# To Activate virtualenv
pipenv shell

# Install all dependencies in your virtualenv
pipenv install
```
### Run the tests

```python
# Setup report portal on docker
# Update rp_uuid in pytest.ini with project token
docker-compose -f docker-compose.yml -p reportportal up -d

# Launch pipenv
pipenv shell

# Install all packages
pipenv install

# Run tests via pytest (single threaded)
python -m pytest

# Run tests in parallel
python -m pytest -n auto
```
#### Acknowledgement 

Thanks for  [Test automation university](https://testautomationu.applitools.com/python-api-testing/) for the in-depth knowledge and context of API automation and  you can find the Course Code in [here](https://github.com/automationhacks/course-api-framework-python)
