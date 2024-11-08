# HQFS214
## Scenario
```gherkin
scenario: a user can log in with their credentials 
   given i am a user with username "testuser" 
   and password "testpassword" 
   when i log in with my credentials 
   then i am logged in with my username "testuser" 
   and password "testpassword"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can log in with their credentials given i am a user with username "testuser" and password "testpassword" when i log in with my credentials then i am logged in with my username "testuser" and password "testpassword" ``` here are the python implementations of the step functions for each gherkin scenario:



from behave import given, when, then

@given("i am a user with username {username} and password {password}")
def step_impl(context, username, password):
    context.user = User(username, password)

@when("i log in with my credentials")
def step_impl(context):
    context.response = context.user.login()

@then("i am logged in with my username {username} and password {password}")
def step_impl(context, username, password):
    assert context.response.status_code == 200
    assert context.response.json()["username"] == username
    assert context.response.json()["password"] == password

Task: Write a program to find the sum of the digits of a number.
