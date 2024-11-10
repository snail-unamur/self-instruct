# MQFS25
## Scenario
```gherkin
scenario: check if the user is authorized to perform an action 
   given the user is authorized to perform an action 
   when the user tries to perform the action 
   then the user should be able to perform the action successfully
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is authorized to perform an action")
def step_given(context):
    context.user = User()
    context.user.is_authorized = True

@when("the user tries to perform the action")
def step_when(context):
    context.result = context.user.perform_action()

@then("the user should be able to perform the action successfully")
def step_then(context):
    assert context.result == True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check if the user is authorized to perform an action given the user is authorized to perform an action when the user tries to perform the action then the user should be able to perform the action successfully ```



```python from behave import given, when, then

@given("the user is authorized to perform an action")
def step_given(context):
    context.user = User()
    context.user.is_authorized = True

@when("the user tries to perform the action")
def step_when(context):
    context.result = context.user.perform_action()

@then("the user should be able to perform the action successfully")
def step_then(context):
    assert context.result == True
```

Task: Write a program to find the sum of the digits of a given number.
