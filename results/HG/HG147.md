# HQFS147
## Scenario
```gherkin
scenario: a user cannot register with a password that is too short 
   given a user is on the registration page 
   when they enter a password that is less than 8 characters 
   and they click the 'register' button 
   then their account is not created 
   and they are not logged in
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user cannot register with a password that is too short given a user is on the registration page when they enter a password that is less than 8 characters and they click the 'register' button then their account is not created and they are not logged in ```



from behave import given, when, then

@given("a user is on the registration page")
def step_given_a_user_is_on_the_registration_page(context):
    pass

@when("they enter a password that is less than 8 characters")
def step_when_they_enter_a_password_that_is_less_than_8_characters(context):
    context.password = "short"

@when("they click the 'register' button")
def step_when_they_click_the_register_button(context):
    pass

@then("their account is not created")
def step_then_their_account_is_not_created(context):
    assert not context.user.exists

@then("they are not logged in")
def step_then_they_are_not_logged_in(context):
    assert not context.session.logged_in


Task: Write a program to find the sum of the digits of a number.
