# MQFS249
## Scenario
```gherkin
scenario: a user can add a new task to a project 
   given a user is logged in 
   and the user is on the project page with the task list open 
   when the user clicks on the "add task" button 
   then the user is taken to the task creation page 
   when the user enters the task details 
   and clicks "create" 
   then the task is added to the task list
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in and the user is on the project page with the task list open")
def step_impl(context):
    pass

@when("the user clicks on the 'add task' button")
def step_impl(context):
    pass

@then("the user is taken to the task creation page")
def step_impl(context):
    pass

@when("the user enters the task details and clicks 'create'")
def step_impl(context):
    pass

@then("the task is added to the task list")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new task to a project given a user is logged in and the user is on the project page with the task list open when the user clicks on the "add task" button then the user is taken to the task creation page when the user enters the task details and clicks "create" then the task is added to the task list ```



```python from behave import given, when, then

@given("a user is logged in and the user is on the project page with the task list open")
def step_impl(context):
    pass

@when("the user clicks on the 'add task' button")
def step_impl(context):
    pass

@then("the user is taken to the task creation page")
def step_impl(context):
    pass

@when("the user enters the task details and clicks 'create'")
def step_impl(context):
    pass

@then("the task is added to the task list")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
