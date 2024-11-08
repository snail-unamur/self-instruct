# HQFS187
## Scenario
```gherkin
scenario: 
   given a user has a list of friends 
   when the user deletes a friend from the list 
   then the friend should no longer be in the list
```


## Python Implementation
```python
from behave import given, when, then

@given('a user has a list of friends')
def step_given_a_user_has_a_list_of_friends(context):
    context.friends = ['friend1', 'friend2', 'friend3']

@when('the user deletes a friend from the list')
def step_when_the_user_deletes_a_friend_from_the_list(context):
    context.friend_to_delete = 'friend2'
    context.friends.remove(context.friend_to_delete)

@then('the friend should no longer be in the list')
def step_then_the_friend_should_no_longer_be_in_the_list(context):
    assert context.friend_to_delete not in context.friends
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has a list of friends when the user deletes a friend from the list then the friend should no longer be in the list ```



```python from behave import given, when, then

@given('a user has a list of friends')
def step_given_a_user_has_a_list_of_friends(context):
    context.friends = ['friend1', 'friend2', 'friend3']

@when('the user deletes a friend from the list')
def step_when_the_user_deletes_a_friend_from_the_list(context):
    context.friend_to_delete = 'friend2'
    context.friends.remove(context.friend_to_delete)

@then('the friend should no longer be in the list')
def step_then_the_friend_should_no_longer_be_in_the_list(context):
    assert context.friend_to_delete not in context.friends
```

Task: Write a program to find the sum of the digits of a given number.
