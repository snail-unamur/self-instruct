# MQFS275
## Scenario
```gherkin
scenario: testing the user profile functionality 
   given i am logged in 
   when i go to my profile page 
   then i should be able to view 
   and edit my personal information 
   and i should be able to view 
   and edit my account settings 
   and i should be able to view my order history
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the user profile functionality given i am logged in when i go to my profile page then i should be able to view and edit my personal information and i should be able to view and edit my account settings and i should be able to view my order history ```



from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("i go to my profile page")
def step_impl(context):
    context.profile_page = context.user.go_to_profile_page()

@then("i should be able to view and edit my personal information")
def step_impl(context):
    assert context.profile_page.is_displayed()
    context.profile_page.edit_personal_info()

@then("i should be able to view and edit my account settings")
def step_impl(context):
    context.profile_page.edit_account_settings()

@then("i should be able to view my order history")
def step_impl(context):
    context.profile_page.view_order_history()


Task: Write a program to find the sum of the digits of a given number.
