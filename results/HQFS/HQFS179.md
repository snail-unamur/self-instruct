# HQFS179
## Scenario
```gherkin
scenario: checking if a user is logged out 
   given i am logged out 
   when i navigate to the "users" page 
   then i should see the "login" button 
   and i should not see the "logout" button
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged out")
def step_impl(context):
    context.user = None

@when("i navigate to the 'users' page")
def step_impl(context):
    context.response = context.app.get("/users")

@then("i should see the 'login' button")
def step_impl(context):
    assert "login" in context.response.content

@then("i should not see the 'logout' button")
def step_impl(context):
    assert "logout" not in context.response.content
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking if a user is logged out given i am logged out when i navigate to the "users" page then i should see the "login" button and i should not see the "logout" button ```



```python from behave import given, when, then

@given("i am logged out")
def step_impl(context):
    context.user = None

@when("i navigate to the 'users' page")
def step_impl(context):
    context.response = context.app.get("/users")

@then("i should see the 'login' button")
def step_impl(context):
    assert "login" in context.response.content

@then("i should not see the 'logout' button")
def step_impl(context):
    assert "logout" not in context.response.content
```

Task: Write a program to find the sum of the digits of a given number.
