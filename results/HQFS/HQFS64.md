# HQFS64
## Scenario
```gherkin
scenario: 
   given a list of numbers 
   when i sort them 
   then i should get a sorted list 
   and the list should be in descending order 
   and the first element should be the largest number 
   and the last element should be the smallest number
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = [1, 5, 8, 3, 6, 9, 2, 7, 4]

@when("i sort them")
def step_impl(context):
    context.numbers.sort(reverse=True)

@then("i should get a sorted list")
def step_impl(context):
    assert sorted(context.numbers, reverse=True) == context.numbers

@then("the list should be in descending order")
def step_impl(context):
    for i in range(len(context.numbers) - 1):
        assert context.numbers[i] >= context.numbers[i + 1]

@then("the first element should be the largest number")
def step_impl(context):
    assert context.numbers[0] >= context.numbers[-1]

@then("the last element should be the smallest number")
def step_impl(context):
    assert context.numbers[0] <= context.numbers[-1]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers when i sort them then i should get a sorted list and the list should be in descending order and the first element should be the largest number and the last element should be the smallest number ```



```python from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = [1, 5, 8, 3, 6, 9, 2, 7, 4]

@when("i sort them")
def step_impl(context):
    context.numbers.sort(reverse=True)

@then("i should get a sorted list")
def step_impl(context):
    assert sorted(context.numbers, reverse=True) == context.numbers

@then("the list should be in descending order")
def step_impl(context):
    for i in range(len(context.numbers) - 1):
        assert context.numbers[i] >= context.numbers[i + 1]

@then("the first element should be the largest number")
def step_impl(context):
    assert context.numbers[0] >= context.numbers[-1]

@then("the last element should be the smallest number")
def step_impl(context):
    assert context.numbers[0] <= context.numbers[-1]
```

Task: Write a program to find the sum of the digits of a given number.
