# MQFS263
## Scenario
```gherkin
scenario: 
   given i have a user with username "testuser" 
   and password "testpassword" 
   when i log in with the user 
   then i should be logged in with the user 
   and i should see a dashboard page 
   and i should see a button to create a new post 
   and i click the button to create a new post 
   then i should see a new post page
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a user with username 'testuser' and password 'testpassword'")
def step_impl(context):
    context.user = User.objects.create_user(username="testuser", password="testpassword")

@when("i log in with the user")
def step_impl(context):
    context.response = login(context.user)

@then("i should be logged in with the user")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.user in context.response.context["user"]

@then("i should see a dashboard page")
def step_impl(context):
    assert context.response.status_code == 200
    assert "dashboard" in context.response.content.decode("utf-8")

@then("i should see a button to create a new post")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Create New Post" in context.response.content.decode("utf-8")

@when("i click the button to create a new post")
def step_impl(context):
    context.response = create_post(context.user)

@then("i should see a new post page")
def step_impl(context):
    assert context.response.status_code == 200
    assert "New Post" in context.response.content.decode("utf-8")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i have a user with username "testuser" and password "testpassword" when i log in with the user then i should be logged in with the user and i should see a dashboard page and i should see a button to create a new post and i click the button to create a new post then i should see a new post page ```



```python from behave import given, when, then

@given("i have a user with username 'testuser' and password 'testpassword'")
def step_impl(context):
    context.user = User.objects.create_user(username="testuser", password="testpassword")

@when("i log in with the user")
def step_impl(context):
    context.response = login(context.user)

@then("i should be logged in with the user")
def step_impl(context):
    assert context.response.status_code == 200
    assert context.user in context.response.context["user"]

@then("i should see a dashboard page")
def step_impl(context):
    assert context.response.status_code == 200
    assert "dashboard" in context.response.content.decode("utf-8")

@then("i should see a button to create a new post")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Create New Post" in context.response.content.decode("utf-8")

@when("i click the button to create a new post")
def step_impl(context):
    context.response = create_post(context.user)

@then("i should see a new post page")
def step_impl(context):
    assert context.response.status_code == 200
    assert "New Post" in context.response.content.decode("utf-8")
```

Task: Write a program to find the sum of the digits of a number.
