# HQFS207
## Scenario
```gherkin
scenario: 
   given a user with name "john" 
   and age 20 
   when i check if the user is an adult 
   then i should get "john is an adult"
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with name 'john' and age 20")
def step_impl(context):
    context.user = {"name": "john", "age": 20}

@when("i check if the user is an adult")
def step_impl(context):
    if context.user["age"] >= 18:
        context.result = f"{context.user['name']} is an adult"
    else:
        context.result = f"{context.user['name']} is not an adult"

@then("i should get 'john is an adult'")
def step_impl(context):
    assert context.result == "john is an adult"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user with name "john" and age 20 when i check if the user is an adult then i should get "john is an adult" ```



```python from behave import given, when, then

@given("a user with name 'john' and age 20")
def step_impl(context):
    context.user = {"name": "john", "age": 20}

@when("i check if the user is an adult")
def step_impl(context):
    if context.user["age"] >= 18:
        context.result = f"{context.user['name']} is an adult"
    else:
        context.result = f"{context.user['name']} is not an adult"

@then("i should get 'john is an adult'")
def step_impl(context):
    assert context.result == "john is an adult"
```

Task: Write a program to find the sum of the digits of a given number.
