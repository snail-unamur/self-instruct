# HQFS234
## Scenario
```gherkin
scenario: user account activation 
   given a user has signed up 
   when the user activates their account 
   then the user's account is activated 
   and the user is logged in 
   and the user is redirected to the homepage
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has signed up")
def step_given_a_user_has_signed_up(context):
    pass

@when("the user activates their account")
def step_when_the_user_activates_their_account(context):
    pass

@then("the user's account is activated and the user is logged in and the user is redirected to the homepage")
def step_then_the_user_s_account_is_activated_and_the_user_is_logged_in_and_the_user_is_redirected_to_the_homepage(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user account activation given a user has signed up when the user activates their account then the user's account is activated and the user is logged in and the user is redirected to the homepage ```



```python from behave import given, when, then

@given("a user has signed up")
def step_given_a_user_has_signed_up(context):
    pass

@when("the user activates their account")
def step_when_the_user_activates_their_account(context):
    pass

@then("the user's account is activated and the user is logged in and the user is redirected to the homepage")
def step_then_the_user_s_account_is_activated_and_the_user_is_logged_in_and_the_user_is_redirected_to_the_homepage(context):
    pass
```

Task: Write a program to print the first 100 prime numbers.
