# MQFS27
## Scenario
```gherkin
scenario: a user can delete a user 
   given that the user has valid credentials 
   and the user makes a get request to /login 
   and the user makes a get request to /users 
   and the user selects a user to delete 
   then the user can delete the user 
   and the user should no longer be listed in the user list
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a user given that the user has valid credentials and the user makes a get request to /login and the user makes a get request to /users and the user selects a user to delete then the user can delete the user and the user should no longer be listed in the user list ```



```python from behave import given, when, then

@given("a user has valid credentials")
def step_given_a_user_has_valid_credentials(context):
    context.user = User("testuser", "testpassword")

@when("the user makes a get request to /login")
def step_when_the_user_makes_a_get_request_to_login(context):
    context.login_response = context.client.get("/login", headers={"Authorization": context.user.get_auth_header()})

@then("the user should be logged in")
def step_then_the_user_should_be_logged_in(context):
    assert context.login_response.status_code == 200

@when("the user makes a get request to /users")
def step_when_the_user_makes_a_get_request_to_users(context):
    context.users_response = context.client.get("/users", headers={"Authorization": context.user.get_auth_header()})

@then("the user should see a list of users")
def step_then_the_user_should_see_a_list_of_users(context):
    assert context.users_response.status_code == 200

@when("the user selects a user to delete")
def step_when_the_user_selects_a_user_to_delete(context):
    context.selected_user = context.users_response.json()[0]

@when("the user makes a delete request to /users/{user_id}".format(user_id=context.selected_user["id"]))
def step_when_the_user_makes_a_delete_request_to_users(context):
    context.delete_response = context.client.delete("/users/{}".format(context.selected_user["id"]), headers={"Authorization": context.user.get_auth_header()})

@then("the user should see a 204 response")
def step_then_the_user_should_see_a_204_response(context):
    assert context
