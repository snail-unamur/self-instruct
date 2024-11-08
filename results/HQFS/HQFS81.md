# HQFS81
## Scenario
```gherkin
scenario: user can edit their profile 
   given a user is logged in 
   when they navigate to their profile page 
   and they click on the "edit" button 
   then they should see a form with their current information pre-filled 
   and they can edit their information 
   and they can save their changes
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can edit their profile given a user is logged in when they navigate to their profile page and they click on the "edit" button then they should see a form with their current information pre-filled and they can edit their information and they can save their changes ```



from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.login(username=context.user.username, password="testpassword")

@when("they navigate to their profile page")
def step_impl(context):
    context.response = context.client.get("/profile/")

@when("they click on the 'edit' button")
def step_impl(context):
    context.response = context.client.get("/profile/edit/")

@then("they should see a form with their current information pre-filled")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Edit Profile" in context.response.content.decode("utf-8")
    assert context.user.first_name in context.response.content.decode("utf-8")
    assert context.user.last_name in context.response.content.decode("utf-8")
    assert context.user.email in context.response.content.decode("utf-8")

@then("they can edit their information")
def step_impl(context):
    response = context.client.post("/profile/edit/", {"first_name": "NewFirstName", "last_name": "NewLastName", "email": "newemail@example.com"})
    assert response.status_code == 302

@then("they can save their changes")
def step_impl(context):
    context.user.refresh_from_db()
    assert context.user.first_name == "NewFirstName"
    assert context.user.last_name == "NewLastName"
    assert context.user.email == "newemail@example.com"
