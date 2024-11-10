# HQFS61
## Scenario
```gherkin
scenario: a user can sort tasks 
   given the user is logged in 
   and there are tasks in the system 
   when the user clicks on a column header to sort the tasks 
   then the tasks should be sorted by that column in ascending or descending order
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in and there are tasks in the system")
def step_impl(context):
    # Implement preconditions
    pass

@when("the user clicks on a column header to sort the tasks")
def step_impl(context):
    # Implement action
    pass

@then("the tasks should be sorted by that column in ascending or descending order")
def step_impl(context):
    # Implement verification
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can sort tasks given the user is logged in and there are tasks in the system when the user clicks on a column header to sort the tasks then the tasks should be sorted by that column in ascending or descending order ```



```python from behave import given, when, then

@given("the user is logged in and there are tasks in the system")
def step_impl(context):
    # Implement preconditions
    pass

@when("the user clicks on a column header to sort the tasks")
def step_impl(context):
    # Implement action
    pass

@then("the tasks should be sorted by that column in ascending or descending order")
def step_impl(context):
    # Implement verification
    pass
```

Task: Write a program to find the second largest number in a list.
