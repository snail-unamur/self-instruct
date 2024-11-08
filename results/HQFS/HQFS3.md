# HQFS3
## Scenario
```gherkin
scenario: step with data table 
   given the following data table: |name |age | |alice|30 | |bob |25 | 
   then the data is as expected
```


## Python Implementation
```python
from behave import given, then

@given("the following data table:")
def step_impl(context):
    context.data = []
    for row in context.table:
        context.data.append(dict(row))

@then("the data is as expected")
def step_impl(context):
    for row in context.data:
        assert row["name"]
        assert row["age"]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: step with data table given the following data table: |name |age | |alice|30 | |bob |25 | then the data is as expected ```



```python from behave import given, then

@given("the following data table:")
def step_impl(context):
    context.data = []
    for row in context.table:
        context.data.append(dict(row))

@then("the data is as expected")
def step_impl(context):
    for row in context.data:
        assert row["name"]
        assert row["age"]
```

Task: Write a program to find the sum of the digits of a given number.
