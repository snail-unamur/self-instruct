# HQFS279
## Scenario
```gherkin
scenario: 
   given i have a list of numbers: | num | | 1 | | 2 | | 3 | | 4 | | 5 | | 6 | | 7 | | 8 | | 9 | | 10 | 
   when i select every 3rd number from the list starting from the 2nd number 
   then i should get the following list: | num | | 3 | | 6 | | 9 | | 10 |
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a list of numbers:")
def step_impl(context):
    context.numbers = list(range(1, 11))

@when("i select every 3rd number from the list starting from the 2nd number")
def step_impl(context):
    context.selected_numbers = context.numbers[1::3]

@then("i should get the following list:")
def step_impl(context):
    context.assert_equals(context.selected_numbers, [3, 6, 9, 10])
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of numbers: | num | | 1 | | 2 | | 3 | | 4 | | 5 | | 6 | | 7 | | 8 | | 9 | | 10 | when i select every 3rd number from the list starting from the 2nd number then i should get the following list: | num | | 3 | | 6 | | 9 | | 10 | ```



```python
from behave import given, when, then

@given("i have a list of numbers:")
def step_impl(context):
    context.numbers = list(range(1, 11))

@when("i select every 3rd number from the list starting from the 2nd number")
def step_impl(context):
    context.selected_numbers = context.numbers[1::3]

@then("i should get the following list:")
def step_impl(context):
    context.assert_equals(context.selected_numbers, [3, 6, 9, 10])
```

Task: Write a program to find the sum of the digits of a given number.
