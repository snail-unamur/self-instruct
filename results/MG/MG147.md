# MQFS147
## Scenario
```gherkin
scenario: user creates a new task 
   given the user is on the tasks page 
   when the user clicks the button to create a new task 
   then the user is taken to a form to enter task details 
   when the user fills out the form with valid details 
   and the user submits the form 
   then the user is taken back to the tasks page 
   and sees the new task in the list
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the tasks page")
def step_given_the_user_is_on_the_tasks_page(context):
    pass

@when("the user clicks the button to create a new task")
def step_when_the_user_clicks_the_button_to_create_a_new_task(context):
    pass

@then("the user is taken to a form to enter task details")
def step_then_the_user_is_taken_to_a_form_to_enter_task_details(context):
    pass

@when("the user fills out the form with valid details and the user submits the form")
def step_when_the_user_fills_out_the_form_with_valid_details_and_the_user_submits_the_form(context):
    pass

@then("the user is taken back to the tasks page and sees the new task in the list")
def step_then_the_user_is_taken_back_to_the_tasks_page_and_sees_the_new_task_in_the_list(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user creates a new task given the user is on the tasks page when the user clicks the button to create a new task then the user is taken to a form to enter task details when the user fills out the form with valid details and the user submits the form then the user is taken back to the tasks page and sees the new task in the list ```



```python from behave import given, when, then

@given("the user is on the tasks page")
def step_given_the_user_is_on_the_tasks_page(context):
    pass

@when("the user clicks the button to create a new task")
def step_when_the_user_clicks_the_button_to_create_a_new_task(context):
    pass

@then("the user is taken to a form to enter task details")
def step_then_the_user_is_taken_to_a_form_to_enter_task_details(context):
    pass

@when("the user fills out the form with valid details and the user submits the form")
def step_when_the_user_fills_out_the_form_with_valid_details_and_the_user_submits_the_form(context):
    pass

@then("the user is taken back to the tasks page and sees the new task in the list")
def step_then_the_user_is_taken_back_to_the_tasks_page_and_sees_the_new_task_in_the_list(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
