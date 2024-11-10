# MQFS52
## Scenario
```gherkin
scenario: user can mark a task as complete 
   given user is logged in 
   when user navigates to their task list page 
   then user can mark a task as complete 
   when user confirms the completion 
   then the task is marked as complete on the user's task list
```


## Python Implementation
```python
from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user navigates to their task list page")
def step_impl(context):
    context.task_list_page = TaskListPage(context.user)
    context.task_list_page.load()

@when("user marks a task as complete")
def step_impl(context):
    context.task = context.task_list_page.get_random_task()
    context.task.mark_complete()

@when("user confirms the completion")
def step_impl(context):
    context.task.confirm_completion()

@then("the task is marked as complete on the user's task list")
def step_impl(context):
    assert context.task.is_complete()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can mark a task as complete given user is logged in when user navigates to their task list page then user can mark a task as complete when user confirms the completion then the task is marked as complete on the user's task list ```



```python from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user navigates to their task list page")
def step_impl(context):
    context.task_list_page = TaskListPage(context.user)
    context.task_list_page.load()

@when("user marks a task as complete")
def step_impl(context):
    context.task = context.task_list_page.get_random_task()
    context.task.mark_complete()

@when("user confirms the completion")
def step_impl(context):
    context.task.confirm_completion()

@then("the task is marked as complete on the user's task list")
def step_impl(context):
    assert context.task.is_complete()
```

Task: Write a program to find the sum of the digits of a number.
