# MQFS217
## Scenario
```gherkin
scenario: testing the functionality of the remove method 
   given i have a list of integers 
   then i should be able to remove an integer from the list 
   when i remove 5 from the list 
   then the list should not contain 5
```


## Python Implementation
```python
from behave import given, when, then

@given('i have a list of integers')
def step_impl(context):
    context.list = [1, 2, 3, 4, 5]

@when('i remove 5 from the list')
def step_impl(context):
    context.list.remove(5)

@then('the list should not contain 5')
def step_impl(context):
    assert 5 not in context.list
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the remove method given i have a list of integers then i should be able to remove an integer from the list when i remove 5 from the list then the list should not contain 5 ```



```python from behave import given, when, then

@given('i have a list of integers')
def step_impl(context):
    context.list = [1, 2, 3, 4, 5]

@when('i remove 5 from the list')
def step_impl(context):
    context.list.remove(5)

@then('the list should not contain 5')
def step_impl(context):
    assert 5 not in context.list
```

Task: Write a program to find the second largest number in a list.
