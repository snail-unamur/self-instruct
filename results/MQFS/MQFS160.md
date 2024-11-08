# MQFS160
## Scenario
```gherkin
scenario: testing the create functionality 
   given a new user with name "john doe" 
   and email "[john.doe@example.com](mailto:john.doe@example.com)" 
   when i navigate to the create user page 
   then i enter the user details 
   and i click the create button 
   then the user is created 
   and visible on the user list page
```


## Python Implementation
```python
from behave import given, when, then

@given("a new user with name 'john doe' and email 'john.doe@example.com'")
def step_given_a_new_user_with_name_john_doe_and_email_john_doe_example_com(context):
    context.user = {
        "name": "john doe",
        "email": "john.doe@example.com"
    }

@when("i navigate to the create user page")
def step_when_i_navigate_to_the_create_user_page(context):
    pass

@when("i enter the user details")
def step_when_i_enter_the_user_details(context):
    pass

@when("i click the create button")
def step_when_i_click_the_create_button(context):
    pass

@then("the user is created and visible on the user list page")
def step_then_the_user_is_created_and_visible_on_the_user_list_page(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the create functionality given a new user with name "john doe" and email "[john.doe@example.com](mailto:john.doe@example.com)" when i navigate to the create user page then i enter the user details and i click the create button then the user is created and visible on the user list page ```



```python from behave import given, when, then

@given("a new user with name 'john doe' and email 'john.doe@example.com'")
def step_given_a_new_user_with_name_john_doe_and_email_john_doe_example_com(context):
    context.user = {
        "name": "john doe",
        "email": "john.doe@example.com"
    }

@when("i navigate to the create user page")
def step_when_i_navigate_to_the_create_user_page(context):
    pass

@when("i enter the user details")
def step_when_i_enter_the_user_details(context):
    pass

@when("i click the create button")
def step_when_i_click_the_create_button(context):
    pass

@then("the user is created and visible on the user list page")
def step_then_the_user_is_created_and_visible_on_the_user_list_page(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
