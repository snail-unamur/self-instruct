# MQFS201
## Scenario
```gherkin
scenario: a user can view another user's profile page 
   given a user exists with the username "testuser" 
   and another user exists with the username "otheruser" 
   when the user navigates to the other user's profile page 
   then they should see the

other user's profile page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view another user's profile page given a user exists with the username "testuser" and another user exists with the username "otheruser" when the user navigates to the other user's profile page then they should see the

other user's profile page
```

from behave import given, when, then
from features.steps.steps import user_exists, other_user_exists

@given("a user exists with the username 'testuser' and another user exists with the username 'otheruser'")
def step_impl(context):
    user_exists(context, 'testuser')
    other_user_exists(context, 'otheruser')

@when("the user navigates to the other user's profile page")
def step_impl(context):
    context.browser.visit(f"/users/{other_user_exists['otheruser']}")

@then("they should see the other user's profile page")
def step_impl(context):
    assert context.browser.url == f"/users/{other_user_exists['otheruser']}"

Task: Write a program to find the sum of the digits of a given number.
