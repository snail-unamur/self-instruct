# MQFS145
## Scenario
```gherkin
scenario: user creates a new task 
   given i am a user 
   and i am on the task list page 
   when i click on the "create task" button 
   then i am taken to the "create task" page 
   and i can enter a name for the task 
   and i can enter a description for the task 
   and i can enter a priority for the task 
   and i can enter a due date for the task 
   and i can enter a category for the task 
   and i can save the new task 
   then i am taken back to the task list page 
   and i can see the new task in the list
```


## Python Implementation
```python
from behave import given, when, then

@given("i am a user and i am on the task list page")
def step_impl(context):
    pass

@when("i click on the 'create task' button")
def step_impl(context):
    pass

@then("i am taken to the 'create task' page")
def step_impl(context):
    pass

@then("i can enter a name for the task")
def step_impl(context):
    pass

@then("i can enter a description for the task")
def step_impl(context):
    pass

@then("i can enter a priority for the task")
def step_impl(context):
    pass

@then("i can enter a due date for the task")
def step_impl(context):
    pass

@then("i can enter a category for the task")
def step_impl(context):
    pass

@then("i can save the new task")
def step_impl(context):
    pass

@then("i am taken back to the task list page")
def step_impl(context):
    pass

@then("i can see the new task in the list")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user creates a new task given i am a user and i am on the task list page when i click on the "create task" button then i am taken to the "create task" page and i can enter a name for the task and i can enter a description for the task and i can enter a priority for the task and i can enter a due date for the task and i can enter a category for the task and i can save the new task then i am taken back to the task list page and i can see the new task in the list ```



```python from behave import given, when, then

@given("i am a user and i am on the task list page")
def step_impl(context):
    pass

@when("i click on the 'create task' button")
def step_impl(context):
    pass

@then("i am taken to the 'create task' page")
def step_impl(context):
    pass

@then("i can enter a name for the task")
def step_impl(context):
    pass

@then("i can enter a description for the task")
def step_impl(context):
    pass

@then("i can enter a priority for the task")
def step_impl(context):
    pass

@then("i can enter a due date for the task")
def step_impl(context):
    pass

@then("i can enter a category for the task")
def step_impl(context):
    pass

@then("i can save the new task")
def step_impl(context):
    pass

@then("i am taken back to the task list page")
def step_impl(context):
    pass

@then("i can see the new task in the list")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
