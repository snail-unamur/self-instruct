# MQFS204
## Scenario
```gherkin
scenario: 
   given i have a list of numbers [1, 2, 3, 4, 5] 
   when i insert 0 at index 0 
   then the element at index 0 is 0 
   and the length of the list is 6
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a list of numbers {numbers}")
def step_given(context, numbers):
    context.numbers = [int(i) for i in numbers.split(',')]

@when("i insert 0 at index 0")
def step_when(context):
    context.numbers.insert(0, 0)

@then("the element at index 0 is 0")
def step_then(context):
    assert context.numbers[0] == 0

@then("the length of the list is 6")
def step_then(context):
    assert len(context.numbers) == 6
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of numbers [1, 2, 3, 4, 5] when i insert 0 at index 0 then the element at index 0 is 0 and the length of the list is 6 ```



```python from behave import given, when, then

@given("i have a list of numbers {numbers}")
def step_given(context, numbers):
    context.numbers = [int(i) for i in numbers.split(',')]

@when("i insert 0 at index 0")
def step_when(context):
    context.numbers.insert(0, 0)

@then("the element at index 0 is 0")
def step_then(context):
    assert context.numbers[0] == 0

@then("the length of the list is 6")
def step_then(context):
    assert len(context.numbers) == 6
```

Task: Write a program to find the sum of the digits of a number.
