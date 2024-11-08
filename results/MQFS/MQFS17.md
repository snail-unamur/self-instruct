# MQFS17
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: manage user account information given user "testuser" with account information "testuser@example.com" when i update account information for user "testuser" to "newuser@example.com" then user "testuser" has account information "newuser

@example.com"

from behave import given, when, then

@given("user {user} with account information {email}")
def step_given_user_with_account_information(context, user, email):
    context.user = user
    context.email = email

@when("i update account information for user {user} to {new_email}")
def step_when_i_update_account_information(context, user, new_email):
    context.new_email = new_email

@then("user {user} has account information {new_email}")
def step_then_user_has_account_information(context, user, new_email):
    assert context.email == new_email

Task: Write a program to find the sum of the digits of a given number.
