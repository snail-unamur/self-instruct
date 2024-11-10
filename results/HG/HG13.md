# HQFS13
## Scenario
```gherkin
scenario: adding a new task to the to-do list 
   given a to-do list with the following tasks: |title |description |due date | |----- |----------- |--------- | |task 1 |task 1 description |2023-02-01 | |task 2 |task 2 description |2023-02-02 | 
   when a new task is added with the following details: |title |description |due date | |----- |----------- |--------- | |task 3 |task 3 description |2023-02-03 | 
   then the to-do list should contain the following tasks: |title |description |due date | |----- |----------- |--------- | |task 1 |task 1 description |2023-02-01 | |task 2 |task 2 description |2023-02-02 | |task 3 |task 3 description |2023-02-03 |
```


## Python Implementation
```python
from behave import given, when, then

@given("a to-do list with the following tasks:")
def step_impl(context):
    context.tasks = [
        {"title": "task 1", "description": "task 1 description", "due_date": "2023-02-01"},
        {"title": "task 2", "description": "task 2 description", "due_date": "2023-02-02"}
    ]

@when("a new task is added with the following details:")
def step_impl(context, title, description, due_date):
    context.new_task = {"title": title, "description": description, "due_date": due_date}
    context.tasks.append(context.new_task)

@then("the to-do list should contain the following tasks:")
def step_impl(context, title, description, due_date):
    assert context.tasks == [
        {"title": "task 1", "description": "task 1 description", "due_date": "2023-02-01"},
        {"title": "task 2", "description": "task 2 description", "due_date": "2023-02-02"},
        {"title": title, "description": description, "due_date": due_date}
    ]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new task to the to-do list given a to-do list with the following tasks: |title |description |due date | |----- |----------- |--------- | |task 1 |task 1 description |2023-02-01 | |task 2 |task 2 description |2023-02-02 | when a new task is added with the following details: |title |description |due date | |----- |----------- |--------- | |task 3 |task 3 description |2023-02-03 | then the to-do list should contain the following tasks: |title |description |due date | |----- |----------- |--------- | |task 1 |task 1 description |2023-02-01 | |task 2 |task 2 description |2023-02-02 | |task 3 |task 3 description |2023-02-03 | ```



```python from behave import given, when, then

@given("a to-do list with the following tasks:")
def step_impl(context):
    context.tasks = [
        {"title": "task 1", "description": "task 1 description", "due_date": "2023-02-01"},
        {"title": "task 2", "description": "task 2 description", "due_date": "2023-02-02"}
    ]

@when("a new task is added with the following details:")
def step_impl(context, title, description, due_date):
    context.new_task = {"title": title, "description": description, "due_date": due_date}
    context.tasks.append(context.new_task)

@then("the to-do list should contain the following tasks:")
def step_impl(context, title, description, due_date):
    assert context.tasks == [
        {"title": "task 1", "description": "task 1 description", "due_date": "2023-02-01"},
        {"title": "task 2", "description": "task 2 description", "due_date": "2023-02-02"},
        {"title": title, "description": description, "due_date": due_date}
    ]
```

Task: Write a program to find the sum of the digits of a number.
