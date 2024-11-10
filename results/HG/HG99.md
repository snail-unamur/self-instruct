# HQFS99
## Scenario
```gherkin
scenario: a user can add a new task to the task list 
   given i am on the task list page 
   when i add a new task with name "task 1" 
   and i add a new task with name "task 2" 
   then i should see the following tasks on the task list: | task 1 | task 2 |
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the task list page")
def step_given_i_am_on_the_task_list_page(context):
    context.task_list = []

@when("i add a new task with name 'task 1'")
def step_when_i_add_a_new_task_with_name_task_1(context):
    context.task_list.append("task 1")

@when("i add a new task with name 'task 2'")
def step_when_i_add_a_new_task_with_name_task_2(context):
    context.task_list.append("task 2")

@then("i should see the following tasks on the task list:")
def step_then_i_should_see_the_following_tasks_on_the_task_list(context):
    assert context.task_list == ["task 1", "task 2"]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new task to the task list given i am on the task list page when i add a new task with name "task 1" and i add a new task with name "task 2" then i should see the following tasks on the task list: | task 1 | task 2 | ```



```python from behave import given, when, then

@given("i am on the task list page")
def step_given_i_am_on_the_task_list_page(context):
    context.task_list = []

@when("i add a new task with name 'task 1'")
def step_when_i_add_a_new_task_with_name_task_1(context):
    context.task_list.append("task 1")

@when("i add a new task with name 'task 2'")
def step_when_i_add_a_new_task_with_name_task_2(context):
    context.task_list.append("task 2")

@then("i should see the following tasks on the task list:")
def step_then_i_should_see_the_following_tasks_on_the_task_list(context):
    assert context.task_list == ["task 1", "task 2"]
```

Task: Write a program to find the sum of the digits of a given number.
