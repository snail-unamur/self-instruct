# HQFS152
## Scenario
```gherkin
scenario: a user can delete a log 
   given that the user has valid credentials 
   and the user navigates to the log page 
   and the user selects the log to delete 
   and the user confirms the deletion 
   when the user tries to delete the log 
   then the log should be deleted 
   and the user should be redirected to the logs page 
   and the log should not be listed at the /logs endpoint
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has valid credentials")
def step_impl(context):
    context.user = User("testuser", "testpassword")

@given("the user navigates to the log page")
def step_impl(context):
    context.log_page = LogPage()
    context.log_page.navigate()

@when("the user selects the log to delete")
def step_impl(context):
    context.log = context.log_page.select_log()

@when("the user confirms the deletion")
def step_impl(context):
    context.log.delete()

@then("the log should be deleted")
def step_impl(context):
    assert context.log.deleted

@then("the user should be redirected to the logs page")
def step_impl(context):
    assert context.log_page.current_url == context.base_url + "/logs"

@then("the log should not be listed at the /logs endpoint")
def step_impl(context):
    logs = context.client.get(context.base_url + "/logs").json()
    assert context.log not in logs
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a log given that the user has valid credentials and the user navigates to the log page and the user selects the log to delete and the user confirms the deletion when the user tries to delete the log then the log should be deleted and the user should be redirected to the logs page and the log should not be listed at the /logs endpoint ```



```python from behave import given, when, then

@given("a user has valid credentials")
def step_impl(context):
    context.user = User("testuser", "testpassword")

@given("the user navigates to the log page")
def step_impl(context):
    context.log_page = LogPage()
    context.log_page.navigate()

@when("the user selects the log to delete")
def step_impl(context):
    context.log = context.log_page.select_log()

@when("the user confirms the deletion")
def step_impl(context):
    context.log.delete()

@then("the log should be deleted")
def step_impl(context):
    assert context.log.deleted

@then("the user should be redirected to the logs page")
def step_impl(context):
    assert context.log_page.current_url == context.base_url + "/logs"

@then("the log should not be listed at the /logs endpoint")
def step_impl(context):
    logs = context.client.get(context.base_url + "/logs").json()
    assert context.log not in logs
```

Task: Write a program to find the sum of the digits of a number.
