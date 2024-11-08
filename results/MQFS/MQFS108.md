# MQFS108
## Scenario
```gherkin
scenario: create a new post 
   given i am on the post creation page 
   when i fill in the form with the following data: title: "my first post" body: "this is the body of my first post." slug: "my-first-post" status: "publish" 
   when i submit the form 
   then i should be redirected to the post list page 
   and i should see the new post in the list
```


## Python Implementation
```python
from behave import given, when, then
from django.urls import reverse

@given("i am on the post creation page")
def step_impl(context):
    context.response = context.client.get(reverse("post_create"))

@when("i fill in the form with the following data:")
def step_impl(context):
    context.response = context.client.post(
        reverse("post_create"),
        {
            "title": "my first post",
            "body": "this is the body of my first post.",
            "slug": "my-first-post",
            "status": "publish",
        },
    )

@then("i should be redirected to the post list page")
def step_impl(context):
    assert context.response.status_code == 302
    assert context.response.url == reverse("post_list")

@then("i should see the new post in the list")
def step_impl(context):
    context.response = context.client.get(reverse("post_list"))
    assert "my first post" in context.response.content.decode()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new post given i am on the post creation page when i fill in the form with the following data: title: "my first post" body: "this is the body of my first post." slug: "my-first-post" status: "publish" when i submit the form then i should be redirected to the post list page and i should see the new post in the list ```



```python from behave import given, when, then
from django.urls import reverse

@given("i am on the post creation page")
def step_impl(context):
    context.response = context.client.get(reverse("post_create"))

@when("i fill in the form with the following data:")
def step_impl(context):
    context.response = context.client.post(
        reverse("post_create"),
        {
            "title": "my first post",
            "body": "this is the body of my first post.",
            "slug": "my-first-post",
            "status": "publish",
        },
    )

@then("i should be redirected to the post list page")
def step_impl(context):
    assert context.response.status_code == 302
    assert context.response.url == reverse("post_list")

@then("i should see the new post in the list")
def step_impl(context):
    context.response = context.client.get(reverse("post_list"))
    assert "my first post" in context.response.content.decode()
```

Task: Write a program to find the sum of the digits of a given number.
