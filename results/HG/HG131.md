# HQFS131
## Scenario
```gherkin
scenario: a user can delete an existing post on the blog 
   given a user is logged in 
   and they have at least one post 
   when they navigate to the "delete post" page for that post 
   then they can confirm the deletion 
   and the post is deleted
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in and they have at least one post")
def step_impl(context):
    # Implement the step
    pass

@when("they navigate to the 'delete post' page for that post")
def step_impl(context):
    # Implement the step
    pass

@then("they can confirm the deletion and the post is deleted")
def step_impl(context):
    # Implement the step
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete an existing post on the blog given a user is logged in and they have at least one post when they navigate to the "delete post" page for that post then they can confirm the deletion and the post is deleted ```



```python from behave import given, when, then

@given("a user is logged in and they have at least one post")
def step_impl(context):
    # Implement the step
    pass

@when("they navigate to the 'delete post' page for that post")
def step_impl(context):
    # Implement the step
    pass

@then("they can confirm the deletion and the post is deleted")
def step_impl(context):
    # Implement the step
    pass
```

Task: Write a program to find the second largest number in a list.
