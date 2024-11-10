# HQFS67
## Scenario
```gherkin
scenario: user can delete a post 
   given i am logged in as "kea@gmail.com" 
   and i am on the home page 
   when i click on the "delete" button for a post 
   then i am redirected to the home page 
   and i no longer see the post in my list of posts
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as 'kea@gmail.com' and i am on the home page")
def step_impl(context):
    context.execute_steps(u"""
        given i am logged in as "kea@gmail.com"
        and i am on the home page
    """)

@when("i click on the 'delete' button for a post")
def step_impl(context):
    context.execute_steps(u"""
        when i click on the "delete" button for a post
    """)

@then("i am redirected to the home page")
def step_impl(context):
    context.execute_steps(u"""
        then i am redirected to the home page
    """)

@then("i no longer see the post in my list of posts")
def step_impl(context):
    context.execute_steps(u"""
        then i no longer see the post in my list of posts
    """)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can delete a post given i am logged in as "kea@gmail.com" and i am on the home page when i click on the "delete" button for a post then i am redirected to the home page and i no longer see the post in my list of posts ```



```python from behave import given, when, then

@given("i am logged in as 'kea@gmail.com' and i am on the home page")
def step_impl(context):
    context.execute_steps(u"""
        given i am logged in as "kea@gmail.com"
        and i am on the home page
    """)

@when("i click on the 'delete' button for a post")
def step_impl(context):
    context.execute_steps(u"""
        when i click on the "delete" button for a post
    """)

@then("i am redirected to the home page")
def step_impl(context):
    context.execute_steps(u"""
        then i am redirected to the home page
    """)

@then("i no longer see the post in my list of posts")
def step_impl(context):
    context.execute_steps(u"""
        then i no longer see the post in my list of posts
    """)
```

Task: Write a program to find the sum of the digits of a number.
