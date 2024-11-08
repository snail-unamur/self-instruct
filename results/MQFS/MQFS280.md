# MQFS280
## Scenario
```gherkin
scenario: 
   given a user has a list of tasks 
   when the user marks a task as incomplete 
   then the task should be moved back to the list of tasks 
   and the task should be marked as incomplete
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has a list of tasks")
def step_given_a_user_has_a_list_of_tasks(context):
    context.tasks = ["Task 1", "Task 2", "Task 3"]
    context.completed_tasks = ["Task 1"]

@when("the user marks a task as incomplete")
def step_when_the_user_marks_a_task_as_incomplete(context):
    task_to_mark_incomplete = "Task 2"
    context.tasks.append(task_to_mark_incomplete)
    context.tasks.remove(task_to_mark_incomplete)
    context.completed_tasks.remove(task_to_mark_incomplete)

@then("the task should be moved back to the list of tasks")
def step_then_the_task_should_be_moved_back_to_the_list_of_tasks(context):
    assert "Task 2" in context.tasks

@then("the task should be marked as incomplete")
def step_then_the_task_should_be_marked_as_incomplete(context):
    assert "Task 2" not in context.completed_tasks
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has a list of tasks when the user marks a task as incomplete then the task should be moved back to the list of tasks and the task should be marked as incomplete ```



```python from behave import given, when, then

@given("a user has a list of tasks")
def step_given_a_user_has_a_list_of_tasks(context):
    context.tasks = ["Task 1", "Task 2", "Task 3"]
    context.completed_tasks = ["Task 1"]

@when("the user marks a task as incomplete")
def step_when_the_user_marks_a_task_as_incomplete(context):
    task_to_mark_incomplete = "Task 2"
    context.tasks.append(task_to_mark_incomplete)
    context.tasks.remove(task_to_mark_incomplete)
    context.completed_tasks.remove(task_to_mark_incomplete)

@then("the task should be moved back to the list of tasks")
def step_then_the_task_should_be_moved_back_to_the_list_of_tasks(context):
    assert "Task 2" in context.tasks

@then("the task should be marked as incomplete")
def step_then_the_task_should_be_marked_as_incomplete(context):
    assert "Task 2" not in context.completed_tasks
```

Task: Write a program to find the sum of the digits of a number.
