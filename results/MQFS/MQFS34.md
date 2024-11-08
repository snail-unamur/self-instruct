# MQFS34
## Scenario
```gherkin
scenario: 
   given a list of numbers, 
   when i find the median, 
   then the median is correct 
   given a list of numbers: [1, 2, 3, 4, 5] 
   when i find the median 
   then the median is: 3 
   given a list of numbers: [1, 2, 3, 4, 5, 6] 
   when i find the median 
   then the median is: 3.5
```


## Python Implementation
```python
from behave import given, when, then from statistics import median

@given("a list of numbers: {numbers}")
def step_given_a_list_of_numbers(context, numbers):
    context.numbers = [int(x) for x in numbers.split(',')]

@when("i find the median")
def step_when_i_find_the_median(context):
    context.median = median(context.numbers)

@then("the median is: {expected}")
def step_then_the_median_is(context, expected):
    assert context.median == float(expected)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, when i find the median, then the median is correct given a list of numbers: [1, 2, 3, 4, 5] when i find the median then the median is: 3 given a list of numbers: [1, 2, 3, 4, 5, 6] when i find the median then the median is: 3.5 ```



```python from behave import given, when, then from statistics import median

@given("a list of numbers: {numbers}")
def step_given_a_list_of_numbers(context, numbers):
    context.numbers = [int(x) for x in numbers.split(',')]

@when("i find the median")
def step_when_i_find_the_median(context):
    context.median = median(context.numbers)

@then("the median is: {expected}")
def step_then_the_median_is(context, expected):
    assert context.median == float(expected)
```

Task: Write a program to find the sum of the digits of a number.
