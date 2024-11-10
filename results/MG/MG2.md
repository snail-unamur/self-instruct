# MQFS2
## Scenario
```gherkin
scenario: user can delete a post 
   given a user has created a post 
   when they navigate to their posts page 
   and they click delete on the post 
   then the post is deleted
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has created a post")
def step_given_a_user_has_created_a_post(context):
    pass

@when("they navigate to their posts page")
def step_when_they_navigate_to_their_posts_page(context):
    pass

@when("they click delete on the post")
def step_when_they_click_delete_on_the_post(context):
    pass

@then("the post is deleted")
def step_then_the_post_is_deleted(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can delete a post given a user has created a post when they navigate to their posts page and they click delete on the post then the post is deleted ```



```python from behave import given, when, then

@given("a user has created a post")
def step_given_a_user_has_created_a_post(context):
    pass

@when("they navigate to their posts page")
def step_when_they_navigate_to_their_posts_page(context):
    pass

@when("they click delete on the post")
def step_when_they_click_delete_on_the_post(context):
    pass

@then("the post is deleted")
def step_then_the_post_is_deleted(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
