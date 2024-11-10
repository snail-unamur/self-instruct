# HQFS269
## Scenario
```gherkin
scenario: user can edit a post 
   given a user is logged in 
   when they click on the "edit" button on one of their posts 
   then they are taken to a page where they can edit the post
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.browser.login(context.user.username, "testpassword")

@when("they click on the 'edit' button on one of their posts")
def step_impl(context):
    post = Post.objects.get(user=context.user, title="Test Post")
    context.browser.visit(post.get_absolute_url())
    context.browser.click_link_by_value("Edit")

@then("they are taken to a page where they can edit the post")
def step_impl(context):
    post = Post.objects.get(user=context.user, title="Test Post")
    context.browser.visit(post.get_absolute_url() + "edit/")
    assert context.browser.title == "Edit Post"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can edit a post given a user is logged in when they click on the "edit" button on one of their posts then they are taken to a page where they can edit the post ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.browser.login(context.user.username, "testpassword")

@when("they click on the 'edit' button on one of their posts")
def step_impl(context):
    post = Post.objects.get(user=context.user, title="Test Post")
    context.browser.visit(post.get_absolute_url())
    context.browser.click_link_by_value("Edit")

@then("they are taken to a page where they can edit the post")
def step_impl(context):
    post = Post.objects.get(user=context.user, title="Test Post")
    context.browser.visit(post.get_absolute_url() + "edit/")
    assert context.browser.title == "Edit Post"
```

Task: Write a program to find the sum of the digits of a number.
