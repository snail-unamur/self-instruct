# HQFS54
## Scenario
```gherkin
scenario: testing the task filtering functionality 
   given i am logged in as a user 
   and i am on the project page 
   when i select a task status from the filter dropdown


   then the task list should update to show only tasks with the selected status

Scenario: testing the task filtering functionality

   Given i am logged in as a user

   And i am on the project page

   When i select a task status from the filter dropdown

   Then the task list should update to show only tasks with the selected status
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User()
    context.user.login()

@given("i am on the project page")
def step_impl(context):
    context.project_page = ProjectPage(context.user)
    context.project_page.load()

@when("i select a task status from the filter dropdown")
def step_impl(context):
    context.selected_status = "In Progress"
    context.project_page.select_task_status_filter(context.selected_status)

@then("the task list should update to show only tasks with the selected status")
def step_impl(context):
    tasks_with_selected_status = context.project_page.get_tasks_with_status(context.selected_status)
    tasks_displayed = context.project_page.get_displayed_tasks()
    assert tasks_displayed == tasks_with_selected_status
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the task filtering functionality given i am logged in as a user and i am on the project page when i select a task status from the filter dropdown

then the task list should update to show only tasks with the selected status

Scenario: testing the task filtering functionality
Given i am logged in as a user
And i am on the project page
When i select a task status from the filter dropdown
Then the task list should update to show only tasks with the selected status
```

```python from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User()
    context.user.login()

@given("i am on the project page")
def step_impl(context):
    context.project_page = ProjectPage(context.user)
    context.project_page.load()

@when("i select a task status from the filter dropdown")
def step_impl(context):
    context.selected_status = "In Progress"
    context.project_page.select_task_status_filter(context.selected_status)

@then("the task list should update to show only tasks with the selected status")
def step_impl(context):
    tasks_with_selected_status = context.project_page.get_tasks_with_status(context.selected_status)
    tasks_displayed = context.project_page.get_displayed_tasks()
    assert tasks_displayed == tasks_with_selected_status
```

Task: Write a program to find the sum of the digits of a number.
