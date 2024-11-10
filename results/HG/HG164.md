# HQFS164
## Scenario
```gherkin
scenario: delete a user from a group 
   given a user "user1" is in a group "group1" 
   when i delete "user1" from "group1" 
   then "user1" is no longer in "group1"
```


## Python Implementation
```python
from behave import given, when, then

@given("a user {user} is in a group {group}")
def step_given_a_user_is_in_a_group(context, user, group):
    context.group = Group(name=group)
    context.group.users.append(User(name=user))

@when("i delete {user} from {group}")
def step_when_i_delete_a_user_from_a_group(context, user, group):
    context.group = Group(name=group)
    user_to_delete = next(filter(lambda user: user.name == user, context.group.users))
    context.group.users.remove(user_to_delete)

@then("{user} is no longer in {group}")
def step_then_a_user_is_no_longer_in_a_group(context, user, group):
    context.group = Group(name=group)
    user_to_check = next(filter(lambda user: user.name == user, context.group.users), None)
    assert user_to_check is None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: delete a user from a group given a user "user1" is in a group "group1" when i delete "user1" from "group1" then "user1" is no longer in "group1" ```



```python from behave import given, when, then

@given("a user {user} is in a group {group}")
def step_given_a_user_is_in_a_group(context, user, group):
    context.group = Group(name=group)
    context.group.users.append(User(name=user))

@when("i delete {user} from {group}")
def step_when_i_delete_a_user_from_a_group(context, user, group):
    context.group = Group(name=group)
    user_to_delete = next(filter(lambda user: user.name == user, context.group.users))
    context.group.users.remove(user_to_delete)

@then("{user} is no longer in {group}")
def step_then_a_user_is_no_longer_in_a_group(context, user, group):
    context.group = Group(name=group)
    user_to_check = next(filter(lambda user: user.name == user, context.group.users), None)
    assert user_to_check is None
```

Task: Write a program to find the sum of the digits of a number.
