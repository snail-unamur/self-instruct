# HQFS16
## Scenario
```gherkin
scenario: a user can edit their profile 
   given the user is logged in 
   when the user navigates to their profile page 
   and the user clicks the edit button 
   then the user should be taken to the edit profile page 
   and the user should see the current profile information displayed on the page 
   and the user can update their profile information 
   and the user can save the changes 
   then the user should be taken back to the profile page 
   and the user should see the updated profile information displayed on the page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("the user navigates to their profile page")
def step_impl(context):
    context.profile_page = context.user.navigate_to_profile_page()

@when("the user clicks the edit button")
def step_impl(context):
    context.edit_profile_page = context.profile_page.click_edit_button()

@then("the user should be taken to the edit profile page")
def step_impl(context):
    assert context.edit_profile_page is not None

@then("the user should see the current profile information displayed on the page")
def step_impl(context):
    assert context.edit_profile_page.is_profile_information_displayed()

@when("the user updates their profile information")
def step_impl(context):
    context.edit_profile_page.update_profile_information()

@when("the user can save the changes")
def step_impl(context):
    context.profile_page = context.edit_profile_page.save_changes()

@then("the user should be taken back to the profile page")
def step_impl(context):
    assert context.profile_page is not None

@then("the user should see the updated profile information displayed on the page")
def step_impl(context):
    assert context.profile_page.is_profile_information_updated()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit their profile given the user is logged in when the user navigates to their profile page and the user clicks the edit button then the user should be taken to the edit profile page and the user should see the current profile information displayed on the page and the user can update their profile information and the user can save the changes then the user should be taken back to the profile page and the user should see the updated profile information displayed on the page ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("the user navigates to their profile page")
def step_impl(context):
    context.profile_page = context.user.navigate_to_profile_page()

@when("the user clicks the edit button")
def step_impl(context):
    context.edit_profile_page = context.profile_page.click_edit_button()

@then("the user should be taken to the edit profile page")
def step_impl(context):
    assert context.edit_profile_page is not None

@then("the user should see the current profile information displayed on the page")
def step_impl(context):
    assert context.edit_profile_page.is_profile_information_displayed()

@when("the user updates their profile information")
def step_impl(context):
    context.edit_profile_page.update_profile_information()

@when("the user can save the changes")
def step_impl(context):
    context.profile_page = context.edit_profile_page.save_changes()

@then("the user should be taken back to the profile page")
def step_impl(context):
    assert context.profile_page is not None

@then("the user should see the updated profile information displayed on the page")
def step_impl(context):
    assert context.profile_page.is_profile_information_updated()
```

Task: Write a program to find the sum of the digits of a number.
