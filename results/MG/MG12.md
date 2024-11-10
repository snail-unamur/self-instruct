# MQFS12
## Scenario
```gherkin
scenario: 
   given a user with the username "johndoe" 
   and the password "secret" 
   when they log in 
   then they should be redirected to their profile page 
   and they should see a welcome message with their username
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with the username 'johndoe' and the password 'secret'")
def step_impl(context):
    context.user = User("johndoe", "secret")

@when("they log in")
def step_impl(context):
    context.response = context.user.login()

@then("they should be redirected to their profile page")
def step_impl(context):
    assert context.response.url == "/profile"

@then("they should see a welcome message with their username")
def step_impl(context):
    assert context.response.text.find(f"Welcome {context.user.username}") != -1
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user with the username "johndoe" and the password "secret" when they log in then they should be redirected to their profile page and they should see a welcome message with their username ```



```python from behave import given, when, then

@given("a user with the username 'johndoe' and the password 'secret'")
def step_impl(context):
    context.user = User("johndoe", "secret")

@when("they log in")
def step_impl(context):
    context.response = context.user.login()

@then("they should be redirected to their profile page")
def step_impl(context):
    assert context.response.url == "/profile"

@then("they should see a welcome message with their username")
def step_impl(context):
    assert context.response.text.find(f"Welcome {context.user.username}") != -1
```

Task: Write a program to find the sum of the digits of a given number.
