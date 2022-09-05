#Python-API-Automation-Framework

This is full Automation Framwork for  API testing with Python. This includes
* Makeing  HTTP Request
* Assertions
* XML/JSON payload request
* Schema Validation
* Reporting and Parallel Testing

This entinre framework used on [Petstore API Collection](https://petstore.swagger.io/#/user/updateUser). 

This is build on custom Python environment. Please refer [here](https://pipenv.pypa.io/en/latest/install/) for setup custome python envoironment 

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
