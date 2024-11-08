# HQFS161
## Scenario
```gherkin
scenario: user can view a post 
   given a post exists 
   when the user navigates to the post page 
   then the user should see the post with the 
   given title 
   and body
```


## Python Implementation
```python
from behave import given, when, then

@given("a post exists")
def step_impl(context):
    context.post = {"title": "Test Post", "body": "Test Body"}
    context.post_id = 1
    context.app.post_list[context.post_id] = context.post

@when("the user navigates to the post page")
def step_impl(context):
    context.response = context.app.get_post(context.post_id)

@then("the user should see the post with the given title and body")
def step_impl(context):
    post = context.response.json()
    assert post["title"] == context.post["title"]
    assert post["body"] == context.post["body"]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view a post given a post exists when the user navigates to the post page then the user should see the post with the given title and body ```



```python from behave import given, when, then

@given("a post exists")
def step_impl(context):
    context.post = {"title": "Test Post", "body": "Test Body"}
    context.post_id = 1
    context.app.post_list[context.post_id] = context.post

@when("the user navigates to the post page")
def step_impl(context):
    context.response = context.app.get_post(context.post_id)

@then("the user should see the post with the given title and body")
def step_impl(context):
    post = context.response.json()
    assert post["title"] == context.post["title"]
    assert post["body"] == context.post["body"]
```

Task: Write a program to find the sum of the digits of a given number.
