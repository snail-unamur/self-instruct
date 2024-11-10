# HQFS216
## Scenario
```gherkin
scenario: user can view other users' profiles 
   given i am logged in 
   and there is another user 
   when i click the view profile button for that user 
   then i can see their username 
   and email
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in and there is another user")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()
    context.other_user = User("otheruser")

@when("i click the view profile button for that user")
def step_impl(context):
    context.other_user_profile = context.other_user.view_profile()

@then("i can see their username and email")
def step_impl(context):
    assert context.other_user_profile.username == "otheruser"
    assert context.other_user_profile.email == "otheruser@example.com"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can view other users' profiles given i am logged in and there is another user when i click the view profile button for that user then i can see their username and email ```



```python from behave import given, when, then

@given("i am logged in and there is another user")
def step_impl(context):
    context.user = User("testuser")
    context.user.login()
    context.other_user = User("otheruser")

@when("i click the view profile button for that user")
def step_impl(context):
    context.other_user_profile = context.other_user.view_profile()

@then("i can see their username and email")
def step_impl(context):
    assert context.other_user_profile.username == "otheruser"
    assert context.other_user_profile.email == "otheruser@example.com"
```

Task: Write a program to find the sum of the digits of a given number.
