# HQFS71
## Scenario
```gherkin
scenario: user can view all posts 
   given that the posts exist 
   given the posts exist 
   when the user makes a get request to /posts 
   then all the posts should be returned
```


## Python Implementation
```python
from behave import given, when, then

@given("the posts exist")
def step_impl(context):
    context.posts = [
        {"id": 1, "title": "Post 1", "content": "Content of Post 1"},
        {"id": 2, "title": "Post 2", "content": "Content of Post 2"},
        {"id": 3, "title": "Post 3", "content": "Content of Post 3"},
    ]

@when("the user makes a get request to /posts")
def step_impl(context):
    context.response = context.app.get("/posts")

@then("all the posts should be returned")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json == context.posts
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view all posts given that the posts exist given the posts exist when the user makes a get request to /posts then all the posts should be returned ```



```python from behave import given, when, then

@given("the posts exist")
def step_impl(context):
    context.posts = [
        {"id": 1, "title": "Post 1", "content": "Content of Post 1"},
        {"id": 2, "title": "Post 2", "content": "Content of Post 2"},
        {"id": 3, "title": "Post 3", "content": "Content of Post 3"},
    ]

@when("the user makes a get request to /posts")
def step_impl(context):
    context.response = context.app.get("/posts")

@then("all the posts should be returned")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json == context.posts
```

Task: Write a program to find the sum of the digits of a given number.
