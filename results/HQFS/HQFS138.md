# HQFS138
## Scenario
```gherkin
scenario: testing the delete functionality 
   given i am logged in as a user with a post 
   when i click on the delete button for the post 
   then i should see a confirmation message 
   and the post should be deleted
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as a user with a post")
def step_impl(context):
    # Implement the step
    pass

@when("i click on the delete button for the post")
def step_impl(context):
    # Implement the step
    pass

@then("i should see a confirmation message and the post should be deleted")
def step_impl(context):
    # Implement the step
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete functionality given i am logged in as a user with a post when i click on the delete button for the post then i should see a confirmation message and the post should be deleted ```



```python from behave import given, when, then

@given("i am logged in as a user with a post")
def step_impl(context):
    # Implement the step
    pass

@when("i click on the delete button for the post")
def step_impl(context):
    # Implement the step
    pass

@then("i should see a confirmation message and the post should be deleted")
def step_impl(context):
    # Implement the step
    pass
```

Task: Write a program to find the sum of the digits of a given number.
