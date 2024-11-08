# HQFS78
## Scenario
```gherkin
scenario: a user wants to add a new tag to a post 
   given the user is logged in 
   when the user is on the post page 
   and the user clicks the 'add tag' button 
   then the user is taken to a page to add a new tag 
   and the user can enter the name of the new tag 
   and the user can submit the new tag 
   and the new tag is added to the post 
   and the user is taken back to the post page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    pass

@given("the user is on the post page")
def step_impl(context):
    pass

@when("the user clicks the 'add tag' button")
def step_impl(context):
    pass

@then("the user is taken to a page to add a new tag")
def step_impl(context):
    pass

@then("the user can enter the name of the new tag")
def step_impl(context):
    pass

@then("the user can submit the new tag")
def step_impl(context):
    pass

@then("the new tag is added to the post")
def step_impl(context):
    pass

@then("the user is taken back to the post page")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user wants to add a new tag to a post given the user is logged in when the user is on the post page and the user clicks the 'add tag' button then the user is taken to a page to add a new tag and the user can enter the name of the new tag and the user can submit the new tag and the new tag is added to the post and the user is taken back to the post page ```



```python from behave import given, when, then

@given("the user is logged in")
def step_impl(context):
    pass

@given("the user is on the post page")
def step_impl(context):
    pass

@when("the user clicks the 'add tag' button")
def step_impl(context):
    pass

@then("the user is taken to a page to add a new tag")
def step_impl(context):
    pass

@then("the user can enter the name of the new tag")
def step_impl(context):
    pass

@then("the user can submit the new tag")
def step_impl(context):
    pass

@then("the new tag is added to the post")
def step_impl(context):
    pass

@then("the user is taken back to the post page")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
