# HQFS75
## Scenario
```gherkin
scenario: user can delete their account 
   given a user is logged in 
   when they click on their profile picture 
   then they should be taken to their profile page 
   when they click on the 'delete account' button 
   then they should be taken to the delete account page 
   when they confirm deletion 
   then their account should be deleted
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can delete their account given a user is logged in when they click on their profile picture then they should be taken to their profile page when they click on the 'delete account' button then they should be taken to the delete account page when they confirm deletion then their account should be deleted ```



from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    pass

@when("they click on their profile picture")
def step_impl(context):
    pass

@then("they should be taken to their profile page")
def step_impl(context):
    pass

@when("they click on the 'delete account' button")
def step_impl(context):
    pass

@then("they should be taken to the delete account page")
def step_impl(context):
    pass

@when("they confirm deletion")
def step_impl(context):
    pass

@then("their account should be deleted")
def step_impl(context):
    pass
