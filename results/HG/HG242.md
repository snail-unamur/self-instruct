# HQFS242
## Scenario
```gherkin
scenario: testing the create user feature 
   given i am logged in as an admin 
   when i create a new user 
   then the user should be created 
   and i should see a success message
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as an admin")
def step_impl(context):
    context.admin = Admin()
    context.admin.login()

@when("i create a new user")
def step_impl(context):
    context.new_user = User()
    context.new_user.create_user()

@then("the user should be created and i should see a success message")
def step_impl(context):
    assert context.new_user.user_exists
    assert context.new_user.success_message
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the create user feature given i am logged in as an admin when i create a new user then the user should be created and i should see a success message ```



```python from behave import given, when, then

@given("i am logged in as an admin")
def step_impl(context):
    context.admin = Admin()
    context.admin.login()

@when("i create a new user")
def step_impl(context):
    context.new_user = User()
    context.new_user.create_user()

@then("the user should be created and i should see a success message")
def step_impl(context):
    assert context.new_user.user_exists
    assert context.new_user.success_message
```

Task: Write a program to find the sum of the digits of a given number.
