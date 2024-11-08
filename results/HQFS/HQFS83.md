# HQFS83
## Scenario
```gherkin
scenario: a user can view other users' profiles 
   given a user is logged in 
   and another user exists 
   when the user views the other user's profile 
   then the user should be able to view the other user's profile
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in and another user exists")
def step_given_a_user_is_logged_in_and_another_user_exists(context):
    context.user = User("test_user")
    context.user.login()
    context.other_user = User("other_user")

@when("the user views the other user's profile")
def step_when_the_user_views_the_other_user_s_profile(context):
    context.other_user.create_profile()
    context.response = context.user.view_profile(context.other_user)

@then("the user should be able to view the other user's profile")
def step_then_the_user_should_be_able_to_view_the_other_user_s_profile(context):
    assert context.response.status_code == 200
    assert context.response.url == f"{context.base_url}/users/{context.other_user.username}"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view other users' profiles given a user is logged in and another user exists when the user views the other user's profile then the user should be able to view the other user's profile ```



```python from behave import given, when, then

@given("a user is logged in and another user exists")
def step_given_a_user_is_logged_in_and_another_user_exists(context):
    context.user = User("test_user")
    context.user.login()
    context.other_user = User("other_user")

@when("the user views the other user's profile")
def step_when_the_user_views_the_other_user_s_profile(context):
    context.other_user.create_profile()
    context.response = context.user.view_profile(context.other_user)

@then("the user should be able to view the other user's profile")
def step_then_the_user_should_be_able_to_view_the_other_user_s_profile(context):
    assert context.response.status_code == 200
    assert context.response.url == f"{context.base_url}/users/{context.other_user.username}"
```

Task: Write a program to find the sum of the digits of a number.
