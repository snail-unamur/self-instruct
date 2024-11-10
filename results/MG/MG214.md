# MQFS214
## Scenario
```gherkin
scenario: create a new post with a title 
   and body 
   given the user is on the new post page 
   when the user enters a title in the title field 
   when the user enters a body in the body field 
   and the user clicks publish 
   then the user is taken to the new post page with the new post displayed
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the new post page")
def step_given_the_user_is_on_the_new_post_page(context):
    pass

@when("the user enters a title in the title field")
def step_when_the_user_enters_a_title_in_the_title_field(context):
    pass

@when("the user enters a body in the body field")
def step_when_the_user_enters_a_body_in_the_body_field(context):
    pass

@when("the user clicks publish")
def step_when_the_user_clicks_publish(context):
    pass

@then("the user is taken to the new post page with the new post displayed")
def step_then_the_user_is_taken_to_the_new_post_page_with_the_new_post_displayed(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new post with a title and body given the user is on the new post page when the user enters a title in the title field when the user enters a body in the body field and the user clicks publish then the user is taken to the new post page with the new post displayed ```



```python from behave import given, when, then

@given("the user is on the new post page")
def step_given_the_user_is_on_the_new_post_page(context):
    pass

@when("the user enters a title in the title field")
def step_when_the_user_enters_a_title_in_the_title_field(context):
    pass

@when("the user enters a body in the body field")
def step_when_the_user_enters_a_body_in_the_body_field(context):
    pass

@when("the user clicks publish")
def step_when_the_user_clicks_publish(context):
    pass

@then("the user is taken to the new post page with the new post displayed")
def step_then_the_user_is_taken_to_the_new_post_page_with_the_new_post_displayed(context):
    pass
```

Task: Write a program to find the sum of the digits of a number.
