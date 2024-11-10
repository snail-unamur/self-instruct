# HQFS204
## Scenario
```gherkin
scenario: user can edit a log entry 
   given the user is logged in 
   when the user navigates to the log entry page 
   and the user selects the edit button for a log entry 
   then the user should be redirected to the edit log entry page 
   and the user should be able to edit the log entry 
   and the user should be able to submit the edited log entry 
   and the user should be redirected to the log entry page 
   and the edited log entry should be displayed on the log entry page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the log entry page")
def step_impl(context):
    pass

@when("the user selects the edit button for a log entry")
def step_impl(context):
    pass

@then("the user should be redirected to the edit log entry page")
def step_impl(context):
    pass

@then("the user should be able to edit the log entry")
def step_impl(context):
    pass

@then("the user should be able to submit the edited log entry")
def step_impl(context):
    pass

@then("the user should be redirected to the log entry page")
def step_impl(context):
    pass

@then("the edited log entry should be displayed on the log entry page")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can edit a log entry given the user is logged in when the user navigates to the log entry page and the user selects the edit button for a log entry then the user should be redirected to the edit log entry page and the user should be able to edit the log entry and the user should be able to submit the edited log entry and the user should be redirected to the log entry page and the edited log entry should be displayed on the log entry page ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    pass

@when("the user navigates to the log entry page")
def step_impl(context):
    pass

@when("the user selects the edit button for a log entry")
def step_impl(context):
    pass

@then("the user should be redirected to the edit log entry page")
def step_impl(context):
    pass

@then("the user should be able to edit the log entry")
def step_impl(context):
    pass

@then("the user should be able to submit the edited log entry")
def step_impl(context):
    pass

@then("the user should be redirected to the log entry page")
def step_impl(context):
    pass

@then("the edited log entry should be displayed on the log entry page")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
