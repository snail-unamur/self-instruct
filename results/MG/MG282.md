# MQFS282
## Scenario
```gherkin
scenario: 
   given i have a list of numbers 
   when i sum the numbers 
   then i get the correct sum 
   given i have a list of numbers [1, 2, 3, 4, 5] 
   when i sum the numbers 
   then i get 15 
   given i have a list of numbers [0, -1, 2, -3, 4] 
   when i sum the numbers 
   then i get 2 
   given i have a list of numbers [1.5, 2.2, 3.3, 4.4] 
   when i sum the numbers 
   then i get 11.4
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a list of numbers {numbers}")
def step_impl(context, numbers):
    context.numbers = [float(i) for i in numbers.split(",")]

@when("i sum the numbers")
def step_impl(context):
    context.sum = sum(context.numbers)

@then("i get the correct sum {expected_sum}")
def step_impl(context, expected_sum):
    assert context.sum == float(expected_sum), f"Expected sum {expected_sum} but got {context.sum}"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of numbers when i sum the numbers then i get the correct sum given i have a list of numbers [1, 2, 3, 4, 5] when i sum the numbers then i get 15 given i have a list of numbers [0, -1, 2, -3, 4] when i sum the numbers then i get 2 given i have a list of numbers [1.5, 2.2, 3.3, 4.4] when i sum the numbers then i get 11.4 ```



```python from behave import given, when, then

@given("i have a list of numbers {numbers}")
def step_impl(context, numbers):
    context.numbers = [float(i) for i in numbers.split(",")]

@when("i sum the numbers")
def step_impl(context):
    context.sum = sum(context.numbers)

@then("i get the correct sum {expected_sum}")
def step_impl(context, expected_sum):
    assert context.sum == float(expected_sum), f"Expected sum {expected_sum} but got {context.sum}"
```

Task: Write a program to find the sum of the digits of a given number.
