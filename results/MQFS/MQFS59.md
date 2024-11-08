# MQFS59
## Scenario
```gherkin
scenario: user can update their profile 
   given i am logged in as a user 
   when i navigate to my profile page 
   then i should see an edit button 
   when i click the edit button 
   then i should see fields to update my username, email, 
   and password 
   when i update the fields 
   and click save 
   then my profile should be updated with the new information
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can update their profile given i am logged in as a user when i navigate to my profile page then i should see an edit button when i click the edit button then i should see fields to update my username, email, and password when i update the fields and click save then my profile should be updated with the new information ```



from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.login(username=context.user.username, password="testpassword")

@when("i navigate to my profile page")
def step_impl(context):
    context.response = context.client.get("/profile/")

@then("i should see an edit button")
def step_impl(context):
    assert context.response.context["user"] == context.user
    assert context.response.status_code == 200
    assert "Edit Profile" in context.response.content.decode("utf-8")

@when("i click the edit button")
def step_impl(context):
    context.response = context.client.get("/profile/edit/")

@then("i should see fields to update my username, email, and password")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Username" in context.response.content.decode("utf-8")
    assert "Email" in context.response.content.decode("utf-8")
    assert "Password" in context.response.content.decode("utf-8")

@when("i update the fields and click save")
def step_impl(context):
    context.response = context.client.post(
        "/profile/edit/",
        {
            "username": "newusername",
            "email": "newemail@example.com",
            "password": "newpassword",
        },
    )

@then("my profile should be updated with the new information")
def step_impl(context):
    context.user.refresh_from_db()
    assert context.user.username == "newusername"
    assert context.user.email == "newemail@example.com"
    assert context.user.check_password("newpassword")
