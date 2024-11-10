# MQFS11
## Scenario
```gherkin
scenario: 
   given a list of integers, 
   when i remove duplicates, 
   then they should be removed 
   given [5, 2, 6, 3, 1, 2, 6] 
   when i remove duplicates 
   then [5, 2, 6, 3, 1]
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of integers")
def step_given_a_list_of_integers(context):
    context.list = [5, 2, 6, 3, 1, 2, 6]

@when("i remove duplicates")
def step_when_i_remove_duplicates(context):
    context.list = list(set(context.list))

@then("they should be removed")
def step_then_they_should_be_removed(context):
    assert context.list == [5, 2, 6, 3, 1]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, when i remove duplicates, then they should be removed given [5, 2, 6, 3, 1, 2, 6] when i remove duplicates then [5, 2, 6, 3, 1] ```



```python from behave import given, when, then

@given("a list of integers")
def step_given_a_list_of_integers(context):
    context.list = [5, 2, 6, 3, 1, 2, 6]

@when("i remove duplicates")
def step_when_i_remove_duplicates(context):
    context.list = list(set(context.list))

@then("they should be removed")
def step_then_they_should_be_removed(context):
    assert context.list == [5, 2, 6, 3, 1]
```

Task: Write a program to find the number of occurrences of a given word in a given string.
