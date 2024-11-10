# HQFS22
## Scenario
```gherkin
scenario: a user can login 
   given a user with username "user1" 
   and password "pass1" 
   when the user logs in with the correct username 
   and password 
   then the user should be logged in
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with username 'user1' and password 'pass1'")
def step_given_a_user_with_username_user1_and_password_pass1(context):
    context.user = User("user1", "pass1")

@when("the user logs in with the correct username and password")
def step_when_the_user_logs_in_with_the_correct_username_and_password(context):
    context.login_response = context.user.login()

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    assert context.login_response.status_code == 200
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can login given a user with username "user1" and password "pass1" when the user logs in with the correct username and password then the user should be logged in ```



```python from behave import given, when, then

@given("a user with username 'user1' and password 'pass1'")
def step_given_a_user_with_username_user1_and_password_pass1(context):
    context.user = User("user1", "pass1")

@when("the user logs in with the correct username and password")
def step_when_the_user_logs_in_with_the_correct_username_and_password(context):
    context.login_response = context.user.login()

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    assert context.login_response.status_code == 200
```

Task: Write a program to find the sum of the digits of a given number.
