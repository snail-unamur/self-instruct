# MQFS155
## Scenario
```gherkin
scenario: testing the login functionality 
   given a user with the username "johndoe" 
   and the password "password123" 
   when the user navigates to the login page 
   then the user enters the username "johndoe" 
   and the password "password123" 
   and clicks the login button 
   then the user is redirected to the homepage 
   and the user is logged in
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with the username 'johndoe' and the password 'password123'")
def step_given(context):
    context.user = User("johndoe", "password123")

@when("the user navigates to the login page")
def step_when(context):
    context.login_page = LoginPage()
    context.login_page.navigate()

@when("the user enters the username 'johndoe' and the password 'password123' and clicks the login button")
def step_when(context):
    context.login_page.login(context.user)

@then("the user is redirected to the homepage and the user is logged in")
def step_then(context):
    context.homepage = HomePage()
    context.homepage.wait_for_page_load()
    assert context.homepage.is_logged_in(context.user)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given a user with the username "johndoe" and the password "password123" when the user navigates to the login page then the user enters the username "johndoe" and the password "password123" and clicks the login button then the user is redirected to the homepage and the user is logged in```



```python from behave import given, when, then

@given("a user with the username 'johndoe' and the password 'password123'")
def step_given(context):
    context.user = User("johndoe", "password123")

@when("the user navigates to the login page")
def step_when(context):
    context.login_page = LoginPage()
    context.login_page.navigate()

@when("the user enters the username 'johndoe' and the password 'password123' and clicks the login button")
def step_when(context):
    context.login_page.login(context.user)

@then("the user is redirected to the homepage and the user is logged in")
def step_then(context):
    context.homepage = HomePage()
    context.homepage.wait_for_page_load()
    assert context.homepage.is_logged_in(context.user)
```

Task: Write a program to find the sum of the digits of a given number.
