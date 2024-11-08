# MQFS14
## Scenario
```gherkin
scenario: 
   given a user is logged in 
   when the user navigates to the profile page 
   then the user should see their profile information 
   given the user has the correct credentials 
   when the user enters username 
   and the user enters password 
   and clicks login 
   then the user is presented with a welcome message 
   given the user is on the welcome page 
   when the user clicks on the profile link 
   then the user is taken to the profile page
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("the user navigates to the profile page")
def step_impl(context):
    context.profile_page = context.user.navigate_to_profile_page()

@then("the user should see their profile information")
def step_impl(context):
    assert context.profile_page.is_displayed

@given("the user has the correct credentials")
def step_impl(context):
    context.user = User("testuser")

@when("the user enters username and the user enters password and clicks login")
def step_impl(context):
    context.user.login()

@then("the user is presented with a welcome message")
def step_impl(context):
    assert context.user.is_welcome_displayed

@given("the user is on the welcome page")
def step_impl(context):
    context.welcome_page = WelcomePage()

@when("the user clicks on the profile link")
def step_impl(context):
    context.profile_page = context.welcome_page.click_profile_link()

@then("the user is taken to the profile page")
def step_impl(context):
    assert context.profile_page.is_displayed
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is logged in when the user navigates to the profile page then the user should see their profile information given the user has the correct credentials when the user enters username and the user enters password and clicks login then the user is presented with a welcome message given the user is on the welcome page when the user clicks on the profile link then the user is taken to the profile page ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@when("the user navigates to the profile page")
def step_impl(context):
    context.profile_page = context.user.navigate_to_profile_page()

@then("the user should see their profile information")
def step_impl(context):
    assert context.profile_page.is_displayed

@given("the user has the correct credentials")
def step_impl(context):
    context.user = User("testuser")

@when("the user enters username and the user enters password and clicks login")
def step_impl(context):
    context.user.login()

@then("the user is presented with a welcome message")
def step_impl(context):
    assert context.user.is_welcome_displayed

@given("the user is on the welcome page")
def step_impl(context):
    context.welcome_page = WelcomePage()

@when("the user clicks on the profile link")
def step_impl(context):
    context.profile_page = context.welcome_page.click_profile_link()

@then("the user is taken to the profile page")
def step_impl(context):
    assert context.profile_page.is_displayed
```

Task: Write a program to find the sum of the digits of a number.
