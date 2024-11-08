# MQFS142
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can create a new post given that a user is logged in when they navigate to the new post page and they enter a title and content for the post and they click the publish button then the post should be created and they should be taken to the post page and the post should be visible on the post page and the post should have the title and content they entered and the post should have the current date and time as the published date and the post should have the user as the author



from behave import given, when, then
from datetime import datetime
from typing import Dict

@given("a user is logged in")
def step_impl(context):
    context.user = User("testuser")
    context.auth_token = context.user.login()

@given("they navigate to the new post page")
def step_impl(context):
    context.response = context.client.get("/new_post", headers={"Authorization": context.auth_token})

@when("they enter a title and content for the post")
def step_impl(context):
    context.post_data = {
        "title": "Test Post",
        "content": "This is a test post.",
        "published_date": datetime.now().isoformat()
    }
    context.response = context.client.post("/new_post", json=context.post_data, headers={"Authorization": context.auth_token})

@then("the post should be created")
def step_impl(context):
    assert context.response.status_code == 201
    context.post_id = context.response.json["id"]

@then("they should be taken to the post page")
def step_impl(context):
    context.response = context.client.get(f"/posts/{context.post_id}", headers={"Authorization": context.auth_token})
    assert context.response.status_code == 200

@then("the post should be visible on the post page")
def step_impl(context):
    post = context.response.json
    assert post["id"] == context.post_id

@then("the post should have the title and content they entered")
def step_impl(context):
    post = context.response.json
    assert post["title"] == context.post_data["title"]
    assert post["content"] == context.post_data["content"]

@then("the post should have the current date and time as the published date")
def step_impl(context):
    post = context.response.json
    assert post["published_date"] == context.post_data["published_date"]

@then
