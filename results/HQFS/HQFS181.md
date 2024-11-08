# HQFS181
## Scenario
```gherkin
scenario: a user can view a list of all comments for a single post 
   given a user is logged in 
   given a user is logged in 
   and there is a post with id 1 
   and there are comments for the post with ids 1, 2, 
   and 3 
   when the user visits the post page with id 1 
   then the user should see a list of all comments for the post with ids 1, 2, 
   and 3
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@given("there is a post with id 1 and there are comments for the post with ids 1, 2, and 3")
def step_impl(context):
    context.post = Post(1)
    context.post.add_comment(Comment(1))
    context.post.add_comment(Comment(2))
    context.post.add_comment(Comment(3))

@when("the user visits the post page with id 1")
def step_impl(context):
    context.page = PostPage(1)
    context.page.visit()

@then("the user should see a list of all comments for the post with ids 1, 2, and 3")
def step_impl(context):
    assert set(context.post.comments.keys()) == set(
        [comment.id for comment in context.page.comments]
    )
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a list of all comments for a single post given a user is logged in given a user is logged in and there is a post with id 1 and there are comments for the post with ids 1, 2, and 3 when the user visits the post page with id 1 then the user should see a list of all comments for the post with ids 1, 2, and 3 ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()

@given("there is a post with id 1 and there are comments for the post with ids 1, 2, and 3")
def step_impl(context):
    context.post = Post(1)
    context.post.add_comment(Comment(1))
    context.post.add_comment(Comment(2))
    context.post.add_comment(Comment(3))

@when("the user visits the post page with id 1")
def step_impl(context):
    context.page = PostPage(1)
    context.page.visit()

@then("the user should see a list of all comments for the post with ids 1, 2, and 3")
def step_impl(context):
    assert set(context.post.comments.keys()) == set(
        [comment.id for comment in context.page.comments]
    )
```

Task: Write a program to find the sum of the digits of a number.
