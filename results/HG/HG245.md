# HQFS245
## Scenario
```gherkin
scenario: 
   given a list of dictionaries, 
   when i sort them by a specific key, 
   then the list should be sorted by that key 
   given a list of dictionaries: [{"name": "john", "age": 25}, {"name": "jane", "age": 30}, {"name": "jack", "age": 20}] 
   when i sort the list by the "age" key 
   then the sorted list should be: [{"name": "jack", "age": 20}, {"name": "john", "age": 25}, {"name": "jane", "age": 30}]
```


## Python Implementation
```python
from behave import given, when, then

@given("a list of dictionaries: {list}")
def step_impl(context, list):
    context.list = eval(list)

@when("i sort the list by the {key} key")
def step_impl(context, key):
    context.list.sort(key=lambda x: x[key])

@then("the sorted list should be: {list}")
def step_impl(context, list):
    assert context.list == eval(list)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of dictionaries, when i sort them by a specific key, then the list should be sorted by that key given a list of dictionaries: [{"name": "john", "age": 25}, {"name": "jane", "age": 30}, {"name": "jack", "age": 20}] when i sort the list by the "age" key then the sorted list should be: [{"name": "jack", "age": 20}, {"name": "john", "age": 25}, {"name": "jane", "age": 30}] ```



```python from behave import given, when, then

@given("a list of dictionaries: {list}")
def step_impl(context, list):
    context.list = eval(list)

@when("i sort the list by the {key} key")
def step_impl(context, key):
    context.list.sort(key=lambda x: x[key])

@then("the sorted list should be: {list}")
def step_impl(context, list):
    assert context.list == eval(list)
```

Task: Write a program to find the second largest number in a list.
