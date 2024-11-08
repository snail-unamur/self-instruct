# MQFS68
## Scenario
```gherkin
scenario: user can add a new post 
   given i am logged in as a user 
   when i navigate to the posts page 
   then i should see a button to add a new post 
   when i click on the button to add a new post 
   then i should see a form to enter the details of the new post 
   when i enter the details of the new post 
   and i click on the submit button 
   then i should be taken back to the posts page 
   and i should see the new post listed on the page
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.force_login(context.user)

@when("i navigate to the posts page")
def step_impl(context):
    context.response = context.client.get("/posts/")

@then("i should see a button to add a new post")
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Add Post" in context.response.content

@when("i click on the button to add a new post")
def step_impl(context):
    response = context.client.get("/posts/add/")
    context.response = context.client.post("/posts/add/", {
        "title": "Test Post",
        "content": "Test Content"
    })

@then("i should see a form to enter the details of the new post")
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Title" in context.response.content
    assert b"Content" in context.response.content

@then("i enter the details of the new post and i click on the submit button")
def step_impl(context):
    context.response = context.client.post("/posts/add/", {
        "title": "Test Post",
        "content": "Test Content"
    })

@then("i should be taken back to the posts page")
def step_impl(context):
    assert context.response.status_code == 302
    assert context.client.get("/posts/").status_code == 200

@then("i should see the new post listed on the page")
def step_impl(context):
    assert b"Test Post" in context.client.get("/posts/").content
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can add a new post given i am logged in as a user when i navigate to the posts page then i should see a button to add a new post when i click on the button to add a new post then i should see a form to enter the details of the new post when i enter the details of the new post and i click on the submit button then i should be taken back to the posts page and i should see the new post listed on the page ```



```python from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.force_login(context.user)

@when("i navigate to the posts page")
def step_impl(context):
    context.response = context.client.get("/posts/")

@then("i should see a button to add a new post")
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Add Post" in context.response.content

@when("i click on the button to add a new post")
def step_impl(context):
    response = context.client.get("/posts/add/")
    context.response = context.client.post("/posts/add/", {
        "title": "Test Post",
        "content": "Test Content"
    })

@then("i should see a form to enter the details of the new post")
def step_impl(context):
    assert context.response.status_code == 200
    assert b"Title" in context.response.content
    assert b"Content" in context.response.content

@then("i enter the details of the new post and i click on the submit button")
def step_impl(context):
    context.response = context.client.post("/posts/add/", {
        "title": "Test Post",
        "content": "Test Content"
    })

@then("i should be taken back to the posts page")
def step_impl(context):
    assert context.response.status_code == 302
    assert context.client.get("/posts/").status_code == 200

@then("i should see the new post listed on the page")
def step_impl(context):
    assert b"Test Post" in context.client.get("/posts/").content
```

Task: Write a program to find the sum of the digits of a number.
