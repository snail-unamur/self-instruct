# HQFS182
## Scenario
```gherkin
scenario: testing the account verification feature 
   given i am not verified 
   when i sign up 
   then i should be sent a verification email 
   and i should be able to verify my account
```


## Python Implementation
```python
from behave import given, when, then

@given("i am not verified")
def step_given_i_am_not_verified(context):
    context.user = User()
    context.user.is_verified = False

@when("i sign up")
def step_when_i_sign_up(context):
    context.user.sign_up()

@then("i should be sent a verification email")
def step_then_i_should_be_sent_a_verification_email(context):
    assert context.user.email_sent

@then("i should be able to verify my account")
def step_then_i_should_be_able_to_verify_my_account(context):
    context.user.verify_account()
    assert context.user.is_verified
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the account verification feature given i am not verified when i sign up then i should be sent a verification email and i should be able to verify my account ```



```python from behave import given, when, then

@given("i am not verified")
def step_given_i_am_not_verified(context):
    context.user = User()
    context.user.is_verified = False

@when("i sign up")
def step_when_i_sign_up(context):
    context.user.sign_up()

@then("i should be sent a verification email")
def step_then_i_should_be_sent_a_verification_email(context):
    assert context.user.email_sent

@then("i should be able to verify my account")
def step_then_i_should_be_able_to_verify_my_account(context):
    context.user.verify_account()
    assert context.user.is_verified
```

Task: Write a program to find the sum of the digits of a number.
