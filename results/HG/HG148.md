# HQFS148
## Scenario
```gherkin
scenario: testing the reset password feature 
   given a user has requested to reset their password 
   when they click the link in the email 
   and they enter their new password 
   and they confirm their new password 
   and they click the reset password button 
   then their

password should be reset


   Given a user has requested to reset their password

   When they click the link in the email

   And they enter their new password "newpassword"

   And they confirm their new password "newpassword"

   And they click the reset password button

   Then their password should be reset
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has requested to reset their password")
def step_given_a_user_has_requested_to_reset_their_password(context):
    pass

@when("they click the link in the email")
def step_when_they_click_the_link_in_the_email(context):
    pass

@when("they enter their new password {new_password}")
def step_when_they_enter_their_new_password(context, new_password):
    context.new_password = new_password

@when("they confirm their new password {new_password}")
def step_when_they_confirm_their_new_password(context, new_password):
    context.confirm_password = new_password

@when("they click the reset password button")
def step_when_they_click_the_reset_password_button(context):
    pass

@then("their password should be reset")
def step_then_their_password_should_be_reset(context):
    assert context.user.password_reset()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the reset password feature given a user has requested to reset their password when they click the link in the email and they enter their new password and they confirm their new password and they click the reset password button then their

password should be reset

Given a user has requested to reset their password
When they click the link in the email
And they enter their new password "newpassword"
And they confirm their new password "newpassword"
And they click the reset password button
Then their password should be reset
```

```python
from behave import given, when, then

@given("a user has requested to reset their password")
def step_given_a_user_has_requested_to_reset_their_password(context):
    pass

@when("they click the link in the email")
def step_when_they_click_the_link_in_the_email(context):
    pass

@when("they enter their new password {new_password}")
def step_when_they_enter_their_new_password(context, new_password):
    context.new_password = new_password

@when("they confirm their new password {new_password}")
def step_when_they_confirm_their_new_password(context, new_password):
    context.confirm_password = new_password

@when("they click the reset password button")
def step_when_they_click_the_reset_password_button(context):
    pass

@then("their password should be reset")
def step_then_their_password_should_be_reset(context):
    assert context.user.password_reset()
```

Task: Write a program to find the sum of the digits of a number.
