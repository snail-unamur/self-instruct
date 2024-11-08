# MQFS140
## Scenario
```gherkin
scenario: a user can view a list of all users 
   given a list of users 
   when a user navigates to the user list page 
   then they should see a list of all users
```


## Python Implementation
```python
from behave import given, when, then @given("a list of users") def step_impl(context): context.users = ["user1", "user2", "user3"] @when("a user navigates to the user list page") def step_impl(context): pass @then("they should see a list of all users") def step_impl(context): assert context.users == ["user1", "user2", "user3"]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a list of all users given a list of users when a user navigates to the user list page then they should see a list of all users ``` ```python from behave import given, when, then @given("a list of users") def step_impl(context): context.users = ["user1", "user2", "user3"] @when("a user navigates to the user list page") def step_impl(context): pass @then("they should see a list of all users") def step_impl(context): assert context.users == ["user1", "user2", "user3"] ```



```python from behave import given, when, then @given("a list of users") def step_impl(context): context.users = ["user1", "user2", "user3"] @when("a user navigates to the user list page") def step_impl(context): pass @then("they should see a list of all users") def step_impl(context): assert context.users == ["user1", "user2", "user3"] ```

Task: Write a program to find the sum of the digits of a number.
