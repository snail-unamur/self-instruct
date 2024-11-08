# MQFS76
## Scenario
```gherkin
scenario: 
   given a user with the username "johndoe" 
   and the password "password123" 
   when they visit the login page 
   then they should see a login form with fields for their username 
   and password 
   when they enter their username 
   and password 
   and click the login button 
   then they should be logged in 
   and they should be redirected to their profile page 
   given that the user is logged in 
   when they visit the logout page 
   then they should be logged out 
   and they should be redirected to the login page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user with the username "johndoe" and the password "password123" when they visit the login page then they should see a login form with fields for their username and password when they enter their username and password and click the login button then they should be logged in and they should be redirected to their profile page given that the user is logged in when they visit the logout page then they should be logged out and they should be redirected to the login page ```



```python from behave import given, when, then

@given("a user with the username 'johndoe' and the password 'password123'")
def step_given_a_user_with_the_username_johndoe_and_the_password_password123(context):
    context.user = User("johndoe", "password123")

@when("they visit the login page")
def step_when_they_visit_the_login_page(context):
    context.login_page = LoginPage()
    context.login_page.load()

@then("they should see a login form with fields for their username and password")
def step_then_they_should_see_a_login_form_with_fields_for_their_username_and_password(context):
    assert context.login_page.is_displayed()
    assert context.login_page.username_field.is_displayed()
    assert context.login_page.password_field.is_displayed()

@when("they enter their username and password and click the login button")
def step_when_they_enter_their_username_and_password_and_click_the_login_button(context):
    context.login_page.username_field.send_keys(context.user.username)
    context.login_page.password_field.send_keys(context.user.password)
    context.login_page.login_button.click()

@then("they should be logged in and they should be redirected to their profile page")
def step_then_they_should_be_logged_in_and_they_should_be_redirected_to_their_profile_page(context):
    assert context.profile_page.is_displayed()

@given("that the user is logged in")
def step_given_that_the_user_is_logged_in(context):
    context.profile_page = ProfilePage()
    context.profile_page.load()

@when("they visit the logout page")
def step_when_they_visit_the_logout_page(
