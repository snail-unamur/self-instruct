# MQFS93
## Scenario
```gherkin
scenario: 
   given a string "hello world" 
   when the first character is removed 
   then the resulting string should be "ello world"
```


## Python Implementation
```python
from behave import given, when, then

@given("a string 'hello world'")
def step_given(context):
    context.string = "hello world"

@when("the first character is removed")
def step_when(context):
    context.result = context.string[1:]

@then("the resulting string should be 'ello world'")
def step_then(context):
    assert context.result == "ello world"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a string "hello world" when the first character is removed then the resulting string should be "ello world" ```



```python from behave import given, when, then

@given("a string 'hello world'")
def step_given(context):
    context.string = "hello world"

@when("the first character is removed")
def step_when(context):
    context.result = context.string[1:]

@then("the resulting string should be 'ello world'")
def step_then(context):
    assert context.result == "ello world"
```

Task: Write a program to find the sum of the digits of a given number.
