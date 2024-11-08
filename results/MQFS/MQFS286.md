# MQFS286
## Scenario
```gherkin
scenario: testing the edit account feature 
   given a user is logged in 
   when i click the edit account button 
   and i change the username to "newfoo" 
   and i change the password to "newbar" 
   and i click the save button 
   then i should see a success message "account updated successfully" 
   and the user account should be updated with the new username 
   and password
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User("oldfoo", "oldbar")
    context.session = Session()
    context.session.login(context.user)

@when("i click the edit account button")
def step_when_i_click_the_edit_account_button(context):
    context.page = context.session.visit(EditAccountPage)

@when("i change the username to {username}")
def step_when_i_change_the_username_to(context, username):
    context.page.change_username(username)

@when("i change the password to {password}")
def step_when_i_change_the_password_to(context, password):
    context.page.change_password(password)

@when("i click the save button")
def step_when_i_click_the_save_button(context):
    context.page = context.page.save()

@then("i should see a success message {message}")
def step_then_i_should_see_a_success_message(context, message):
    assert context.page.flash == message

@then("the user account should be updated with the new username and password")
def step_then_the_user_account_should_be_updated_with_the_new_username_and_password(context):
    user = context.session.get_user(context.user.username)
    assert user.password == context.page.password
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit account feature given a user is logged in when i click the edit account button and i change the username to "newfoo" and i change the password to "newbar" and i click the save button then i should see a success message "account updated successfully" and the user account should be updated with the new username and password ```



```python from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User("oldfoo", "oldbar")
    context.session = Session()
    context.session.login(context.user)

@when("i click the edit account button")
def step_when_i_click_the_edit_account_button(context):
    context.page = context.session.visit(EditAccountPage)

@when("i change the username to {username}")
def step_when_i_change_the_username_to(context, username):
    context.page.change_username(username)

@when("i change the password to {password}")
def step_when_i_change_the_password_to(context, password):
    context.page.change_password(password)

@when("i click the save button")
def step_when_i_click_the_save_button(context):
    context.page = context.page.save()

@then("i should see a success message {message}")
def step_then_i_should_see_a_success_message(context, message):
    assert context.page.flash == message

@then("the user account should be updated with the new username and password")
def step_then_the_user_account_should_be_updated_with_the_new_username_and_password(context):
    user = context.session.get_user(context.user.username)
    assert user.password == context.page.password
```

Task: Write a program to find the sum of the digits of a given number.
