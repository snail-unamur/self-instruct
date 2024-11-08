# HQFS167
## Scenario
```gherkin
scenario: 
   given a user has an account 
   when the user tries to log in with the correct credentials 
   then the user should be able to log in 
   and the user should be redirected to the homepage 
   and the user should see a welcome message 
   and the user should see a list of their projects
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has an account when the user tries to log in with the correct credentials then the user should be able to log in and the user should be redirected to the homepage and the user should see a welcome message and the user should see a list of their projects ```



from behave import given, when, then

@given("a user has an account")
def step_given_a_user_has_an_account(context):
    context.user = User()
    context.user.login("username", "password")

@when("the user tries to log in with the correct credentials")
def step_when_the_user_tries_to_log_in_with_the_correct_credentials(context):
    context.response = context.user.post("/login", {"username": "username", "password": "password"})

@then("the user should be able to log in")
def step_then_the_user_should_be_able_to_log_in(context):
    assert context.response.status_code == 200

@then("the user should be redirected to the homepage")
def step_then_the_user_should_be_redirected_to_the_homepage(context):
    assert context.response.headers["Location"] == "/"

@then("the user should see a welcome message")
def step_then_the_user_should_see_a_welcome_message(context):
    assert "Welcome" in context.response.text

@then("the user should see a list of their projects")
def step_then_the_user_should_see_a_list_of_their_projects(context):
    assert "Project 1" in context.response.text
    assert "Project 2" in context.response.text


Task: Write a program to find the sum of the digits of a number.
