# HQFS79
## Scenario
```gherkin
scenario: adding two matrices 
   given a1 is a matrix of [[1, 2], [3, 4]] 
   and a2 is a matrix of [[5, 6], [7, 8]] 
   then a1 + a2 is a matrix of [[6, 8], [10, 12]]
```


## Python Implementation
```python
from behave import given, when, then

@given("a1 is a matrix of [[1, 2], [3, 4]]")
def step_given_a1_is_a_matrix_of_1_2_3_4(context):
   
    context.a1 = [[1, 2], [3, 4]]

@given("a2 is a matrix of [[5, 6], [7, 8]]")
def step_given_a2_is_a_matrix_of_5_6_7_8(context):   
    context.a2 = [[5, 6], [7, 8]]

@when("a1 + a2 is a matrix of [[6, 8], [10, 12]]")
def step_when_a1_plus_a2_is_a_matrix_of_6_8_10_12(context):
    context.result = [[6, 8], [10, 12]]

@then("the sum of a1 and a2 is correct")
def step_then_the_sum_of_a1_and_and_a2_is_correct(context):
    assert context.result == [[sum(x) for x in zip(context.a1[i], context.a2[i])] for i in range(len(context.a1))]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding two matrices given a1 is a matrix of [[1, 2], [3, 4]] and a2 is a matrix of [[5, 6], [7, 8]] then a1 + a2 is a matrix of [[6, 8], [10, 12]] ```



```python
from behave import given, when, then

@given("a1 is a matrix of [[1, 2], [3, 4]]")
def step_given_a1_is_a_matrix_of_1_2_3_4(context):
   
    context.a1 = [[1, 2], [3, 4]]

@given("a2 is a matrix of [[5, 6], [7, 8]]")
def step_given_a2_is_a_matrix_of_5_6_7_8(context):   
    context.a2 = [[5, 6], [7, 8]]

@when("a1 + a2 is a matrix of [[6, 8], [10, 12]]")
def step_when_a1_plus_a2_is_a_matrix_of_6_8_10_12(context):
    context.result = [[6, 8], [10, 12]]

@then("the sum of a1 and a2 is correct")
def step_then_the_sum_of_a1_and_and_a2_is_correct(context):
    assert context.result == [[sum(x) for x in zip(context.a1[i], context.a2[i])] for i in range(len(context.a1))]
```

Task: Write a program to find the sum of the digits of a number.
