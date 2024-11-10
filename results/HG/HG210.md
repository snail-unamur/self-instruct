# HQFS210
## Scenario
```gherkin
scenario: i can create a new user 
   given i am on the create user page 
   when i fill in the form with valid data 
   then i can submit the form 
   and i am taken to the user details page 
   and the user details are displayed
```


## Python Implementation
```python
from behave import given, when, then @given("i am on the create user page") def step_given_i_am_on_the_create_user_page(context): # implementation here pass @when("i fill in the form with valid data") def step_when_i_fill_in_the_form_with_valid_data(context): # implementation here pass @then("i can submit the form") def step_then_i_can_submit_the_form(context): # implementation here pass @then("i am taken to the user details page") def step_then_i_am_taken_to_the_user_details_page(context): # implementation here pass @then("the user details are displayed") def step_then_the_user_details_are_displayed(context): # implementation here pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can create a new user given i am on the create user page when i fill in the form with valid data then i can submit the form and i am taken to the user details page and the user details are displayed ``` here is a possible implementation of the step functions for this scenario: ```python from behave import given, when, then @given("i am on the create user page") def step_given_i_am_on_the_create_user_page(context): # implementation here pass @when("i fill in the form with valid data") def step_when_i_fill_in_the_form_with_valid_data(context): # implementation here pass @then("i can submit the form") def step_then_i_can_submit_the_form(context): # implementation here pass @then("i am taken to the user details page") def step_then_i_am_taken_to_the_user_details_page(context): # implementation here pass @then("the user details are displayed") def step_then_the_user_details_are_displayed(context): # implementation here pass ``` the `given` step sets up the preconditions for the scenario, such as navigating to the create user page. the `when` step represents the action that the user takes, which is filling in the form with valid data. the `then` steps verify the expected outcome, which is that the user can submit the form, and that the user details are displayed on the user details page. you can then use the `behave` command to run the scenario and test the implementation. ``` behave test_i_can_create_a_new_user.py ```

Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number in a list.
