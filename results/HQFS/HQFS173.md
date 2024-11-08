# HQFS173
## Scenario
```gherkin
scenario: 
   given a list of integers, 
   when i find the median, 
   then the median is the middle value of the sorted list 
   given a list of integers [1, 3, 5, 7, 9] 
   when i find the median 
   then the median is 5 
   given a list of integers [1, 3, 5, 7, 9, 11] 
   when i find the median 
   then the median is 6 
   given a list of integers [1, 3, 5, 7, 9, 11, 13] 
   when i find the median 
   then the median is 7
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of integers {list}")
def step_given_a_list_of_integers(context, list):
    context.numbers = [int(i) for i in list.split(',')]

@when("i find the median")
def step_when_i_find_the_median(context):
    context.median = sorted(context.numbers)[len(context.numbers) // 2]

@then("the median is {median}")
def step_then_the_median_is(context, median):
    assert context.median == int(median)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, when i find the median, then the median is the middle value of the sorted list given a list of integers [1, 3, 5, 7, 9] when i find the median then the median is 5 given a list of integers [1, 3, 5, 7, 9, 11] when i find the median then the median is 6 given a list of integers [1, 3, 5, 7, 9, 11, 13] when i find the median then the median is 7 ```



```python from behave import given, when, then

@given("a list of integers {list}")
def step_given_a_list_of_integers(context, list):
    context.numbers = [int(i) for i in list.split(',')]

@when("i find the median")
def step_when_i_find_the_median(context):
    context.median = sorted(context.numbers)[len(context.numbers) // 2]

@then("the median is {median}")
def step_then_the_median_is(context, median):
    assert context.median == int(median)
```

Task: Write a program to find the sum of the digits of a given number.
