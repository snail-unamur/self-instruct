# MQFS198
## Scenario
```gherkin
scenario: testing the login functionality 
   given a user with the username "testuser" 
   and password "testpassword" 
   when the user logs in with the correct credentials 
   then the user should be logged in 
   when the user logs in with the incorrect credentials 
   then the user should not be logged in
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with the username 'testuser' and password 'testpassword'")
def step_given_a_user_with_the_username_testuser_and_password_testpassword(context):
    context.user = User("testuser", "testpassword")

@when("the user logs in with the correct credentials")
def step_when_the_user_logs_in_with_the_correct_credentials(context):
    context.login_response = context.user.login()

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    assert context.login_response.status_code == 200

@when("the user logs in with the incorrect credentials")
def step_when_the_user_logs_in_with_the_incorrect_credentials(context):
    context.user.password = "wrongpassword"
    context.login_response = context.user.login()

@then("the user should not be logged in")
def step_then_the_user_should_not_be_logged_in(context):
    assert context.login_response.status_code != 200
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given a user with the username "testuser" and password "testpassword" when the user logs in with the correct credentials then the user should be logged in when the user logs in with the incorrect credentials then the user should not be logged in``` note: the above scenarios are just examples, you can create your own scenarios and generate the step functions accordingly.



```python from behave import given, when, then

@given("a user with the username 'testuser' and password 'testpassword'")
def step_given_a_user_with_the_username_testuser_and_password_testpassword(context):
    context.user = User("testuser", "testpassword")

@when("the user logs in with the correct credentials")
def step_when_the_user_logs_in_with_the_correct_credentials(context):
    context.login_response = context.user.login()

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    assert context.login_response.status_code == 200

@when("the user logs in with the incorrect credentials")
def step_when_the_user_logs_in_with_the_incorrect_credentials(context):
    context.user.password = "wrongpassword"
    context.login_response = context.user.login()

@then("the user should not be logged in")
def step_then_the_user_should_not_be_logged_in(context):
    assert context.login_response.status_code != 200
```

Task: Write a program to find the sum of the digits of a given number.
