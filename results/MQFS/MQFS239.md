# MQFS239
## Scenario
```gherkin
scenario: i can create a new user 
   given i am on the registration page 
   when i enter the following details: - username: "olivia" - email: "olivia@example.com" - password: "password" 
   then i should be registered as a new user
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the registration page")
def step_given_i_am_on_the_registration_page(context):
    context.browser.get('http://example.com/register')

@when("i enter the following details:")
def step_when_i_enter_the_following_details(context):
    context.browser.find_element_by_name('username').send_keys('olivia')
    context.browser.find_element_by_name('email').send_keys('olivia@example.com')
    context.browser.find_element_by_name('password').send_keys('password')

@then("i should be registered as a new user")
def step_then_i_should_be_registered_as_a_new_user(context):
    context.browser.find_element_by_name('submit').click()
    assert 'Welcome, olivia' in context.browser.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can create a new user given i am on the registration page when i enter the following details: - username: "olivia" - email: "olivia@example.com" - password: "password" then i should be registered as a new user ```



```python from behave import given, when, then

@given("i am on the registration page")
def step_given_i_am_on_the_registration_page(context):
    context.browser.get('http://example.com/register')

@when("i enter the following details:")
def step_when_i_enter_the_following_details(context):
    context.browser.find_element_by_name('username').send_keys('olivia')
    context.browser.find_element_by_name('email').send_keys('olivia@example.com')
    context.browser.find_element_by_name('password').send_keys('password')

@then("i should be registered as a new user")
def step_then_i_should_be_registered_as_a_new_user(context):
    context.browser.find_element_by_name('submit').click()
    assert 'Welcome, olivia' in context.browser.page_source
```

Task: Write a program to find the sum of the digits of a given number.
