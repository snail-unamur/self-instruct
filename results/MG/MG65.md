# MQFS65
## Scenario
```gherkin
scenario: testing the edit functionality 
   given a user with username "testuser" 
   and a task with id "123" 
   when the user edits the task 
   then the task is updated in the system
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with username 'testuser'")
def step_given_a_user_with_username_testuser(context):
    context.user = User("testuser")

@given("a task with id '123'")
def step_given_a_task_with_id_123(context):
    context.task = Task("123")

@when("the user edits the task")
def step_when_the_user_edits_the_task(context):
    context.task.edit(context.user)

@then("the task is updated in the system")
def step_then_the_task_is_updated_in_the_system(context):
    assert context.task.is_updated
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit functionality given a user with username "testuser" and a task with id "123" when the user edits the task then the task is updated in the system ```



```python from behave import given, when, then

@given("a user with username 'testuser'")
def step_given_a_user_with_username_testuser(context):
    context.user = User("testuser")

@given("a task with id '123'")
def step_given_a_task_with_id_123(context):
    context.task = Task("123")

@when("the user edits the task")
def step_when_the_user_edits_the_task(context):
    context.task.edit(context.user)

@then("the task is updated in the system")
def step_then_the_task_is_updated_in_the_system(context):
    assert context.task.is_updated
```

Task: Write a program to find the sum of the digits of a given number.
