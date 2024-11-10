# MQFS159
## Scenario
```gherkin
scenario: a user can change their password 
   given i am logged in to the system 
   when i change my password to "newpassword1234" 
   then i should be able to login with email "test@example.com" 
   and password "newpassword1234"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in to the system")
def step_impl(context):
    context.user = User("test@example.com", "oldpassword1234")
    context.user.login()

@when("i change my password to {new_password}")
def step_impl(context, new_password):
    context.user.change_password(new_password)

@then("i should be able to login with email {email} and password {password}")
def step_impl(context, email, password):
    context.user = User(email, password)
    context.user.login()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can change their password given i am logged in to the system when i change my password to "newpassword1234" then i should be able to login with email "test@example.com" and password "newpassword1234" ```



```python from behave import given, when, then

@given("i am logged in to the system")
def step_impl(context):
    context.user = User("test@example.com", "oldpassword1234")
    context.user.login()

@when("i change my password to {new_password}")
def step_impl(context, new_password):
    context.user.change_password(new_password)

@then("i should be able to login with email {email} and password {password}")
def step_impl(context, email, password):
    context.user = User(email, password)
    context.user.login()
```

Task: Write a program to find the sum of the digits of a given number.
