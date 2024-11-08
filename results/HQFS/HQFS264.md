# HQFS264
## Scenario
```gherkin
scenario: 
   given a list of integers, 
   when the first element is removed, 
   then the resulting list should not contain the first element 
   given a list of integers [5, 2, 8, 1, 4] 
   when the first element is removed 
   then the resulting list should not contain the first element
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of integers {list}")
def step_given_a_list_of_integers(context, list):
    context.list = [5, 2, 8, 1, 4]

@when("the first element is removed")
def step_when_the_first_element_is_removed(context):
    context.resulting_list = context.list.pop(0)

@then("the resulting list should not contain the first element")
def step_then_the_resulting_list_should_not_contain_the_first_element(context):
    assert context.resulting_list not in context.list
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of integers, when the first element is removed, then the resulting list should not contain the first element given a list of integers [5, 2, 8, 1, 4] when the first element is removed then the resulting list should not contain the first element ```



```python from behave import given, when, then

@given("a list of integers {list}")
def step_given_a_list_of_integers(context, list):
    context.list = [5, 2, 8, 1, 4]

@when("the first element is removed")
def step_when_the_first_element_is_removed(context):
    context.resulting_list = context.list.pop(0)

@then("the resulting list should not contain the first element")
def step_then_the_resulting_list_should_not_contain_the_first_element(context):
    assert context.resulting_list not in context.list
```

Task: Write a program to find the second largest number in a list.
