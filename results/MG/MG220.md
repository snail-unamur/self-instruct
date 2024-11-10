# MQFS220
## Scenario
```gherkin
scenario: user creates a new blog post 
   given a user is logged in with email "john@example.com" 
   and password "password" 
   when the user creates a new blog post with title "my first blog post" 
   and content "this is my first blog post." 
   then the user's blog post is created with title "my first blog post" 
   and content "this is my first blog post."
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in with email 'john@example.com' and password 'password'")
def step_impl(context):
    context.user = User.login("john@example.com", "password")

@when("the user creates a new blog post with title 'my first blog post' and content 'this is my first blog post.'")
def step_impl(context):
    context.blog_post = context.user.create_blog_post(title="my first blog post", content="this is my first blog post.")

@then("the user's blog post is created with title 'my first blog post' and content 'this is my first blog post.'")
def step_impl(context):
    assert context.blog_post.title == "my first blog post"
    assert context.blog_post.content == "this is my first blog post."
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user creates a new blog post given a user is logged in with email "john@example.com" and password "password" when the user creates a new blog post with title "my first blog post" and content "this is my first blog post." then the user's blog post is created with title "my first blog post" and content "this is my first blog post." ```



```python from behave import given, when, then

@given("a user is logged in with email 'john@example.com' and password 'password'")
def step_impl(context):
    context.user = User.login("john@example.com", "password")

@when("the user creates a new blog post with title 'my first blog post' and content 'this is my first blog post.'")
def step_impl(context):
    context.blog_post = context.user.create_blog_post(title="my first blog post", content="this is my first blog post.")

@then("the user's blog post is created with title 'my first blog post' and content 'this is my first blog post.'")
def step_impl(context):
    assert context.blog_post.title == "my first blog post"
    assert context.blog_post.content == "this is my first blog post."
```

Task: Write a program to find the sum of the digits of a number.
