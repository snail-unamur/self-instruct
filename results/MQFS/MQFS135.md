# MQFS135
## Scenario
```gherkin
scenario: create a new user 
   given the user does not exist 
   when i create a new user with the following details: name: 'john doe' email: 'johndoe@example.com' password: 'password123' 
   then the user is created with the following details: name: 'john doe' email: 'johndoe@example.com' password: 'password123'
```


## Python Implementation
```python
from behave import given, when, then
from steps.user_steps import UserSteps

@given('the user does not exist')
def step_impl(context):
    user_steps = UserSteps()
    user_steps.delete_user_if_exists('johndoe@example.com')

@when('i create a new user with the following details: name: "john doe" email: "johndoe@example.com" password: "password123"')
def step_impl(context):
    user_steps = UserSteps()
    user_steps.create_user('johndoe@example.com', 'password123', 'john doe')

@then('the user is created with the following details: name: "john doe" email: "johndoe@example.com" password: "password123"')
def step_impl(context):
    user_steps = UserSteps()
    user = user_steps.get_user('johndoe@example.com')
    assert user.name == 'john doe'
    assert user.email == 'johndoe@example.com'
    assert user.password == 'password123'
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given the user does not exist when i create a new user with the following details: name: 'john doe' email: 'johndoe@example.com' password: 'password123' then the user is created with the following details: name: 'john doe' email: 'johndoe@example.com' password: 'password123' ```



```python from behave import given, when, then
from steps.user_steps import UserSteps

@given('the user does not exist')
def step_impl(context):
    user_steps = UserSteps()
    user_steps.delete_user_if_exists('johndoe@example.com')

@when('i create a new user with the following details: name: "john doe" email: "johndoe@example.com" password: "password123"')
def step_impl(context):
    user_steps = UserSteps()
    user_steps.create_user('johndoe@example.com', 'password123', 'john doe')

@then('the user is created with the following details: name: "john doe" email: "johndoe@example.com" password: "password123"')
def step_impl(context):
    user_steps = UserSteps()
    user = user_steps.get_user('johndoe@example.com')
    assert user.name == 'john doe'
    assert user.email == 'johndoe@example.com'
    assert user.password == 'password123'
```

Task: Write a program to find the sum of the digits of a number.
