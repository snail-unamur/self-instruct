# HQFS51
## Scenario
```gherkin
scenario: 
   given a list of numbers, 
   when i find the mean, 
   then the mean is the sum of the values divided by the length of the list examples: | numbers | mean | | [1, 2, 3, 4, 5] | 3 | | [1, 2, 3, 4, 5, 6] | 3.5 | | [1, 2, 3, 4, 5, 6, 7] | 4.28571428571 |
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = [1, 2, 3, 4, 5]

@when("i find the mean")
def step_impl(context):
    context.mean = sum(context.numbers) / len(context.numbers)

@then("the mean is the sum of the values divided by the length of the list")
def step_impl(context):
    assert context.mean == sum(context.numbers) / len(context.numbers)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when i find the mean, then the mean is the sum of the values divided by the length of the list examples: | numbers | mean | | [1, 2, 3, 4, 5] | 3 | | [1, 2, 3, 4, 5, 6] | 3.5 | | [1, 2, 3, 4, 5, 6, 7] | 4.28571428571 | ```



```python from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = [1, 2, 3, 4, 5]

@when("i find the mean")
def step_impl(context):
    context.mean = sum(context.numbers) / len(context.numbers)

@then("the mean is the sum of the values divided by the length of the list")
def step_impl(context):
    assert context.mean == sum(context.numbers) / len(context.numbers)
```

Task: Write a program to find the sum of the digits of a given number.
