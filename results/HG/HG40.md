# HQFS40
## Scenario
```gherkin
scenario: edit a user 
   given i am on the user list page 
   when i click the "edit" button next to a user 
   then i should be redirected to the edit user page 
   and i should be able to edit the user's information 
   and i should be able to save the edited user 
   then the edited user should be updated in the user list 
   and i should be redirected to the user list page
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the user list page")
def step_impl(context):
    pass

@when("i click the \"edit\" button next to a user")
def step_impl(context):
    pass

@then("i should be redirected to the edit user page")
def step_impl(context):
    pass

@then("i should be able to edit the user's information")
def step_impl(context):
    pass

@then("i should be able to save the edited user")
def step_impl(context):
    pass

@then("the edited user should be updated in the user list")
def step_impl(context):
    pass

@then("i should be redirected to the user list page")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: edit a user given i am on the user list page when i click the "edit" button next to a user then i should be redirected to the edit user page and i should be able to edit the user's information and i should be able to save the edited user then the edited user should be updated in the user list and i should be redirected to the user list page ```



```python from behave import given, when, then

@given("i am on the user list page")
def step_impl(context):
    pass

@when("i click the \"edit\" button next to a user")
def step_impl(context):
    pass

@then("i should be redirected to the edit user page")
def step_impl(context):
    pass

@then("i should be able to edit the user's information")
def step_impl(context):
    pass

@then("i should be able to save the edited user")
def step_impl(context):
    pass

@then("the edited user should be updated in the user list")
def step_impl(context):
    pass

@then("i should be redirected to the user list page")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
