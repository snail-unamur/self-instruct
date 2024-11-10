# MQFS53
## Scenario
```gherkin
scenario: 
   given a set of integers, find the largest 
   and smallest integers 
   given a set of integers {1, 2, 3, 4, 5} 
   when i find the largest integer 
   then i should get 5 
   when i find the smallest integer 
   then i should get 1
```


## Python Implementation
```python
from behave import given, when, then

@given("a set of integers {integers}")
def step_given_a_set_of_integers(context, integers):
    context.numbers = [int(i) for i in integers.split(',')]

@when("i find the largest integer")
def step_when_i_find_the_largest_integer(context):
    context.largest = max(context.numbers)

@then("i should get {expected}")
def step_then_i_should_get(context, expected):
    assert context.largest == int(expected)

@when("i find the smallest integer")
def step_when_i_find_the_smallest_integer(context):
    context.smallest = min(context.numbers)

@then("i should get {expected}")
def step_then_i_should_get_1(context, expected):
    assert context.smallest == int(expected)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a set of integers, find the largest and smallest integers given a set of integers {1, 2, 3, 4, 5} when i find the largest integer then i should get 5 when i find the smallest integer then i should get 1 ```



```python from behave import given, when, then

@given("a set of integers {integers}")
def step_given_a_set_of_integers(context, integers):
    context.numbers = [int(i) for i in integers.split(',')]

@when("i find the largest integer")
def step_when_i_find_the_largest_integer(context):
    context.largest = max(context.numbers)

@then("i should get {expected}")
def step_then_i_should_get(context, expected):
    assert context.largest == int(expected)

@when("i find the smallest integer")
def step_when_i_find_the_smallest_integer(context):
    context.smallest = min(context.numbers)

@then("i should get {expected}")
def step_then_i_should_get_1(context, expected):
    assert context.smallest == int(expected)
```

Task: Write a program to find the sum of the digits of a given number.
