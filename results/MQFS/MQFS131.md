# MQFS131
## Scenario
```gherkin
scenario: a user can view a post 
   given a user is logged in to the system 
   and there is a published post 
   when the user navigates to the post page 
   then the user can view the post's title 
   and content
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in to the system")
def step_given_a_user_is_logged_in_to_the_system(context):
    context.user = User()
    context.user.login()

@given("there is a published post")
def step_given_there_is_a_published_post(context):
    context.post = Post()
    context.post.publish()

@when("the user navigates to the post page")
def step_when_the_user_navigates_to_the_post_page(context):
    context.post_page = PostPage()
    context.post_page.navigate_to()

@then("the user can view the post's title and content")
def step_then_the_user_can_view_the_post_s_title_and_content(context):
    assert context.post_page.title == context.post.title
    assert context.post_page.content == context.post.content
```


## Raw Text
Generate a python implementation of step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a post given a user is logged in to the system and there is a published post when the user navigates to the post page then the user can view the post's title and content ```



```python from behave import given, when, then

@given("a user is logged in to the system")
def step_given_a_user_is_logged_in_to_the_system(context):
    context.user = User()
    context.user.login()

@given("there is a published post")
def step_given_there_is_a_published_post(context):
    context.post = Post()
    context.post.publish()

@when("the user navigates to the post page")
def step_when_the_user_navigates_to_the_post_page(context):
    context.post_page = PostPage()
    context.post_page.navigate_to()

@then("the user can view the post's title and content")
def step_then_the_user_can_view_the_post_s_title_and_content(context):
    assert context.post_page.title == context.post.title
    assert context.post_page.content == context.post.content
```

Task: Write a program to find the sum of the digits of a given number.
