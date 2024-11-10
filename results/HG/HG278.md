# HQFS278
## Scenario
```gherkin
scenario: 
   given a user is logged in 
   when they go to the profile page 
   then they should see their profile information 
   and they should be able to edit their profile information 
   when they edit their profile information 
   then they should be able to save the changes 
   and the changes should be reflected on the profile page 
   and they should be able to delete their account 
   when they delete their account 
   then they should be logged out 
   and they should be redirected to the login page 
   and their account should be deleted
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("they go to the profile page")
def step_impl(context):
    context.profile_page = ProfilePage(context.browser)
    context.profile_page.load()

@then("they should see their profile information")
def step_impl(context):
    assert context.profile_page.is_displayed()
    assert context.profile_page.get_profile_info() == context.user.get_profile_info()

@then("they should be able to edit their profile information")
def step_impl(context):
    context.profile_page.edit_profile_info()

@then("they should be able to save the changes")
def step_impl(context):
    context.profile_page.save_changes()

@then("the changes should be reflected on the profile page")
def step_impl(context):
    assert context.profile_page.get_profile_info() == context.user.get_edited_profile_info()

@then("they should be able to delete their account")
def step_impl(context):
    context.profile_page.delete_account()

@then("they should be logged out")
def step_impl(context):
    assert not context.user.is_logged_in()

@then("they should be redirected to the login page")
def step_impl(context):
    assert context.browser.current_url == context.base_url + "login"

@then("their account should be deleted")
def step_impl(context):
    assert not User.objects.filter(email=context.user.email).exists()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is logged in when they go to the profile page then they should see their profile information and they should be able to edit their profile information when they edit their profile information then they should be able to save the changes and the changes should be reflected on the profile page and they should be able to delete their account when they delete their account then they should be logged out and they should be redirected to the login page and their account should be deleted ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("they go to the profile page")
def step_impl(context):
    context.profile_page = ProfilePage(context.browser)
    context.profile_page.load()

@then("they should see their profile information")
def step_impl(context):
    assert context.profile_page.is_displayed()
    assert context.profile_page.get_profile_info() == context.user.get_profile_info()

@then("they should be able to edit their profile information")
def step_impl(context):
    context.profile_page.edit_profile_info()

@then("they should be able to save the changes")
def step_impl(context):
    context.profile_page.save_changes()

@then("the changes should be reflected on the profile page")
def step_impl(context):
    assert context.profile_page.get_profile_info() == context.user.get_edited_profile_info()

@then("they should be able to delete their account")
def step_impl(context):
    context.profile_page.delete_account()

@then("they should be logged out")
def step_impl(context):
    assert not context.user.is_logged_in()

@then("they should be redirected to the login page")
def step_impl(context):
    assert context.browser.current_url == context.base_url + "login"

@then("their account should be deleted")
def step_impl(context):
    assert not User.objects.filter(email=context.user.email).exists()
```

Task: Write a program to find the sum of the digits of a number.
