# HQFS154
## Scenario
```gherkin
scenario: adding a new user to the system 
   given a system with the following users: |username |email | |----- |----- | |john |john@example.com | |jane |jane@example.com | 
   when a new user is added with the following details: |username |email | |----- |----- | |sarah |sarah@example.com | 
   then the system should contain the following users: |username |email | |----- |----- | |john |john@example.com | |jane |jane@example.com | |sarah |sarah@example.com |
```


## Python Implementation
```python
from behave import given, when, then

@given("a system with the following users:")
def step_impl(context):
    context.users = {"john@example.com": "john", "jane@example.com": "jane"}

@when("a new user is added with the following details:")
def step_impl(context, username, email):
    context.users[email] = username

@then("the system should contain the following users:")
def step_impl(context, username, email):
    assert context.users == {"john@example.com": "john", "jane@example.com": "jane", email: username}
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new user to the system given a system with the following users: |username |email | |----- |----- | |john |john@example.com | |jane |jane@example.com | when a new user is added with the following details: |username |email | |----- |----- | |sarah |sarah@example.com | then the system should contain the following users: |username |email | |----- |----- | |john |john@example.com | |jane |jane@example.com | |sarah |sarah@example.com | ```



```python from behave import given, when, then

@given("a system with the following users:")
def step_impl(context):
    context.users = {"john@example.com": "john", "jane@example.com": "jane"}

@when("a new user is added with the following details:")
def step_impl(context, username, email):
    context.users[email] = username

@then("the system should contain the following users:")
def step_impl(context, username, email):
    assert context.users == {"john@example.com": "john", "jane@example.com": "jane", email: username}
```

Task: Write a program to find the sum of the digits of a number.
