# HQFS43
## Scenario
```gherkin
scenario: 
   given a user is logged in 
   when they visit the profile page 
   then they should see their profile information 
   and they should see an option to edit their profile information 
   and 
   when they click on the edit button 
   then they should be taken to the edit profile page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is logged in when they visit the profile page then they should see their profile information and they should see an option to edit their profile information and when they click on the edit button then they should be taken to the edit profile page ```



from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("they visit the profile page")
def step_impl(context):
    context.profile_page = ProfilePage(context.browser)
    context.profile_page.load()

@then("they should see their profile information")
def step_impl(context):
    assert context.profile_page.is_displayed()
    assert context.profile_page.is_profile_info_displayed()

@then("they should see an option to edit their profile information")
def step_impl(context):
    assert context.profile_page.is_edit_profile_button_displayed()

@when("they click on the edit button")
def step_impl(context):
    context.edit_profile_page = context.profile_page.click_edit_profile_button()

@then("they should be taken to the edit profile page")
def step_impl(context):
    assert context.edit_profile_page.is_displayed()
