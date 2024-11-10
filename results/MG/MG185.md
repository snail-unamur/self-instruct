# MQFS185
## Scenario
```gherkin
scenario: testing the login functionality 
   given a user with username "user1" 
   and password "password1" 
   when the user navigates to the login page 
   and enters the username 
   and password 
   and clicks the login button 
   then the user should be logged in 
   and should be redirected to the homepage 
   given a user with incorrect username "user2" 
   and password "password2" 
   when the user navigates to the login page 
   and enters the incorrect username 
   and password 
   and clicks the login button 
   then the user should not be logged in 
   and should see an error message
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with username 'user1' and password 'password1'")
def step_impl(context):
    context.user = User("user1", "password1")

@given("a user with incorrect username 'user2' and password 'password2'")
def step_impl(context):
    context.user = User("user2", "password2")

@when("the user navigates to the login page")
def step_impl(context):
    context.login_page = LoginPage()

@when("enters the username and password and clicks the login button")
def step_impl(context):
    context.login_page.login(context.user)

@then("the user should be logged in and should be redirected to the homepage")
def step_impl(context):
    assert context.login_page.is_logged_in()
    assert context.login_page.is_on_homepage()

@then("the user should not be logged in and should see an error message")
def step_impl(context):
    assert not context.login_page.is_logged_in()
    assert context.login_page.is_error_message_visible()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given a user with username "user1" and password "password1" when the user navigates to the login page and enters the username and password and clicks the login button then the user should be logged in and should be redirected to the homepage given a user with incorrect username "user2" and password "password2" when the user navigates to the login page and enters the incorrect username and password and clicks the login button then the user should not be logged in and should see an error message```



```python from behave import given, when, then

@given("a user with username 'user1' and password 'password1'")
def step_impl(context):
    context.user = User("user1", "password1")

@given("a user with incorrect username 'user2' and password 'password2'")
def step_impl(context):
    context.user = User("user2", "password2")

@when("the user navigates to the login page")
def step_impl(context):
    context.login_page = LoginPage()

@when("enters the username and password and clicks the login button")
def step_impl(context):
    context.login_page.login(context.user)

@then("the user should be logged in and should be redirected to the homepage")
def step_impl(context):
    assert context.login_page.is_logged_in()
    assert context.login_page.is_on_homepage()

@then("the user should not be logged in and should see an error message")
def step_impl(context):
    assert not context.login_page.is_logged_in()
    assert context.login_page.is_error_message_visible()
```

Task: Write a program to find the sum of the digits of a given number.
