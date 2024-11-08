# HQFS69
## Scenario
```gherkin
scenario: user password change 
   given the user is authenticated 
   when the user changes password to "newpass123" 
   then the user's password is changed to "newpass123"
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is authenticated")
def step_impl(context):
    context.user = User("testuser")
    context.user.authenticate("oldpass123")

@when("the user changes password to 'newpass123'")
def step_impl(context):
    context.user.change_password("newpass123")

@then("the user's password is changed to 'newpass123'")
def step_impl(context):
    assert context.user.check_password("newpass123")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user password change given the user is authenticated when the user changes password to "newpass123" then the user's password is changed to "newpass123" ```



```python from behave import given, when, then

@given("the user is authenticated")
def step_impl(context):
    context.user = User("testuser")
    context.user.authenticate("oldpass123")

@when("the user changes password to 'newpass123'")
def step_impl(context):
    context.user.change_password("newpass123")

@then("the user's password is changed to 'newpass123'")
def step_impl(context):
    assert context.user.check_password("newpass123")
```

Task: Write a program to find the sum of the digits of a given number.
