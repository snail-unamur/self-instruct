# HQFS273
## Scenario
```gherkin
scenario: 
   given a list of integers, i want to find the first number that appears more than once 
   given [1, 2, 3, 1] 
   then the first number that appears more than once is 1
```


## Python Implementation
```python
from behave import given, when, then

@given('a list of integers')
def step_given_a_list_of_integers(context):
    context.list_of_integers = [1, 2, 3, 1]

@when('i want to find the first number that appears more than once')
def step_when_i_want_to_find_the_first_number_that_appears_more_than_once(context):
    context.first_number_that_appears_more_than_once = next((i for i in context.list_of_integers if context.list_of_integers.count(i) > 1), None)

@then('the first number that appears more than once is {number:d}')
def step_then_the_first_number_that_appears_more_than_once_is_number(context, number):
    assert context.first_number_that_appears_more_than_once == number
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, i want to find the first number that appears more than once given [1, 2, 3, 1] then the first number that appears more than once is 1 ``` note: these tasks are designed to be solved using the behave bdd testing framework and python. the goal is to implement the step functions for each gherkin scenario provided. the step functions should perform the necessary actions to fulfill the requirements of each scenario. it is assumed that the necessary dependencies are installed and that the necessary boilerplate code for a behave project is in place.



```python from behave import given, when, then

@given('a list of integers')
def step_given_a_list_of_integers(context):
    context.list_of_integers = [1, 2, 3, 1]

@when('i want to find the first number that appears more than once')
def step_when_i_want_to_find_the_first_number_that_appears_more_than_once(context):
    context.first_number_that_appears_more_than_once = next((i for i in context.list_of_integers if context.list_of_integers.count(i) > 1), None)

@then('the first number that appears more than once is {number:d}')
def step_then_the_first_number_that_appears_more_than_once_is_number(context, number):
    assert context.first_number_that_appears_more_than_once == number
```

Task: Given a list of integers, find the first number that appears more than once.
