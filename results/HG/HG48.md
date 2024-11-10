# HQFS48
## Scenario
```gherkin
scenario: 
   given a list of numbers, i want to find the median 
   given a list of numbers: [1, 5, 8, 3, 9, 2] 
   when i find the median of the list 
   then the median should be equal to 4.5
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of numbers: {numbers}")
def step_given_a_list_of_numbers(context, numbers):
    context.numbers = [1, 5, 8, 3, 9, 2]

@when("i find the median of the list")
def step_when_i_find_the_median_of_the_list(context):
    context.median = sorted(context.numbers)[len(context.numbers) // 2]

@then("the median should be equal to {median}")
def step_then_the_median_should_be_equal_to(context, median):
    assert context.median == 4.5
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, i want to find the median given a list of numbers: [1, 5, 8, 3, 9, 2] when i find the median of the list then the median should be equal to 4.5 ``` note: these tasks are for educational purposes only and should not be used for any production code. the step functions are not fully tested and should be adapted to the specific context and requirements of the project.



```python
from behave import given, when, then

@given("a list of numbers: {numbers}")
def step_given_a_list_of_numbers(context, numbers):
    context.numbers = [1, 5, 8, 3, 9, 2]

@when("i find the median of the list")
def step_when_i_find_the_median_of_the_list(context):
    context.median = sorted(context.numbers)[len(context.numbers) // 2]

@then("the median should be equal to {median}")
def step_then_the_median_should_be_equal_to(context, median):
    assert context.median == 4.5
```

Task: Write a program to find the median of a list of numbers.
