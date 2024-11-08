# HQFS256
## Scenario
```gherkin
scenario: 
   given a user has an account 
   when the user tries to log in with an incorrect password 
   then the user should not be able to log in examples: |username|password|expected result| |testuser1|wrongpassword1|login failed| |testuser2|wrongpassword2|login failed|
```


## Python Implementation
```python
from behave import given, when, then @given("a user has an account") def step_given_a_user_has_an_account(context): pass @when("the user tries to log in with an incorrect password") def step_when_the_user_tries_to_log_in_with_an_incorrect_password(context): pass @then("the user should not be able to log in") def step_then_the_user_should_not_be_able_to_log_in(context): pass @given("i prepare environment for tests run") def step_given_i_prepare_environment_for_tests_run(context): pass @when("i search the employee -1") def step_when_i_search_the_employee_1(context): pass @then("i verify that status code is \"404\"") def step_then_i_verify_that_status_code_is_404(context): pass @given("the user is on the homepage") def step_given_the_user_is_on_the_homepage(context): pass @when("the user clicks on the \"products\" link") def step_when_the_user_clicks_on_the_products_link(context):
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has an account when the user tries to log in with an incorrect password then the user should not be able to log in examples: |username|password|expected result| |testuser1|wrongpassword1|login failed| |testuser2|wrongpassword2|login failed| ``` ```python from behave import given, when, then @given("a user has an account") def step_given_a_user_has_an_account(context): pass @when("the user tries to log in with an incorrect password") def step_when_the_user_tries_to_log_in_with_an_incorrect_password(context): pass @then("the user should not be able to log in") def step_then_the_user_should_not_be_able_to_log_in(context): pass @given("i prepare environment for tests run") def step_given_i_prepare_environment_for_tests_run(context): pass @when("i search the employee -1") def step_when_i_search_the_employee_1(context): pass @then("i verify that status code is \"404\"") def step_then_i_verify_that_status_code_is_404(context): pass @given("the user is on the homepage") def step_given_the_user_is_on_the_homepage(context): pass @when("the user clicks on the \"products\" link") def step_when_the_user_clicks_on_the_products_link(context):

```

```python from behave import given, when, then @given("a user has an account") def step_given_a_user_has_an_account(context): pass @when("the user tries to log in with an incorrect password") def step_when_the_user_tries_to_log_in_with_an_incorrect_password(context): context.username = "testuser1" context.password = "wrongpassword1" @then("the user should not be able to log in") def step_then_the_user_should_not_be_able_to_log_in(context): assert context.result == "login failed"
```

Task: Write a program to find the sum of the digits of a given number.
