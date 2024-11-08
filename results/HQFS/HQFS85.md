# HQFS85
## Scenario
```gherkin
scenario: 
   given a set of specific users: 
   and we have the following people in "beer cans": |name | |alice | |bob | 
   and we have the following people in "silly walks": |name | |charly| |dodo | 
   then the set of specific users should be: |name |department | |alice |beer cans | |bob |beer cans | |charly|silly walks| |dodo |silly walks|
```


## Python Implementation
```python
from behave import given, then

@given("a set of specific users")
def step_impl(context):
    context.users = []

@given("we have the following people in \"beer cans\"")
def step_impl(context):
    context.beer_cans = ["alice", "bob"]

@given("we have the following people in \"silly walks\"")
def step_impl(context):
    context.silly_walks = ["charly", "dodo"]

@then("the set of specific users should be")
def step_impl(context):
    for user in context.beer_cans:
        context.users.append({"name": user, "department": "beer cans"})
    for user in context.silly_walks:
        context.users.append({"name": user, "department": "silly walks"})
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a set of specific users: and we have the following people in "beer cans": |name | |alice | |bob | and we have the following people in "silly walks": |name | |charly| |dodo | then the set of specific users should be: |name |department | |alice |beer cans | |bob |beer cans | |charly|silly walks| |dodo |silly walks| ```



```python from behave import given, then

@given("a set of specific users")
def step_impl(context):
    context.users = []

@given("we have the following people in \"beer cans\"")
def step_impl(context):
    context.beer_cans = ["alice", "bob"]

@given("we have the following people in \"silly walks\"")
def step_impl(context):
    context.silly_walks = ["charly", "dodo"]

@then("the set of specific users should be")
def step_impl(context):
    for user in context.beer_cans:
        context.users.append({"name": user, "department": "beer cans"})
    for user in context.silly_walks:
        context.users.append({"name": user, "department": "silly walks"})
```

Task: Write a program to find the sum of the digits of a given number.
