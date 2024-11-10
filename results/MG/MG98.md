# MQFS98
## Scenario
```gherkin
scenario: user can filter contacts by group in the address book 
   given a user is logged in 
   and the address book contains contacts with names


   and groups

   when the user selects the filter button

   then the filter contacts dialog is displayed

   when the user selects a group

   and the user selects the apply button

   then only the contacts in the selected group are displayed

Python Implementation:
from behave import 
   given, 
   when, 
   then

@
   given("a user is logged in 
   and the address book contains contacts with names 
   and groups")
def step_impl(context):
    pass

@
   when("the user selects the filter button")
def step_impl(context):
    pass

@
   then("the filter contacts dialog is displayed")
def step_impl(context):
    pass

@
   when("the user selects a group")
def step_impl(context):
    pass

@
   when("the user selects the apply button")
def step_impl(context):
    pass

@
   then("only the contacts in the selected group are displayed")
def step_impl(context):
    pass
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in and the address book contains contacts with names and groups")
def step_impl(context):
    pass

@when("the user selects the filter button")
def step_impl(context):
    pass

@then("the filter contacts dialog is displayed")
def step_impl(context):
    pass

@when("the user selects a group")
def step_impl(context):
    pass

@when("the user selects the apply button")
def step_impl(context):
    pass

@then("only the contacts in the selected group are displayed")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can filter contacts by group in the address book given a user is logged in and the address book contains contacts with names

and groups
when the user selects the filter button
then the filter contacts dialog is displayed
when the user selects a group
and the user selects the apply button
then only the contacts in the selected group are displayed

Python Implementation:
from behave import given, when, then

@given("a user is logged in and the address book contains contacts with names and groups")
def step_impl(context):
    pass

@when("the user selects the filter button")
def step_impl(context):
    pass

@then("the filter contacts dialog is displayed")
def step_impl(context):
    pass

@when("the user selects a group")
def step_impl(context):
    pass

@when("the user selects the apply button")
def step_impl(context):
    pass

@then("only the contacts in the selected group are displayed")
def step_impl(context):
    pass
```

```python
from behave import given, when, then

@given("a user is logged in and the address book contains contacts with names and groups")
def step_impl(context):
    pass

@when("the user selects the filter button")
def step_impl(context):
    pass

@then("the filter contacts dialog is displayed")
def step_impl(context):
    pass

@when("the user selects a group")
def step_impl(context):
    pass

@when("the user selects the apply button")
def step_impl(context):
    pass

@then("only the contacts in the selected group are displayed")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
