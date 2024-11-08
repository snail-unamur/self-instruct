# HQFS94
## Scenario
```gherkin
scenario: a user can edit a log entry 
   given that the user has valid credentials 
   and the user makes a get request to /account 
   when the user navigates to the log entry list 
   and the user selects a log entry 
   and the user clicks the edit button 
   then the log entry should be displayed in edit mode
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has valid credentials")
def step_given_a_user_has_valid_credentials(context):
    context.user = User("testuser", "testpassword")

@when("the user makes a get request to /account")
def step_when_the_user_makes_a_get_request_to_account(context):
    context.response = context.client.get("/account")

@then("the user navigates to the log entry list")
def step_then_the_user_navigates_to_the_log_entry_list(context):
    assert context.response.status_code == 200

@when("the user selects a log entry")
def step_when_the_user_selects_a_log_entry(context):
    context.log_entry = LogEntry("test log entry")
    context.response = context.client.get("/log_entries/1")

@when("the user clicks the edit button")
def step_when_the_user_clicks_the_edit_button(context):
    context.response = context.client.get("/log_entries/1/edit")

@then("the log entry should be displayed in edit mode")
def step_then_the_log_entry_should_be_displayed_in_edit_mode(context):
    assert context.response.status_code == 200
    assert context.response.content.find(context.log_entry.title) > -1
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit a log entry given that the user has valid credentials and the user makes a get request to /account when the user navigates to the log entry list and the user selects a log entry and the user clicks the edit button then the log entry should be displayed in edit mode ```



```python from behave import given, when, then

@given("a user has valid credentials")
def step_given_a_user_has_valid_credentials(context):
    context.user = User("testuser", "testpassword")

@when("the user makes a get request to /account")
def step_when_the_user_makes_a_get_request_to_account(context):
    context.response = context.client.get("/account")

@then("the user navigates to the log entry list")
def step_then_the_user_navigates_to_the_log_entry_list(context):
    assert context.response.status_code == 200

@when("the user selects a log entry")
def step_when_the_user_selects_a_log_entry(context):
    context.log_entry = LogEntry("test log entry")
    context.response = context.client.get("/log_entries/1")

@when("the user clicks the edit button")
def step_when_the_user_clicks_the_edit_button(context):
    context.response = context.client.get("/log_entries/1/edit")

@then("the log entry should be displayed in edit mode")
def step_then_the_log_entry_should_be_displayed_in_edit_mode(context):
    assert context.response.status_code == 200
    assert context.response.content.find(context.log_entry.title) > -1
```

Task: Write a program to find the sum of the digits of a number.
