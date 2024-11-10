# HQFS259
## Scenario
```gherkin
scenario: a user can view a single post 
   given the user is logged in 
   and there is a post on the page 
   when the user views the single post 
   then the post should be visible on the page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in")
def step_given_the_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@given("there is a post on the page")
def step_given_there_is_a_post_on_the_page(context):
    context.post = Post()
    context.post.create()

@when("the user views the single post")
def step_when_the_user_views_the_single_post(context):
    context.post_page = PostPage()
    context.post_page.view_post(context.post)

@then("the post should be visible on the page")
def step_then_the_post_should_be_visible_on_the_page(context):
    assert context.post_page.post_visible(context.post)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a single post given the user is logged in and there is a post on the page when the user views the single post then the post should be visible on the page ```



```python from behave import given, when, then

@given("the user is logged in")
def step_given_the_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@given("there is a post on the page")
def step_given_there_is_a_post_on_the_page(context):
    context.post = Post()
    context.post.create()

@when("the user views the single post")
def step_when_the_user_views_the_single_post(context):
    context.post_page = PostPage()
    context.post_page.view_post(context.post)

@then("the post should be visible on the page")
def step_then_the_post_should_be_visible_on_the_page(context):
    assert context.post_page.post_visible(context.post)
```

Task: Write a program to find the sum of the digits of a given number.
