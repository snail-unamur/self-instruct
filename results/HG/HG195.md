# HQFS195
## Scenario
```gherkin
scenario: checking the status of a flight 
   given a flight with a status of "on-time" 
   when we check the status of the flight 
   then the status of the flight should be "on-time"
```


## Python Implementation
```python
from behave import given, when, then

@given("a flight with a status of 'on-time'")
def step_impl(context):
    context.flight = {"status": "on-time"}

@when("we check the status of the flight")
def step_impl(context):
    context.status = context.flight["status"]

@then("the status of the flight should be 'on-time'")
def step_impl(context):
    assert context.status == "on-time"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking the status of a flight given a flight with a status of "on-time" when we check the status of the flight then the status of the flight should be "on-time" ```



```python from behave import given, when, then

@given("a flight with a status of 'on-time'")
def step_impl(context):
    context.flight = {"status": "on-time"}

@when("we check the status of the flight")
def step_impl(context):
    context.status = context.flight["status"]

@then("the status of the flight should be 'on-time'")
def step_impl(context):
    assert context.status == "on-time"
```

Task: Write a program to find the sum of the digits of a given number.
