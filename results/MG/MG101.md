# MQFS101
## Scenario
```gherkin
scenario: a user can edit an existing task in the task list 
   given a user is on the task list page 
   when the user clicks on the "edit" button for a specific task 
   then the user is redirected to the task editing page
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is on the task list page")
def step_impl(context):
    pass

@when("the user clicks on the 'edit' button for a specific task")
def step_impl(context):
    pass

@then("the user is redirected to the task editing page")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit an existing task in the task list given a user is on the task list page when the user clicks on the "edit" button for a specific task then the user is redirected to the task editing page ```



```python from behave import given, when, then

@given("a user is on the task list page")
def step_impl(context):
    pass

@when("the user clicks on the 'edit' button for a specific task")
def step_impl(context):
    pass

@then("the user is redirected to the task editing page")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
