# MQFS141
## Scenario
```gherkin
scenario: 
   given i have a list of users 
   when i filter the list by age 
   then i only see users with the specified age 
   when i filter the list by name 
   then i only see users with the specified name in their name
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a list of users")
def step_impl(context):
    context.users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 25},
        {"name": "David", "age": 35},
    ]

@when("i filter the list by age")
def step_impl(context):
    age = int(context.text)
    context.filtered_users = [
        user for user in context.users if user["age"] == age
    ]

@then("i only see users with the specified age")
def step_impl(context):
    assert all(user["age"] == int(context.text) for user in context.filtered_users)

@when("i filter the list by name")
def step_impl(context):
    name = context.text
    context.filtered_users = [
        user for user in context.users if name.lower() in user["name"].lower()
    ]

@then("i only see users with the specified name in their name")
def step_impl(context):
    assert all(name.lower() in user["name"].lower() for user in context.filtered_users)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a list of users when i filter the list by age then i only see users with the specified age when i filter the list by name then i only see users with the specified name in their name ```



```python from behave import given, when, then

@given("i have a list of users")
def step_impl(context):
    context.users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 25},
        {"name": "David", "age": 35},
    ]

@when("i filter the list by age")
def step_impl(context):
    age = int(context.text)
    context.filtered_users = [
        user for user in context.users if user["age"] == age
    ]

@then("i only see users with the specified age")
def step_impl(context):
    assert all(user["age"] == int(context.text) for user in context.filtered_users)

@when("i filter the list by name")
def step_impl(context):
    name = context.text
    context.filtered_users = [
        user for user in context.users if name.lower() in user["name"].lower()
    ]

@then("i only see users with the specified name in their name")
def step_impl(context):
    assert all(name.lower() in user["name"].lower() for user in context.filtered_users)
```

Task: Write a program to find the sum of the digits of a number.
