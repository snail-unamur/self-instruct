# HQFS224
## Scenario
```gherkin
scenario: 
   given i have a list of numbers 
   when i sort the list in descending order 
   then the list should be sorted in descending order 
   and the first element should be the largest number 
   and the last element should be the smallest number 
   and the length of the list should be the same as the original list 
   and the list should contain the same numbers as the original list in the same order as the original list
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a list of numbers")
def step_impl(context):
    context.numbers = [1, 5, 8, 3, 6, 9, 2, 7, 4]

@when("i sort the list in descending order")
def step_impl(context):
    context.numbers.sort(reverse=True)

@then("the list should be sorted in descending order")
def step_impl(context):
    assert context.numbers == sorted(context.numbers, reverse=True)

@then("the first element should be the largest number")
def step_impl(context):
    assert context.numbers[0] == max(context.numbers)

@then("the last element should be the smallest number")
def step_impl(context):
    assert context.numbers[-1] == min(context.numbers)

@then("the length of the list should be the same as the original list")
def step_impl(context):
    assert len(context.numbers) == len([1, 5, 8, 3, 6, 9, 2, 7, 4])

@then("the list should contain the same numbers as the original list in the same order as the original list")
def step_impl(context):
    assert context.numbers == [1, 5, 8, 3, 6, 9, 2, 7, 4]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of numbers when i sort the list in descending order then the list should be sorted in descending order and the first element should be the largest number and the last element should be the smallest number and the length of the list should be the same as the original list and the list should contain the same numbers as the original list in the same order as the original list ```



```python from behave import given, when, then

@given("i have a list of numbers")
def step_impl(context):
    context.numbers = [1, 5, 8, 3, 6, 9, 2, 7, 4]

@when("i sort the list in descending order")
def step_impl(context):
    context.numbers.sort(reverse=True)

@then("the list should be sorted in descending order")
def step_impl(context):
    assert context.numbers == sorted(context.numbers, reverse=True)

@then("the first element should be the largest number")
def step_impl(context):
    assert context.numbers[0] == max(context.numbers)

@then("the last element should be the smallest number")
def step_impl(context):
    assert context.numbers[-1] == min(context.numbers)

@then("the length of the list should be the same as the original list")
def step_impl(context):
    assert len(context.numbers) == len([1, 5, 8, 3, 6, 9, 2, 7, 4])

@then("the list should contain the same numbers as the original list in the same order as the original list")
def step_impl(context):
    assert context.numbers == [1, 5, 8, 3, 6, 9, 2, 7, 4]
```

Task: Write a program to find the sum of the digits of a number.
