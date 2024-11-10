# HQFS15
## Scenario
```gherkin
scenario: testing the functionality of the delete button 
   given the user is logged in 
   when the user clicks on the delete button 
   then the task is deleted
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user clicks on the delete button")
def step_impl(context):
    context.task = Task()
    context.task.delete()

@then("the task is deleted")
def step_impl(context):
    assert context.task.is_deleted
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the delete button given the user is logged in when the user clicks on the delete button then the task is deleted ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user clicks on the delete button")
def step_impl(context):
    context.task = Task()
    context.task.delete()

@then("the task is deleted")
def step_impl(context):
    assert context.task.is_deleted
```

Task: Write a program to find the sum of the digits of a given number.
