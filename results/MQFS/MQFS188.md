# MQFS188
## Scenario
```gherkin
scenario: 
   given a list of integers, 
   when i sum the list, 
   then the sum should be the expected sum 
   given a list of integers [1, 2, 3] 
   when i sum the list 
   then the sum should be 6
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of integers {list}")
def step_given_a_list_of_integers(context, list):
    context.list = [int(i) for i in list.split(',')]

@when("i sum the list")
def step_when_i_sum_the_list(context):
    context.sum = sum(context.list)

@then("the sum should be {expected_sum}")
def step_then_the_sum_should_be(context, expected_sum):
    assert context.sum == int(expected_sum)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, when i sum the list, then the sum should be the expected sum given a list of integers [1, 2, 3] when i sum the list then the sum should be 6 ```



```python from behave import given, when, then

@given("a list of integers {list}")
def step_given_a_list_of_integers(context, list):
    context.list = [int(i) for i in list.split(',')]

@when("i sum the list")
def step_when_i_sum_the_list(context):
    context.sum = sum(context.list)

@then("the sum should be {expected_sum}")
def step_then_the_sum_should_be(context, expected_sum):
    assert context.sum == int(expected_sum)
```

Task: Write a program to find the number of days in a given month and year.
