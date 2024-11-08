# MQFS122
## Scenario
```gherkin
scenario: create a new user 
   given i am on the create user page 
   when i fill in the user creation form with valid information 
   then i should be taken to the user profile page 
   and i should see the user's name 
   and i should see the user's email address
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the create user page")
def step_given_i_am_on_the_create_user_page(context):
    context.browser.get("http://localhost:8000/users/new")

@when("i fill in the user creation form with valid information")
def step_when_i_fill_in_the_user_creation_form_with_valid_information(context):
    context.browser.find_element_by_name("name").send_keys("John Doe")
    context.browser.find_element_by_name("email").send_keys("johndoe@example.com")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be taken to the user profile page")
def step_then_i_should_be_taken_to_the_user_profile_page(context):
    assert context.browser.current_url == "http://localhost:8000/users/1"

@then("i should see the user's name")
def step_then_i_should_see_the_user_s_name(context):
    assert context.browser.find_element_by_xpath("//h1").text == "John Doe"

@then("i should see the user's email address")
def step_then_i_should_see_the_user_s_email_address(context):
    assert context.browser.find_element_by_xpath("//p").text == "johndoe@example.com"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am on the create user page when i fill in the user creation form with valid information then i should be taken to the user profile page and i should see the user's name and i should see the user's email address ```



```python from behave import given, when, then

@given("i am on the create user page")
def step_given_i_am_on_the_create_user_page(context):
    context.browser.get("http://localhost:8000/users/new")

@when("i fill in the user creation form with valid information")
def step_when_i_fill_in_the_user_creation_form_with_valid_information(context):
    context.browser.find_element_by_name("name").send_keys("John Doe")
    context.browser.find_element_by_name("email").send_keys("johndoe@example.com")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be taken to the user profile page")
def step_then_i_should_be_taken_to_the_user_profile_page(context):
    assert context.browser.current_url == "http://localhost:8000/users/1"

@then("i should see the user's name")
def step_then_i_should_see_the_user_s_name(context):
    assert context.browser.find_element_by_xpath("//h1").text == "John Doe"

@then("i should see the user's email address")
def step_then_i_should_see_the_user_s_email_address(context):
    assert context.browser.find_element_by_xpath("//p").text == "johndoe@example.com"
```

Task: Write a program to find the sum of the digits of a given number.
