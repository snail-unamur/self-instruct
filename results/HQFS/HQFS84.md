# HQFS84
## Scenario
```gherkin
scenario: creating a new post 
   given a blog with the following posts: | title | content | | --- | --- | | post 1 | this is the first post | | post 2 | this is the second post | 
   when a new post is created with the following details: | title | content | | --- | --- | | new post | this is a new post | 
   then the new post is displayed in the blog 
   and the blog is sorted by date
```


## Python Implementation
```python
from behave import given, when, then
from model import Blog, Post

@given("a blog with the following posts:")
def step(context):
    context.blog = Blog()
    context.blog.add_post(Post("post 1", "this is the first post"))
    context.blog.add_post(Post("post 2", "this is the second post"))

@when("a new post is created with the following details:")
def step(context, title, content):
    context.new_post = Post(title, content)
    context.blog.add_post(context.new_post)

@then("the new post is displayed in the blog and the blog is sorted by date")
def step(context):
    assert context.new_post in context.blog.posts
    assert context.blog.posts == sorted(context.blog.posts, key=lambda post: post.date)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: creating a new post given a blog with the following posts: | title | content | | --- | --- | | post 1 | this is the first post | | post 2 | this is the second post | when a new post is created with the following details: | title | content | | --- | --- | | new post | this is a new post | then the new post is displayed in the blog and the blog is sorted by date ```



```python from behave import given, when, then
from model import Blog, Post

@given("a blog with the following posts:")
def step(context):
    context.blog = Blog()
    context.blog.add_post(Post("post 1", "this is the first post"))
    context.blog.add_post(Post("post 2", "this is the second post"))

@when("a new post is created with the following details:")
def step(context, title, content):
    context.new_post = Post(title, content)
    context.blog.add_post(context.new_post)

@then("the new post is displayed in the blog and the blog is sorted by date")
def step(context):
    assert context.new_post in context.blog.posts
    assert context.blog.posts == sorted(context.blog.posts, key=lambda post: post.date)
```

Task: Write a program to find the sum of the digits of a number.
