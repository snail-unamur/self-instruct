# MQFS197
## Scenario
```gherkin
scenario: testing the user account update feature 
   given i am logged in as a user 
   when i update my account information 
   then my account information should be updated 
   when i leave some fields blank 
   then the corresponding fields should not be updated
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User("testuser", "testpassword")
    context.user.login()

@when("i update my account information")
def step_impl(context):
    context.user.update_account_info(first_name="New", last_name="Name")

@then("my account information should be updated")
def step_impl(context):
    updated_user = User.get_user(context.user.username)
    assert updated_user.first_name == "New"
    assert updated_user.last_name == "Name"

@when("i leave some fields blank")
def step_impl(context):
    context.user.update_account_info(first_name="New", last_name="")

@then("the corresponding fields should not be updated")
def step_impl(context):
    updated_user = User.get_user(context.user.username)
    assert updated_user.first_name == "New"
    assert updated_user.last_name == "Old"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the user account update feature given i am logged in as a user when i update my account information then my account information should be updated when i leave some fields blank then the corresponding fields should not be updated ```



```python from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User("testuser", "testpassword")
    context.user.login()

@when("i update my account information")
def step_impl(context):
    context.user.update_account_info(first_name="New", last_name="Name")

@then("my account information should be updated")
def step_impl(context):
    updated_user = User.get_user(context.user.username)
    assert updated_user.first_name == "New"
    assert updated_user.last_name == "Name"

@when("i leave some fields blank")
def step_impl(context):
    context.user.update_account_info(first_name="New", last_name="")

@then("the corresponding fields should not be updated")
def step_impl(context):
    updated_user = User.get_user(context.user.username)
    assert updated_user.first_name == "New"
    assert updated_user.last_name == "Old"
```

Task: Write a program to find the sum of the digits of a given number.
