# HQFS162
## Scenario
```gherkin
scenario: 
   given a list of integers, 
   when the list is reduced, 
   then the list is reduced to a single value 
   given a list of integers [4, 1, 3, 2] 
   when the list is reduced with the sum function 
   then the reduced list is 10
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of integers {integers}")
def step_given_a_list_of_integers(context, integers):
    context.list = [int(i) for i in integers.split(",")]

@when("the list is reduced with the sum function")
def step_when_the_list_is_reduced_with_the_sum_function(context):
    context.reduced_list = sum(context.list)

@then("the reduced list is {reduced_list}")
def step_then_the_reduced_list_is(context, reduced_list):
    assert context.reduced_list == int(reduced_list)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, when the list is reduced, then the list is reduced to a single value given a list of integers [4, 1, 3, 2] when the list is reduced with the sum function then the reduced list is 10 ```



```python from behave import given, when, then

@given("a list of integers {integers}")
def step_given_a_list_of_integers(context, integers):
    context.list = [int(i) for i in integers.split(",")]

@when("the list is reduced with the sum function")
def step_when_the_list_is_reduced_with_the_sum_function(context):
    context.reduced_list = sum(context.list)

@then("the reduced list is {reduced_list}")
def step_then_the_reduced_list_is(context, reduced_list):
    assert context.reduced_list == int(reduced_list)
```

Task: Write a program to find the number of occurrences of a given word in a given string.
