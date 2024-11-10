# HQFS232
## Scenario
```gherkin
scenario: user account activation 
   given a user is registered on the platform 
   when the user's account is activated 
   then the user should be able to log in 
   and their account should be marked as active
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is registered on the platform")
def step_given_a_user_is_registered_on_the_platform(context):
    context.user = User()
    context.user.register()

@when("the user's account is activated")
def step_when_the_user_s_account_is_activated(context):
    context.user.activate()

@then("the user should be able to log in and their account should be marked as active")
def step_then_the_user_should_be_able_to_log_in_and_their_account_should_be_marked_as_active(context):
    assert context.user.is_active
    assert context.user.login()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user account activation given a user is registered on the platform when the user's account is activated then the user should be able to log in and their account should be marked as active ```



```python from behave import given, when, then

@given("a user is registered on the platform")
def step_given_a_user_is_registered_on_the_platform(context):
    context.user = User()
    context.user.register()

@when("the user's account is activated")
def step_when_the_user_s_account_is_activated(context):
    context.user.activate()

@then("the user should be able to log in and their account should be marked as active")
def step_then_the_user_should_be_able_to_log_in_and_their_account_should_be_marked_as_active(context):
    assert context.user.is_active
    assert context.user.login()
```

Task: Write a program to find the sum of the digits of a number.
