# MQFS246
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: step with a table given some initial data |name |department | |barry |beer cans | |pudey |silly walks| |two-lumps|silly walks| then we will have the expected data |name |department | |barry |beer cans | |pudey |silly walks| |two-lumps|silly walks| |name |department | |barry |beer cans | |pudey |silly walks| |two-lumps|silly walks| |name |department | |barry |beer cans | |pudey |silly walks| |two-lumps|silly walks| |name |department | |barry |beer cans | |pudey |silly walks| |two-lumps|silly



from behave import given, then

@given("some initial data")
def step(context):
    context.data = [
        {"name": "barry", "department": "beer cans"},
        {"name": "pudey", "department": "silly walks"},
        {"name": "two-lumps", "department": "silly walks"},
    ]

@then("we will have the expected data")
def step(context):
    assert context.data == [
        {"name": "barry", "department": "beer cans"},
        {"name": "pudey", "department": "silly walks"},
        {"name": "two-lumps", "department": "silly walks"},
    ]

@then("we will have the expected data after adding more data")
def step(context):
    context.data.extend([
        {"name": "barry", "department": "beer cans"},
        {"name": "pudey", "department": "silly walks"},
        {"name": "two-lumps", "department": "silly walks"},
        {"name": "barry", "department": "beer cans"},
        {"name": "pudey", "department": "silly walks"},
        {"name": "two-lumps", "department": "silly walks"},
        {"name": "barry", "department": "beer cans"},
        {"name": "pudey", "department": "silly walks"},
        {"name": "two-lumps", "department": "silly walks"},
    ])
    assert context.data == [
        {"name": "barry", "department": "beer cans"},
        {"name": "pudey", "department": "silly walks"},
        {"name": "two-lumps", "department": "silly walks"},
        {"name": "barry", "department": "beer cans"},
        {"name": "pudey", "department": "silly walks"},
