# HQFS32
## Scenario
```gherkin
scenario: 
   given i have a list of integers 
   when i sum them 
   then i should get the correct sum 
   given i have a list of integers [1, 2, 3, 4, 5] 
   when i sum them 
   then i should get 15 
   given i have a list of integers [1, -2, 3, -4, 5] 
   when i sum them 
   then i should get 3 
   given i have a list of integers [] 
   when i sum them 
   then i should get 0
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a list of integers {list}")
def step_given_i_have_a_list_of_integers(context, list):
    context.list = [int(i) for i in list.split(',')]

@when("i sum them")
def step_when_i_sum_them(context):
    context.sum = sum(context.list)

@then("i should get the correct sum {sum}")
def step_then_i_should_get_the_correct_sum(context, sum):
    assert context.sum == int(sum)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of integers when i sum them then i should get the correct sum given i have a list of integers [1, 2, 3, 4, 5] when i sum them then i should get 15 given i have a list of integers [1, -2, 3, -4, 5] when i sum them then i should get 3 given i have a list of integers [] when i sum them then i should get 0 ```



```python from behave import given, when, then

@given("i have a list of integers {list}")
def step_given_i_have_a_list_of_integers(context, list):
    context.list = [int(i) for i in list.split(',')]

@when("i sum them")
def step_when_i_sum_them(context):
    context.sum = sum(context.list)

@then("i should get the correct sum {sum}")
def step_then_i_should_get_the_correct_sum(context, sum):
    assert context.sum == int(sum)
```

Task: Write a program to find the second largest number in a list.
