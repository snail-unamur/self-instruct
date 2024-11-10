# HQFS66
## Scenario
```gherkin
scenario: user password reset confirmation 
   given i am a user 
   and i have requested a password reset 
   and i have clicked the password reset link 
   then i should be able to enter a new password
```


## Python Implementation
```python
from behave import given, when, then

@given("i am a user")
def step_given_i_am_a_user(context):
    pass

@given("i have requested a password reset")
def step_given_i_have_requested_a_password_reset(context):
    pass

@when("i have clicked the password reset link")
def step_when_i_have_clicked_the_password_reset_link(context):
    pass

@then("i should be able to enter a new password")
def step_then_i_should_be_able_to_enter_a_new_password(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user password reset confirmation given i am a user and i have requested a password reset and i have clicked the password reset link then i should be able to enter a new password ```



```python from behave import given, when, then

@given("i am a user")
def step_given_i_am_a_user(context):
    pass

@given("i have requested a password reset")
def step_given_i_have_requested_a_password_reset(context):
    pass

@when("i have clicked the password reset link")
def step_when_i_have_clicked_the_password_reset_link(context):
    pass

@then("i should be able to enter a new password")
def step_then_i_should_be_able_to_enter_a_new_password(context):
    pass
```

Task: Write a program to print the first 100 prime numbers.
