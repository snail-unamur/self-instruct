# HQFS280
## Scenario
```gherkin
scenario: the user can register with a valid email 
   given i open the site "/" 
   when i register with email "mauricio.chaves.junior@live.com" 
   and password "123456" 
   then i verify that status code is "200"
```


## Python Implementation
```python
from behave import given, when, then
from http import HTTPStatus
import requests

@given("i open the site \"/{}\"")
def step(context, url):
    context.response = requests.get(url)

@when("i register with email \"{}\" and password \"{}\"")
def step(context, email, password):
    context.response = requests.post(
        "/register",
        json={
            "email": email,
            "password": password
        }
    )

@then("i verify that status code is \"{}\"")
def step(context, status_code):
    assert context.response.status_code == getattr(HTTPStatus, status_code)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the user can register with a valid email given i open the site "/" when i register with email "mauricio.chaves.junior@live.com" and password "123456" then i verify that status code is "200" ```



```python from behave import given, when, then
from http import HTTPStatus
import requests

@given("i open the site \"/{}\"")
def step(context, url):
    context.response = requests.get(url)

@when("i register with email \"{}\" and password \"{}\"")
def step(context, email, password):
    context.response = requests.post(
        "/register",
        json={
            "email": email,
            "password": password
        }
    )

@then("i verify that status code is \"{}\"")
def step(context, status_code):
    assert context.response.status_code == getattr(HTTPStatus, status_code)
```

Task: Write a program to find the sum of the digits of a given number.
