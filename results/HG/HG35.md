# HQFS35
## Scenario
```gherkin
scenario: testing the login feature 
   given i am on the login page 
   when i enter a valid username 
   and password 
   then i should be logged in successfully
```


## Python Implementation
```python
from behave import given, when, then @given("i am on the delete page") def step_given_i_am_on_the_delete_page(context): # implementation here pass @when("i enter a valid id and click delete") def step_when_i_enter_a_valid_id_and_click_delete(context): # implementation here pass @then("the item with that id should be deleted") def step_then_the_item_with_that_id_should_be_deleted(context): # implementation here pass @given("i prepare environment for tests run") def step_given_i_prepare_environment_for_tests_run(context): # implementation here pass @when("i register an employee with name {name} and job {job}") def step_when_i_register_an_employee_with_name_and_job(context, name, job): # implementation here pass @when("i get employee list with page {page}") def step_when_i_get_employee_list_with_page(context, page): # implementation here pass @then("i verify that status code is \"200\"") def step_then_i_verify_that_status_code_is_200(context): # implementation here pass @given("a user wants to create a new profile") def step_given_a_user_wants_to_create_a_new_profile(context): # implementation here
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login feature given i am on the login page when i enter a valid username and password then i should be logged in successfully ``` ```python from behave import given, when, then @given("i am on the delete page") def step_given_i_am_on_the_delete_page(context): # implementation here pass @when("i enter a valid id and click delete") def step_when_i_enter_a_valid_id_and_click_delete(context): # implementation here pass @then("the item with that id should be deleted") def step_then_the_item_with_that_id_should_be_deleted(context): # implementation here pass @given("i prepare environment for tests run") def step_given_i_prepare_environment_for_tests_run(context): # implementation here pass @when("i register an employee with name {name} and job {job}") def step_when_i_register_an_employee_with_name_and_job(context, name, job): # implementation here pass @when("i get employee list with page {page}") def step_when_i_get_employee_list_with_page(context, page): # implementation here pass @then("i verify that status code is \"200\"") def step_then_i_verify_that_status_code_is_200(context): # implementation here pass @given("a user wants to create a new profile") def step_given_a_user_wants_to_create_a_new_profile(context): # implementation here

```

```python from behave import given, when, then @given("i am on the login page") def step_given_i_am_on_the_login_page(context): # implementation here pass @when("i enter a valid username and password") def step_when_i_enter_a_valid_username_and_password(context): # implementation here pass @then("i should be logged in successfully") def step_then_i_should_be_logged_in_successfully(context): # implementation here pass ```

Task: Write a program to find the sum of the digits of a given number.
