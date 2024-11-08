# HQFS200
## Scenario
```gherkin
scenario: user can register 
   given user "johndoe" does not exist 
   when user "johndoe" registers with password "password123" 
   then user "johndoe" exists with password "password123"
```


## Python Implementation
```python
from behave import given, when, then

@given("user {username} does not exist")
def step_given_user_does_not_exist(context, username):
    context.user = User(username)
    context.user_repo = UserRepository()
    context.user_repo.add(context.user)

@when("user {username} registers with password {password}")
def step_when_user_registers(context, username, password):
    context.user.register(password)

@then("user {username} exists with password {password}")
def step_then_user_exists(context, username, password):
    user = context.user_repo.get(username)
    assert user.password == password
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can register given user "johndoe" does not exist when user "johndoe" registers with password "password123" then user "johndoe" exists with password "password123" ```



```python from behave import given, when, then

@given("user {username} does not exist")
def step_given_user_does_not_exist(context, username):
    context.user = User(username)
    context.user_repo = UserRepository()
    context.user_repo.add(context.user)

@when("user {username} registers with password {password}")
def step_when_user_registers(context, username, password):
    context.user.register(password)

@then("user {username} exists with password {password}")
def step_then_user_exists(context, username, password):
    user = context.user_repo.get(username)
    assert user.password == password
```

Task: Write a program to find the sum of the digits of a number.
