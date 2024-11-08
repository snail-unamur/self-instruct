# MQFS278
## Scenario
```gherkin
scenario: testing the edit profile functionality 
   given the user is logged in 
   when the user clicks on the edit profile button 
   and the user enters the new details 
   then the user should be able to update the profile successfully
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user clicks on the edit profile button")
def step_impl(context):
    context.profile_page = context.user.go_to_profile_page()
    context.profile_page.click_edit_profile_button()

@then("the user enters the new details")
def step_impl(context):
    context.profile_page.enter_new_details()

@then("the user should be able to update the profile successfully")
def step_impl(context):
    context.profile_page.submit_changes()
    context.profile_page.assert_profile_updated()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit profile functionality given the user is logged in when the user clicks on the edit profile button and the user enters the new details then the user should be able to update the profile successfully ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user clicks on the edit profile button")
def step_impl(context):
    context.profile_page = context.user.go_to_profile_page()
    context.profile_page.click_edit_profile_button()

@then("the user enters the new details")
def step_impl(context):
    context.profile_page.enter_new_details()

@then("the user should be able to update the profile successfully")
def step_impl(context):
    context.profile_page.submit_changes()
    context.profile_page.assert_profile_updated()
```

Task: Write a program to find the sum of the digits of a given number.
