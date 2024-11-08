# MQFS144
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the user creation functionality given i am logged in when i create a new user "jane doe" with the following data: | first name | last name | email | password | | "jane" | "doe" | "janedoe

@example.com" | "password123" | then a new user "jane doe" should be created with the following data: | first name | last name | email | | "jane" | "doe" | "janedoe@example.com" |

from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User("jane", "doe", "janedoe@example.com", "password123")

@when("i create a new user {first_name} {last_name} with the following data:")
def step_impl(context, first_name, last_name):
    context.new_user = User(first_name, last_name, "janedoe@example.com", "password123")

@then("a new user {first_name} {last_name} should be created with the following data:")
def step_impl(context, first_name, last_name):
    assert context.new_user.first_name == "jane"
    assert context.new_user.last_name == "doe"
    assert context.new_user.email == "janedoe@example.com"

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


Task: Write a program to find the sum of the digits of a number.
