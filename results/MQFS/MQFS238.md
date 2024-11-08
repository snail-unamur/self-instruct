# MQFS238
## Scenario
```gherkin
scenario: user can see the details of a specific project 
   given a user is logged in 
   and they navigate to the project list page 
   and they click on the project name 
   then they should see the details of that specific project
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.execute_steps("Given a user is logged in with valid credentials")

@when("they navigate to the project list page")
def step_impl(context):
    context.project_list_page.navigate_to_page()

@when("they click on the project name")
def step_impl(context):
    context.project_list_page.click_project_name()

@then("they should see the details of that specific project")
def step_impl(context):
    context.project_details_page.should_be_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can see the details of a specific project given a user is logged in and they navigate to the project list page and they click on the project name then they should see the details of that specific project ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.execute_steps("Given a user is logged in with valid credentials")

@when("they navigate to the project list page")
def step_impl(context):
    context.project_list_page.navigate_to_page()

@when("they click on the project name")
def step_impl(context):
    context.project_list_page.click_project_name()

@then("they should see the details of that specific project")
def step_impl(context):
    context.project_details_page.should_be_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
