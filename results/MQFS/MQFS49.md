# MQFS49
## Scenario
```gherkin
scenario: testing the two-factor authentication functionality 
   given i am logged in 
   when i enable two-factor authentication 
   then i should be prompted to enter a verification code 
   and i should be able to log in using the verification code
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("i enable two-factor authentication")
def step_impl(context):
    context.user.enable_two_factor_auth()

@then("i should be prompted to enter a verification code")
def step_impl(context):
    assert context.user.is_prompted_for_verification_code

@then("i should be able to log in using the verification code")
def step_impl(context):
    context.user.login_with_verification_code("123456")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the two-factor authentication functionality given i am logged in when i enable two-factor authentication then i should be prompted to enter a verification code and i should be able to log in using the verification code ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("i enable two-factor authentication")
def step_impl(context):
    context.user.enable_two_factor_auth()

@then("i should be prompted to enter a verification code")
def step_impl(context):
    assert context.user.is_prompted_for_verification_code

@then("i should be able to log in using the verification code")
def step_impl(context):
    context.user.login_with_verification_code("123456")
```

Task: Write a program to find the sum of the digits of a given number.
