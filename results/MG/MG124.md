# MQFS124
## Scenario
```gherkin
scenario: testing the functionality of a simple to-do list 
   given a to-do list object with the following tasks: | task | description | due date | completed | | --- | --- | --- | --- | | task 1 | task 1 description | 2023-03-01 | false | | task 2 | task 2 description | 2023-03-02 | true | 
   when i mark task 1 as completed 
   then the completed status of task 1 should be true 
   and the to-do list should contain the following tasks: | task | description | due date | completed | | --- | --- | --- | --- | | task 1 | task 1 description | 2023-03-01 | true | | task 2 | task 2 description | 2023-03-02 | true |
```


## Python Implementation
```python
from behave import given, when, then

@given("a to-do list object with the following tasks:")
def step_impl(context):
    context.tasks = [
        {"task": "task 1", "description": "task 1 description", "due_date": "2023-03-01", "completed": False},
        {"task": "task 2", "description": "task 2 description", "due_date": "2023-03-02", "completed": True},
    ]
    context.to_do_list = ToDoList(context.tasks)

@when("i mark task 1 as completed")
def step_impl(context):
    context.to_do_list.mark_completed("task 1")

@then("the completed status of task 1 should be true")
def step_impl(context):
    assert context.to_do_list.tasks[0]["completed"] is True

@then("the to-do list should contain the following tasks:")
def step_impl(context):
    expected_tasks = [
        {"task": "task 1", "description": "task 1 description", "due_date": "2023-03-01", "completed": True},
        {"task": "task 2", "description": "task 2 description", "due_date": "2023-03-02", "completed": True},
    ]
    assert context.to_do_list.tasks == expected_tasks
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of a simple to-do list given a to-do list object with the following tasks: | task | description | due date | completed | | --- | --- | --- | --- | | task 1 | task 1 description | 2023-03-01 | false | | task 2 | task 2 description | 2023-03-02 | true | when i mark task 1 as completed then the completed status of task 1 should be true and the to-do list should contain the following tasks: | task | description | due date | completed | | --- | --- | --- | --- | | task 1 | task 1 description | 2023-03-01 | true | | task 2 | task 2 description | 2023-03-02 | true | ```



```python from behave import given, when, then

@given("a to-do list object with the following tasks:")
def step_impl(context):
    context.tasks = [
        {"task": "task 1", "description": "task 1 description", "due_date": "2023-03-01", "completed": False},
        {"task": "task 2", "description": "task 2 description", "due_date": "2023-03-02", "completed": True},
    ]
    context.to_do_list = ToDoList(context.tasks)

@when("i mark task 1 as completed")
def step_impl(context):
    context.to_do_list.mark_completed("task 1")

@then("the completed status of task 1 should be true")
def step_impl(context):
    assert context.to_do_list.tasks[0]["completed"] is True

@then("the to-do list should contain the following tasks:")
def step_impl(context):
    expected_tasks = [
        {"task": "task 1", "description": "task 1 description", "due_date": "2023-03-01", "completed": True},
        {"task": "task 2", "description": "task 2 description", "due_date": "2023-03-02", "completed": True},
    ]
    assert context.to_do_list.tasks == expected_tasks
```

Task: Write a program to find the sum of the digits of a number.
