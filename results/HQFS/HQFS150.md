# HQFS150
## Scenario
```gherkin
scenario: a user can view a task 
   given the user is logged in 
   when the user clicks on a task 
   then the user should see the details of the task
```


## Python Implementation
```python
from behave import given, when, then @given("the page is loaded") def step_given_the_page_is_loaded(context): pass @when("first name tag found") def step_when_first_name_tag_found(context): pass @then("enter first name") def step_then_enter_first_name(context): pass @given("i prepare environment for tests run") def step_given_i_prepare_environment_for_tests_run(context): pass @when("i register an employee with name {name} and job {job}") def step_when_i_register_an_employee_with_name_and_job(context, name, job): pass @then("i verify that status code is \"200\"") def step_then_i_verify_that_status_code_is_200(context): pass @given("a dataset is available") def step_given_a_dataset_is_available(context): pass @when("the show command is called") def step_when_the_show_command_is_called(context): pass @then("an image should pop up") def step_then_an_image_should_pop_up(context): pass @given("i have a kalibro configuration with name {name}") def step_given_i_have_a_kalibro_configuration_with_name(context, name): pass

@when("i run the kalibro analysis") def step_when_i_run_the_kalibro_analysis(context): pass
@then("i should see the results of the analysis") def step_then_i_should_see_the_results_of_the_analysis(context): pass
@given("i have a user with name {name} and password {password}") def step_given_i_have_a_user_with_name_and_password(context, name, password): pass
@when("i log in with the user") def step_when_i_log_in_with_the_user(context): pass
@then("i should be logged in") def step_then_i_should_be_logged_in(context): pass
@given("i have a task with name {name}") def step_given_i_have_a_task_with_name(context, name): pass
@when("i click on the task") def step_when_i_click_on_the_task(context): pass
@then("i should see the details of the task") def step_then_i_should_see_the_details_of_the_task(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view a task given the user is logged in when the user clicks on a task then the user should see the details of the task ``` ```python from behave import given, when, then @given("the page is loaded") def step_given_the_page_is_loaded(context): pass @when("first name tag found") def step_when_first_name_tag_found(context): pass @then("enter first name") def step_then_enter_first_name(context): pass @given("i prepare environment for tests run") def step_given_i_prepare_environment_for_tests_run(context): pass @when("i register an employee with name {name} and job {job}") def step_when_i_register_an_employee_with_name_and_job(context, name, job): pass @then("i verify that status code is \"200\"") def step_then_i_verify_that_status_code_is_200(context): pass @given("a dataset is available") def step_given_a_dataset_is_available(context): pass @when("the show command is called") def step_when_the_show_command_is_called(context): pass @then("an image should pop up") def step_then_an_image_should_pop_up(context): pass @given("i have a kalibro configuration with name {name}") def step_given_i_have_a_kalibro_configuration_with_name(context, name): pass

@when("i run the kalibro analysis") def step_when_i_run_the_kalibro_analysis(context): pass
@then("i should see the results of the analysis") def step_then_i_should_see_the_results_of_the_analysis(context): pass
@given("i have a user with name {name} and password {password}") def step_given_i_have_a_user_with_name_and_password(context, name, password): pass
@when("i log in with the user") def step_when_i_log_in_with_the_user(context): pass
@then("i should be logged in") def step_then_i_should_be_logged_in(context): pass
@given("i have a task with name {name}") def step_given_i_have_a_task_with_name(context, name): pass
@when("i click on the task") def step_when_i_click_on_the_task(context): pass
@then("i should see the details of the task") def step_then_i_should_see_the_details_of_the_task(context): pass
```

```python from behave import given, when, then @given("the user is logged in") def step_given_the_user_is_logged_in(context): pass @when("the user clicks on a task") def step_when_the_user_clicks_on_a_task(context): pass @then("the user should see the details of the task") def step_then_the_user_should_see_the_details_of_the_task(context): pass ```

Task: Write a program to find the sum of the digits of a number.
