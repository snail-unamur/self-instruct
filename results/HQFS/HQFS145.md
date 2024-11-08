# HQFS145
## Scenario
```gherkin
scenario: 
   given a list of integers, 
   when i sort them in ascending order, 
   then the result is the sorted list of integers 
   given a list of integers [4, 3, 2, 1] 
   when i sort them in ascending order 
   then the result is [1, 2, 3, 4]
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of integers {integers}")
def step(context, integers):
    context.numbers = [int(i) for i in integers.split(",")]

@when("i sort them in ascending order")
def step(context):
    context.numbers.sort()

@then("the result is the sorted list of integers {integers}")
def step(context, integers):
    assert context.numbers == [int(i) for i in integers.split(",")]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, when i sort them in ascending order, then the result is the sorted list of integers given a list of integers [4, 3, 2, 1] when i sort them in ascending order then the result is [1, 2, 3, 4] ```



```python from behave import given, when, then

@given("a list of integers {integers}")
def step(context, integers):
    context.numbers = [int(i) for i in integers.split(",")]

@when("i sort them in ascending order")
def step(context):
    context.numbers.sort()

@then("the result is the sorted list of integers {integers}")
def step(context, integers):
    assert context.numbers == [int(i) for i in integers.split(",")]
```

Task: Write a program to find the number of days in a given month.
