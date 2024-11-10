# HQFS126
## Scenario
```gherkin
scenario: add a new user with an existing email 
   given i am logged in as "admin" 
   and there is a user with email "existinguser@gmail.com" 
   when i add a new user with email "existinguser@gmail.com" 
   and password "password" 
   then i verify that the user has not been added
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as 'admin'")
def step_impl(context):
    context.user = User(username="admin", password="password")
    context.user.login()

@given("there is a user with email 'existinguser@gmail.com'")
def step_impl(context):
    context.existing_user = User(email="existinguser@gmail.com", password="password")
    context.existing_user.create()

@when("i add a new user with email 'existinguser@gmail.com' and password 'password'")
def step_impl(context):
    context.new_user = User(email="existinguser@gmail.com", password="password")
    context.new_user.create()

@then("i verify that the user has not been added")
def step_impl(context):
    assert context.new_user.get_user() is None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new user with an existing email given i am logged in as "admin" and there is a user with email "existinguser@gmail.com" when i add a new user with email "existinguser@gmail.com" and password "password" then i verify that the user has not been added ```



```python from behave import given, when, then

@given("i am logged in as 'admin'")
def step_impl(context):
    context.user = User(username="admin", password="password")
    context.user.login()

@given("there is a user with email 'existinguser@gmail.com'")
def step_impl(context):
    context.existing_user = User(email="existinguser@gmail.com", password="password")
    context.existing_user.create()

@when("i add a new user with email 'existinguser@gmail.com' and password 'password'")
def step_impl(context):
    context.new_user = User(email="existinguser@gmail.com", password="password")
    context.new_user.create()

@then("i verify that the user has not been added")
def step_impl(context):
    assert context.new_user.get_user() is None
```

Task: Write a program to find the sum of the digits of a given number.
