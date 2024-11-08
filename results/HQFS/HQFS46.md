# HQFS46
## Scenario
```gherkin
scenario: 
   given a user with the username "johndoe" 
   and the password "password123" 
   when they log in 
   then they should be logged in 
   and they should see their profile page 
   and they should see a list of their friends
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with the username 'johndoe' and the password 'password123'")
def step_given(context):
    context.user = User("johndoe", "password123")

@when("they log in")
def step_when(context):
    context.login_response = context.user.login()

@then("they should be logged in")
def step_then_1(context):
    assert context.login_response.status_code == 200

@then("they should see their profile page")
def step_then_2(context):
    context.profile_page = context.user.get_profile_page()
    assert context.profile_page is not None

@then("they should see a list of their friends")
def step_then_3(context):
    assert len(context.profile_page.friends) > 0
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user with the username "johndoe" and the password "password123" when they log in then they should be logged in and they should see their profile page and they should see a list of their friends ```



```python from behave import given, when, then

@given("a user with the username 'johndoe' and the password 'password123'")
def step_given(context):
    context.user = User("johndoe", "password123")

@when("they log in")
def step_when(context):
    context.login_response = context.user.login()

@then("they should be logged in")
def step_then_1(context):
    assert context.login_response.status_code == 200

@then("they should see their profile page")
def step_then_2(context):
    context.profile_page = context.user.get_profile_page()
    assert context.profile_page is not None

@then("they should see a list of their friends")
def step_then_3(context):
    assert len(context.profile_page.friends) > 0
```

Task: Write a program to find the sum of the digits of a number.
