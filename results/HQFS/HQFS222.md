# HQFS222
## Scenario
```gherkin
scenario: a user can search for tasks 
   given the user is logged in 
   when the user enters a search term 
   and clicks the search button 
   then the user should see a list of tasks that match the search term
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user enters a search term and clicks the search button")
def step_impl(context):
    context.search_term = "test"
    context.task_list = TaskList()
    context.task_list.search(context.search_term)

@then("the user should see a list of tasks that match the search term")
def step_impl(context):
    assert context.task_list.tasks == [task for task in context.tasks if context.search_term in task.name]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can search for tasks given the user is logged in when the user enters a search term and clicks the search button then the user should see a list of tasks that match the search term ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user enters a search term and clicks the search button")
def step_impl(context):
    context.search_term = "test"
    context.task_list = TaskList()
    context.task_list.search(context.search_term)

@then("the user should see a list of tasks that match the search term")
def step_impl(context):
    assert context.task_list.tasks == [task for task in context.tasks if context.search_term in task.name]
```

Task: Write a program to find the sum of the digits of a given number.
