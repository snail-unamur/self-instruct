# MQFS20
## Scenario
```gherkin
scenario: 
   given i have a user with email "john.doe@example.com" 
   and password "secret" 
   when i log in with the 
   given credentials 
   then i should be logged in
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a user with email 'john.doe@example.com' and password 'secret'")
def step_impl(context):
    context.user = User("john.doe@example.com", "secret")

@when("i log in with the given credentials")
def step_impl(context):
    context.user.login()

@then("i should be logged in")
def step_impl(context):
    assert context.user.is_logged_in
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a user with email "john.doe@example.com" and password "secret" when i log in with the given credentials then i should be logged in ```



```python from behave import given, when, then

@given("i have a user with email 'john.doe@example.com' and password 'secret'")
def step_impl(context):
    context.user = User("john.doe@example.com", "secret")

@when("i log in with the given credentials")
def step_impl(context):
    context.user.login()

@then("i should be logged in")
def step_impl(context):
    assert context.user.is_logged_in
```

Task: Write a program to find the sum of the digits of a given number.
