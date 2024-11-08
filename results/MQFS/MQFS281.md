# MQFS281
## Scenario
```gherkin
scenario: a user can log out of their account 
   given i am on my dashboard page 
   when i click on the log out button 
   then i should be taken to the login page 
   and i should not be logged in
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on my dashboard page")
def step_given_i_am_on_my_dashboard_page(context):
    context.driver.get("http://localhost:3000/dashboard")

@when("i click on the log out button")
def step_when_i_click_on_the_log_out_button(context):
    context.driver.find_element_by_id("logout-button").click()

@then("i should be taken to the login page")
def step_then_i_should_be_taken_to_the_login_page(context):
    assert context.driver.current_url == "http://localhost:3000/login"

@then("i should not be logged in")
def step_then_i_should_not_be_logged_in(context):
    assert context.driver.find_elements_by_id("user-name") == []
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can log out of their account given i am on my dashboard page when i click on the log out button then i should be taken to the login page and i should not be logged in ```



```python from behave import given, when, then

@given("i am on my dashboard page")
def step_given_i_am_on_my_dashboard_page(context):
    context.driver.get("http://localhost:3000/dashboard")

@when("i click on the log out button")
def step_when_i_click_on_the_log_out_button(context):
    context.driver.find_element_by_id("logout-button").click()

@then("i should be taken to the login page")
def step_then_i_should_be_taken_to_the_login_page(context):
    assert context.driver.current_url == "http://localhost:3000/login"

@then("i should not be logged in")
def step_then_i_should_not_be_logged_in(context):
    assert context.driver.find_elements_by_id("user-name") == []
```

Task: Write a program to find the sum of the digits of a given number.
