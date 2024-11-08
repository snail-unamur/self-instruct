# HQFS185
## Scenario
```gherkin
scenario: a user can follow 
   and unfollow another user 
   given a user "alice" 
   and a user "bob" 
   when alice follows bob 
   then bob is followed by alice 
   and alice is following bob 
   when alice unfollows bob 
   then bob is no longer followed by alice 
   and alice is no longer following bob
```


## Python Implementation
```python
from behave import given, when, then
from features.steps.user_steps import UserSteps

@given("a user {user1} and a user {user2}")
def step_impl(context, user1, user2):
    context.user1 = UserSteps(user1)
    context.user2 = UserSteps(user2)

@when("{user1} follows {user2}")
def step_impl(context, user1, user2):
    context.user1.follow(context.user2)

@then("{user2} is followed by {user1} and {user1} is following {user2}")
def step_impl(context, user1, user2):
    assert context.user2.is_followed_by(context.user1)
    assert context.user1.is_following(context.user2)

@when("{user1} unfollows {user2}")
def step_impl(context, user1, user2):
    context.user1.unfollow(context.user2)

@then("{user2} is no longer followed by {user1} and {user1} is no longer following {user2}")
def step_impl(context, user1, user2):
    assert not context.user2.is_followed_by(context.user1)
    assert not context.user1.is_following(context.user2)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can follow and unfollow another user given a user "alice" and a user "bob" when alice follows bob then bob is followed by alice and alice is following bob when alice unfollows bob then bob is no longer followed by alice and alice is no longer following bob ```



```python from behave import given, when, then
from features.steps.user_steps import UserSteps

@given("a user {user1} and a user {user2}")
def step_impl(context, user1, user2):
    context.user1 = UserSteps(user1)
    context.user2 = UserSteps(user2)

@when("{user1} follows {user2}")
def step_impl(context, user1, user2):
    context.user1.follow(context.user2)

@then("{user2} is followed by {user1} and {user1} is following {user2}")
def step_impl(context, user1, user2):
    assert context.user2.is_followed_by(context.user1)
    assert context.user1.is_following(context.user2)

@when("{user1} unfollows {user2}")
def step_impl(context, user1, user2):
    context.user1.unfollow(context.user2)

@then("{user2} is no longer followed by {user1} and {user1} is no longer following {user2}")
def step_impl(context, user1, user2):
    assert not context.user2.is_followed_by(context.user1)
    assert not context.user1.is_following(context.user2)
```

Task: Write a program to find the sum of the digits of a number.
