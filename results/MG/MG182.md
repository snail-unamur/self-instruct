# MQFS182
## Scenario
```gherkin
scenario: user can view other users profiles 
   given i am logged in 
   when i click on the profile button for another user 
   then i should be able to view their profile 
   and i should not be able to edit their profile 
   and i should not be able to delete their account
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("i click on the profile button for another user")
def step_impl(context):
    context.other_user = User("otheruser")
    context.response = context.user.visit_profile(context.other_user)

@then("i should be able to view their profile")
def step_impl(context):
    assert context.response.status_code == 200

@then("i should not be able to edit their profile")
def step_impl(context):
    assert context.response.status_code != 200

@then("i should not be able to delete their account")
def step_impl(context):
    assert context.response.status_code != 200
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view other users profiles given i am logged in when i click on the profile button for another user then i should be able to view their profile and i should not be able to edit their profile and i should not be able to delete their account ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("i click on the profile button for another user")
def step_impl(context):
    context.other_user = User("otheruser")
    context.response = context.user.visit_profile(context.other_user)

@then("i should be able to view their profile")
def step_impl(context):
    assert context.response.status_code == 200

@then("i should not be able to edit their profile")
def step_impl(context):
    assert context.response.status_code != 200

@then("i should not be able to delete their account")
def step_impl(context):
    assert context.response.status_code != 200
```

Task: Write a program to find the sum of the digits of a given number.
