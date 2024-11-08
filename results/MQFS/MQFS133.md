# MQFS133
## Scenario
```gherkin
scenario: a user can create a new post with a title 
   and a body 
   given a user is logged in 
   when the user creates a new post with title "test post" 
   and body "this is a test post" 
   then the user should see the new post with title "test post" 
   and body "this is a test post"
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.login(username=context.user.username, password="testpassword")

@when("the user creates a new post with title 'test post' and body 'this is a test post'")
def step_impl(context):
    context.response = context.client.post(
        "/posts/new/",
        {"title": "test post", "body": "this is a test post"},
        follow=True,
    )

@then("the user should see the new post with title 'test post' and body 'this is a test post'")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.context["post"].title == "test post"
    assert context.response.context["post"].body == "this is a test post"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can create a new post with a title and a body given a user is logged in when the user creates a new post with title "test post" and body "this is a test post" then the user should see the new post with title "test post" and body "this is a test post" ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.login(username=context.user.username, password="testpassword")

@when("the user creates a new post with title 'test post' and body 'this is a test post'")
def step_impl(context):
    context.response = context.client.post(
        "/posts/new/",
        {"title": "test post", "body": "this is a test post"},
        follow=True,
    )

@then("the user should see the new post with title 'test post' and body 'this is a test post'")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.context["post"].title == "test post"
    assert context.response.context["post"].body == "this is a test post"
```

Task: Write a program to find the sum of the digits of a given number.
