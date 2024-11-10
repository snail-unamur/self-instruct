# MQFS4
## Scenario
```gherkin
scenario: test the add 
   and remove functionality of the to-do list 
   given i am on the to-do list page 
   when i add a new task "buy groceries" 
   then i should see the task "buy groceries" on the to-do list 
   when i remove the task "buy groceries" 
   then i should not see the task "buy groceries" on the to-do list
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the to-do list page")
def step_given_i_am_on_the_to_do_list_page(context):
    context.todo_list = []

@when("i add a new task {task}")
def step_when_i_add_a_new_task(context, task):
    context.todo_list.append(task)

@then("i should see the task {task} on the to-do list")
def step_then_i_should_see_the_task_on_the_to_do_list(context, task):
    assert task in context.todo_list

@when("i remove the task {task}")
def step_when_i_remove_the_task(context, task):
    context.todo_list.remove(task)

@then("i should not see the task {task} on the to-do list")
def step_then_i_should_not_see_the_task_on_the_to_do_list(context, task):
    assert task not in context.todo_list
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: test the add and remove functionality of the to-do list given i am on the to-do list page when i add a new task "buy groceries" then i should see the task "buy groceries" on the to-do list when i remove the task "buy groceries" then i should not see the task "buy groceries" on the to-do list ```



```python from behave import given, when, then

@given("i am on the to-do list page")
def step_given_i_am_on_the_to_do_list_page(context):
    context.todo_list = []

@when("i add a new task {task}")
def step_when_i_add_a_new_task(context, task):
    context.todo_list.append(task)

@then("i should see the task {task} on the to-do list")
def step_then_i_should_see_the_task_on_the_to_do_list(context, task):
    assert task in context.todo_list

@when("i remove the task {task}")
def step_when_i_remove_the_task(context, task):
    context.todo_list.remove(task)

@then("i should not see the task {task} on the to-do list")
def step_then_i_should_not_see_the_task_on_the_to_do_list(context, task):
    assert task not in context.todo_list
```

Task: Write a program to find the sum of the digits of a given number.
