# MQFS118
## Scenario
```gherkin
scenario: check that the user can edit their account details 
   given the user is logged in to the system 
   when the user navigates to their account details page 
   and edits their details 
   then the user can save their updated account details
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in to the system")
def step_impl(context):
    context.user = User("testuser", "testpassword")
    context.user.login()

@when("the user navigates to their account details page")
def step_impl(context):
    context.account_page = context.user.navigate_to_account_details_page()

@when("edits their details")
def step_impl(context):
    context.account_page.edit_details("new_name", "new_email")

@then("the user can save their updated account details")
def step_impl(context):
    context.account_page.save_details()
    assert context.account_page.is_saved_message_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check that the user can edit their account details given the user is logged in to the system when the user navigates to their account details page and edits their details then the user can save their updated account details ```



```python from behave import given, when, then

@given("the user is logged in to the system")
def step_impl(context):
    context.user = User("testuser", "testpassword")
    context.user.login()

@when("the user navigates to their account details page")
def step_impl(context):
    context.account_page = context.user.navigate_to_account_details_page()

@when("edits their details")
def step_impl(context):
    context.account_page.edit_details("new_name", "new_email")

@then("the user can save their updated account details")
def step_impl(context):
    context.account_page.save_details()
    assert context.account_page.is_saved_message_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
