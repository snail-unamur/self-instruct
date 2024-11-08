# MQFS255
## Scenario
```gherkin
scenario: create a new user 
   given i am on the registration page 
   when i fill in the registration form with valid data 
   then i should be registered 
   and logged in as a new user 
   when i am logged in as a new user 
   then i should be able to create a new task 
   when i am on the task creation page 
   then i should be able to fill in the task details 
   and i should be able to save the task 
   when i am on the task list page 
   then i should see the new task on the list
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am on the registration page when i fill in the registration form with valid data then i should be registered and logged in as a new user when i am logged in as a new user then i should be able to create a new task when i am on the task creation page then i should be able to fill in the task details and i should be able to save the task when i am on the task list page then i should see the new task on the list ```



```python from behave import given, when, then

@given("i am on the registration page")
def step_given_i_am_on_the_registration_page(context):
    context.browser.get("https://example.com/register")

@when("i fill in the registration form with valid data")
def step_when_i_fill_in_the_registration_form_with_valid_data(context):
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("email").send_keys("testuser@example.com")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_name("submit").click()

@then("i should be registered and logged in as a new user")
def step_then_i_should_be_registered_and_logged_in_as_a_new_user(context):
    assert context.browser.title == "Dashboard"

@given("i am logged in as a new user")
def step_given_i_am_logged_in_as_a_new_user(context):
    context.browser.get("https://example.com/dashboard")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_name("submit").click()

@when("i am on the task creation page")
def step_when_i_am_on_the_task_creation_page(context):
    context.browser.get("https://example.com/tasks/create")

@when("i should be able to fill in the task details and i should be able to save the task")
def step_when_i_should_be_able_to_fill_in_the_task_details_and_i_should_be_able_to_save_the_task(context):
    context.browser.find_
