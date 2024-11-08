# HQFS72
## Scenario
```gherkin
scenario: get all users - get with token 
   given i prepare environment for tests run 
   when i get all users 
   then i verify that status code is "200" 
   and i verify that response contains at least one user
```


## Python Implementation
```python
from behave import given, when, then
import requests

@given("i prepare environment for tests")
def step_impl(context):
    context.base_url = "http://localhost:8000"
    context.headers = {"Content-Type": "application/json"}

@when("i get all users")
def step_impl(context):
    context.response = requests.get(
        f"{context.base_url}/api/users/", headers=context.headers
    )

@then("i verify that status code is '200'")
def step_impl(context):
    assert context.response.status_code == 200

@then("i verify that response contains at least one user")
def step_impl(context):
    assert len(context.response.json()) > 0
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: get all users - get with token given i prepare environment for tests run when i get all users then i verify that status code is "200" and i verify that response contains at least one user ```



```python from behave import given, when, then
import requests

@given("i prepare environment for tests")
def step_impl(context):
    context.base_url = "http://localhost:8000"
    context.headers = {"Content-Type": "application/json"}

@when("i get all users")
def step_impl(context):
    context.response = requests.get(
        f"{context.base_url}/api/users/", headers=context.headers
    )

@then("i verify that status code is '200'")
def step_impl(context):
    assert context.response.status_code == 200

@then("i verify that response contains at least one user")
def step_impl(context):
    assert len(context.response.json()) > 0
```

Task: Write a program to find the sum of the digits of a given number.
