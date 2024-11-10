# MQFS262
## Scenario
```gherkin
scenario: user can log in 
   given the user is on the login page 
   when the user enters their username 
   and password 
   and clicks the login button 
   then the user should be logged in 
   and taken to their profile page 
   when the user clicks on the logout button 
   then the user should be logged out 
   and taken to the login page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can log in given the user is on the login page when the user enters their username and password and clicks the login button then the user should be logged in and taken to their profile page when the user clicks on the logout button then the user should be logged out and taken to the login page```



from behave import given, when, then

@given("the user is on the login page")
def step_given_the_user_is_on_the_login_page(context):
    pass

@when("the user enters their username and password and clicks the login button")
def step_when_the_user_enters_their_username_and_password_and_clicks_the_login_button(context):
    pass

@then("the user should be logged in and taken to their profile page")
def step_then_the_user_should_be_logged_in_and_taken_to_their_profile_page(context):
    pass

@when("the user clicks on the logout button")
def step_when_the_user_clicks_on_the_logout_button(context):
    pass

@then("the user should be logged out and taken to the login page")
def step_then_the_user_should_be_logged_out_and_taken_to_the_login_page(context):
    pass
