# HQFS106
## Scenario
```gherkin
scenario: user profile update 
   given a user with an existing account 
   when the user updates their profile information 
   then the updated information should be saved 
   and displayed correctly
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with an existing account")
def step_impl(context):
    context.user = User()
    context.user.register()

@when("the user updates their profile information")
def step_impl(context):
    context.user.update_profile(new_email="newemail@example.com", new_phone="1234567890")

@then("the updated information should be saved and displayed correctly")
def step_impl(context):
    user = User.get_by_id(context.user.id)
    assert user.email == "newemail@example.com"
    assert user.phone == "1234567890"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user profile update given a user with an existing account when the user updates their profile information then the updated information should be saved and displayed correctly ```



```python from behave import given, when, then

@given("a user with an existing account")
def step_impl(context):
    context.user = User()
    context.user.register()

@when("the user updates their profile information")
def step_impl(context):
    context.user.update_profile(new_email="newemail@example.com", new_phone="1234567890")

@then("the updated information should be saved and displayed correctly")
def step_impl(context):
    user = User.get_by_id(context.user.id)
    assert user.email == "newemail@example.com"
    assert user.phone == "1234567890"
```

Task: Write a program to find the sum of the digits of a given number.
