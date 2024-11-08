# HQFS227
## Scenario
```gherkin
scenario: 
   given a user is logged in 
   when they view their profile 
   then they should see their name 
   and email address 
   and they should see a button to edit their profile 
   and 
   when they click on the edit profile button 
   then they should see a form to edit their name 
   and email address 
   and 
   when they submit the form with new values 
   then their profile should be updated with the new values 
   and they should be redirected to their updated profile page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is logged in when they view their profile then they should see their name and email address and they should see a button to edit their profile and when they click on the edit profile button then they should see a form to edit their name and email address and when they submit the form with new values then their profile should be updated with the new values and they should be redirected to their updated profile page ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.response = login(context.browser, context.user.username, "testpassword")

@when("they view their profile")
def step_impl(context):
    context.response = context.browser.get(context.base_url + reverse("profile"))

@then("they should see their name and email address")
def step_impl(context):
    assert context.response.context["user"].username in context.response.content.decode()
    assert context.response.context["user"].email in context.response.content.decode()

@then("they should see a button to edit their profile")
def step_impl(context):
    assert b"Edit Profile" in context.response.content

@when("they click on the edit profile button")
def step_impl(context):
    context.response = context.browser.click_link_by_partial_href("edit")

@then("they should see a form to edit their name and email address")
def step_impl(context):
    assert b"Edit Profile" in context.response.content
    assert b"Name" in context.response.content
    assert b"Email" in context.response.content

@when("they submit the form with new values")
def step_impl(context):
    context.browser.choose("select[name='role']", "User")
    context.browser.fill("name", "New Name")
    context.browser.fill("email", "newemail@example.com")
    context.response = context.browser.submit_form()

@then("their profile should be updated with the new values")
def step_impl(context):
    user = User.objects.get(username="testuser")
    assert user.username == "New Name"
    assert user.email == "newemail@example.com"

@then("they should be redirected to their updated profile page")
def step_impl(context):
    assert context.browser.url == context.base_url + reverse
