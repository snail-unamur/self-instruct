# MQFS97
## Scenario
```gherkin
scenario: 
   given i have a list of numbers, 
   when i sort the list in ascending order, 
   then the list should be sorted in ascending order 
   and the first element should be the smallest number 
   and the last element should be the largest number
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a list of numbers")
def step_impl(context):
    context.numbers = [8, 92, 2, 5, -4, 92, 5, 101]

@when("i sort the list in ascending order")
def step_impl(context):
    context.numbers.sort()

@then("the list should be sorted in ascending order")
def step_impl(context):
    assert context.numbers == sorted(context.numbers)

@then("the first element should be the smallest number")
def step_impl(context):
    assert context.numbers[0] == min(context.numbers)

@then("the last element should be the largest number")
def step_impl(context):
    assert context.numbers[-1] == max(context.numbers)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of numbers, when i sort the list in ascending order, then the list should be sorted in ascending order and the first element should be the smallest number and the last element should be the largest number```



```python from behave import given, when, then

@given("i have a list of numbers")
def step_impl(context):
    context.numbers = [8, 92, 2, 5, -4, 92, 5, 101]

@when("i sort the list in ascending order")
def step_impl(context):
    context.numbers.sort()

@then("the list should be sorted in ascending order")
def step_impl(context):
    assert context.numbers == sorted(context.numbers)

@then("the first element should be the smallest number")
def step_impl(context):
    assert context.numbers[0] == min(context.numbers)

@then("the last element should be the largest number")
def step_impl(context):
    assert context.numbers[-1] == max(context.numbers)
```

Task: Write a program to find the sum of the digits of a given number.
