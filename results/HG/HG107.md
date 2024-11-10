# HQFS107
## Scenario
```gherkin
scenario: user password reset confirmation 
   given a user with email "<email>" exists 
   and the user has requested a password reset 
   when the user clicks on the password reset link 
   and enters a new password "<password>" 
   then the user's password should be reset
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with email {email} exists and the user has requested a password reset")
def step_impl(context, email):
    # create user
    # send password reset email
    pass

@when("the user clicks on the password reset link and enters a new password {password}")
def step_impl(context, password):
    # click password reset link
    # enter new password
    pass

@then("the user's password should be reset")
def step_impl(context):
    # check password is reset
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user password reset confirmation given a user with email "<email>" exists and the user has requested a password reset when the user clicks on the password reset link and enters a new password "<password>" then the user's password should be reset ```



```python from behave import given, when, then

@given("a user with email {email} exists and the user has requested a password reset")
def step_impl(context, email):
    # create user
    # send password reset email
    pass

@when("the user clicks on the password reset link and enters a new password {password}")
def step_impl(context, password):
    # click password reset link
    # enter new password
    pass

@then("the user's password should be reset")
def step_impl(context):
    # check password is reset
    pass
```

Task: Write a program to find the sum of the digits of a given number.
