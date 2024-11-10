# HQFS197
## Scenario
```gherkin
scenario: manage user 
   given user "john" exists 
   when i create a new user 
   then user "john" is notified of the new user creation 
   and user "john" is notified of the new user creation through email
```


## Python Implementation
```python
from behave import given, when, then

@given("user 'john' exists")
def step_given_user_john_exists(context):
    # create user 'john'
    pass

@when("i create a new user")
def step_when_i_create_a_new_user(context):
    # create new user
    pass

@then("user 'john' is notified of the new user creation")
def step_then_user_john_is_notified_of_the_new_user_creation(context):
    # check if user 'john' was notified
    pass

@then("user 'john' is notified of the new user creation through email")
def step_then_user_john_is_notified_of_the_new_user_creation_through_email(context):
    # check if user 'john' was notified through email
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: manage user given user "john" exists when i create a new user then user "john" is notified of the new user creation and user "john" is notified of the new user creation through email ```



```python from behave import given, when, then

@given("user 'john' exists")
def step_given_user_john_exists(context):
    # create user 'john'
    pass

@when("i create a new user")
def step_when_i_create_a_new_user(context):
    # create new user
    pass

@then("user 'john' is notified of the new user creation")
def step_then_user_john_is_notified_of_the_new_user_creation(context):
    # check if user 'john' was notified
    pass

@then("user 'john' is notified of the new user creation through email")
def step_then_user_john_is_notified_of_the_new_user_creation_through_email(context):
    # check if user 'john' was notified through email
    pass
```

Task: Write a program to find the sum of the digits of a given number.
