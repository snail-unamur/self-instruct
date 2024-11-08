# MQFS266
## Scenario
```gherkin
scenario: user can filter tasks by status 
   given i am on the project details page 
   when i select a task status from the dropdown 
   then only tasks with the selected status should be displayed 
   given i am on the project details page 
   when i select "all" from the dropdown 
   then all tasks should be displayed
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the project details page")
def step_impl(context):
    pass

@when("i select a task status from the dropdown")
def step_impl(context):
    pass

@then("only tasks with the selected status should be displayed")
def step_impl(context):
    pass

@given("i am on the project details page")
def step_impl(context):
    pass

@when("i select 'all' from the dropdown")
def step_impl(context):
    pass

@then("all tasks should be displayed")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can filter tasks by status given i am on the project details page when i select a task status from the dropdown then only tasks with the selected status should be displayed given i am on the project details page when i select "all" from the dropdown then all tasks should be displayed ``` 14.



```python from behave import given, when, then

@given("i am on the project details page")
def step_impl(context):
    pass

@when("i select a task status from the dropdown")
def step_impl(context):
    pass

@then("only tasks with the selected status should be displayed")
def step_impl(context):
    pass

@given("i am on the project details page")
def step_impl(context):
    pass

@when("i select 'all' from the dropdown")
def step_impl(context):
    pass

@then("all tasks should be displayed")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
