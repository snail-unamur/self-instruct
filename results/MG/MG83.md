# MQFS83
## Scenario
```gherkin
scenario: user can view a list of all posts 
   given a user is logged in 
   and there are at least two posts 
   when the user navigates to the posts page 
   then the user should see a list of all posts 
   and the number of posts should be equal to the number of posts in the system
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.login(username=context.user.username, password="testpassword")

@given("there are at least two posts")
def step_impl(context):
    Post.objects.create(title="Test Post 1", content="Test Content 1", author=context.user)
    Post.objects.create(title="Test Post 2", content="Test Content 2", author=context.user)

@when("the user navigates to the posts page")
def step_impl(context):
    context.response = context.client.get("/posts/")

@then("the user should see a list of all posts")
def step_impl(context):
    assert context.response.status_code == 200
    assert len(context.response.context["object_list"]) == 2
    assert all(post.title in context.response.content.decode() for post in Post.objects.all())

@then("the number of posts should be equal to the number of posts in the system")
def step_impl(context):
    assert len(context.response.context["object_list"]) == Post.objects.count()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view a list of all posts given a user is logged in and there are at least two posts when the user navigates to the posts page then the user should see a list of all posts and the number of posts should be equal to the number of posts in the system```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.login(username=context.user.username, password="testpassword")

@given("there are at least two posts")
def step_impl(context):
    Post.objects.create(title="Test Post 1", content="Test Content 1", author=context.user)
    Post.objects.create(title="Test Post 2", content="Test Content 2", author=context.user)

@when("the user navigates to the posts page")
def step_impl(context):
    context.response = context.client.get("/posts/")

@then("the user should see a list of all posts")
def step_impl(context):
    assert context.response.status_code == 200
    assert len(context.response.context["object_list"]) == 2
    assert all(post.title in context.response.content.decode() for post in Post.objects.all())

@then("the number of posts should be equal to the number of posts in the system")
def step_impl(context):
    assert len(context.response.context["object_list"]) == Post.objects.count()
```

Task: Write a program to find the sum of the digits of a given number.
