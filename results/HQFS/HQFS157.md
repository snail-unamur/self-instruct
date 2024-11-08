# HQFS157
## Scenario
```gherkin
scenario: a user can log in 
   given the user is on the login page 
   when the user enters valid credentials 
   then the user should be logged in 
   and the user should be redirected to the home page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the login page")
def step_given_the_user_is_on_the_login_page(context):
    context.login_page = LoginPage()
    context.login_page.navigate()

@when("the user enters valid credentials")
def step_when_the_user_enters_valid_credentials(context):
    context.user = User()
    context.user.login(context.login_page)

@then("the user should be logged in and the user should be redirected to the home page")
def step_then_the_user_should_be_logged_in_and_the_user_should_be_redirected_to_the_home_page(context):
    context.home_page = HomePage()
    context.home_page.is_displayed.should.be.true
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can log in given the user is on the login page when the user enters valid credentials then the user should be logged in and the user should be redirected to the home page ```



```python from behave import given, when, then

@given("the user is on the login page")
def step_given_the_user_is_on_the_login_page(context):
    context.login_page = LoginPage()
    context.login_page.navigate()

@when("the user enters valid credentials")
def step_when_the_user_enters_valid_credentials(context):
    context.user = User()
    context.user.login(context.login_page)

@then("the user should be logged in and the user should be redirected to the home page")
def step_then_the_user_should_be_logged_in_and_the_user_should_be_redirected_to_the_home_page(context):
    context.home_page = HomePage()
    context.home_page.is_displayed.should.be.true
```

Task: Write a program to find the sum of the digits of a given number.
