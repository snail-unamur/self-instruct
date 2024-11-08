# HQFS163
## Scenario
```gherkin
scenario: 
   given a list of numbers, 
   when i add them up, 
   then the sum should be correct 
   given [1, 2, 3, 4] 
   when i add them up 
   then the sum should be 10
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = [1, 2, 3, 4]

@when("i add them up")
def step_impl(context):
    context.sum = sum(context.numbers)

@then("the sum should be {sum:d}")
def step_impl(context, sum):
    assert context.sum == sum
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when i add them up, then the sum should be correct given [1, 2, 3, 4] when i add them up then the sum should be 10 ```



```python from behave import given, when, then

@given("a list of numbers")
def step_impl(context):
    context.numbers = [1, 2, 3, 4]

@when("i add them up")
def step_impl(context):
    context.sum = sum(context.numbers)

@then("the sum should be {sum:d}")
def step_impl(context, sum):
    assert context.sum == sum
```

Task: Write a program to find the second largest number in a list.
