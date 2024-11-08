# HQFS165
## Scenario
```gherkin
scenario: create a new user 
   given i am logged in as "admin" 
   when i create a new user with the following details: |username |password |email | |user1 |password1 |user1@gmail.com | 
   then the new user should be created with the following details: |username |password |email | |user1 |password1 |user1@gmail.com | 
   and the new user should be able to log in with the following credentials: |username |password | |user1 |password1 |
```


## Python Implementation
```python
from behave import given, when, then
from features.steps.user_steps import UserSteps

@given("i am logged in as 'admin'")
def step_given_i_am_logged_in_as_admin(context):
    user_steps = UserSteps(context)
    user_steps.login_as_admin()

@when("i create a new user with the following details:")
def step_when_i_create_a_new_user_with_the_following_details(context):
    user_steps = UserSteps(context)
    user_steps.create_new_user(context.table)

@then("the new user should be created with the following details:")
def step_then_the_new_user_should_be_created_with_the_following_details(context):
    user_steps = UserSteps(context)
    user_steps.check_new_user_details(context.table)

@then("the new user should be able to log in with the following credentials:")
def step_then_the_new_user_should_be_able_to_log_in_with_the_following_credentials(context):
    user_steps = UserSteps(context)
    user_steps.login_as_new_user(context.table)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am logged in as "admin" when i create a new user with the following details: |username |password |email | |user1 |password1 |user1@gmail.com | then the new user should be created with the following details: |username |password |email | |user1 |password1 |user1@gmail.com | and the new user should be able to log in with the following credentials: |username |password | |user1 |password1 | ```



```python from behave import given, when, then
from features.steps.user_steps import UserSteps

@given("i am logged in as 'admin'")
def step_given_i_am_logged_in_as_admin(context):
    user_steps = UserSteps(context)
    user_steps.login_as_admin()

@when("i create a new user with the following details:")
def step_when_i_create_a_new_user_with_the_following_details(context):
    user_steps = UserSteps(context)
    user_steps.create_new_user(context.table)

@then("the new user should be created with the following details:")
def step_then_the_new_user_should_be_created_with_the_following_details(context):
    user_steps = UserSteps(context)
    user_steps.check_new_user_details(context.table)

@then("the new user should be able to log in with the following credentials:")
def step_then_the_new_user_should_be_able_to_log_in_with_the_following_credentials(context):
    user_steps = UserSteps(context)
    user_steps.login_as_new_user(context.table)
```

Task: Write a program to find the sum of the digits of a given number.
