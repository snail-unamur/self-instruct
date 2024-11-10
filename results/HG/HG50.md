# HQFS50
## Scenario
```gherkin
scenario: 
   when i try to login with wrong credentials 
   given i am on the login page 
   when i fill the username field with "wrong_username" 
   when i fill the password field with "wrong_password" 
   when i click on the login button 
   then i should be redirected to the login page with the message "invalid username or password"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the login page")
def step_given_i_am_on_the_login_page(context):
    context.driver.get("https://example.com/login")

@when("i fill the username field with {username}")
def step_when_i_fill_the_username_field_with(context, username):
    context.username_field = context.driver.find_element_by_name("username")
    context.username_field.send_keys(username)

@when("i fill the password field with {password}")
def step_when_i_fill_the_password_field_with(context, password):
    context.password_field = context.driver.find_element_by_name("password")
    context.password_field.send_keys(password)

@when("i click on the login button")
def step_when_i_click_on_the_login_button(context):
    context.login_button = context.driver.find_element_by_xpath("//button[@type='submit']")
    context.login_button.click()

@then("i should be redirected to the login page with the message {message}")
def step_then_i_should_be_redirected_to_the_login_page_with_the_message(context, message):
    context.assertIn(message, context.driver.page_source)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: when i try to login with wrong credentials given i am on the login page when i fill the username field with "wrong_username" when i fill the password field with "wrong_password" when i click on the login button then i should be redirected to the login page with the message "invalid username or password" ```



```python from behave import given, when, then

@given("i am on the login page")
def step_given_i_am_on_the_login_page(context):
    context.driver.get("https://example.com/login")

@when("i fill the username field with {username}")
def step_when_i_fill_the_username_field_with(context, username):
    context.username_field = context.driver.find_element_by_name("username")
    context.username_field.send_keys(username)

@when("i fill the password field with {password}")
def step_when_i_fill_the_password_field_with(context, password):
    context.password_field = context.driver.find_element_by_name("password")
    context.password_field.send_keys(password)

@when("i click on the login button")
def step_when_i_click_on_the_login_button(context):
    context.login_button = context.driver.find_element_by_xpath("//button[@type='submit']")
    context.login_button.click()

@then("i should be redirected to the login page with the message {message}")
def step_then_i_should_be_redirected_to_the_login_page_with_the_message(context, message):
    context.assertIn(message, context.driver.page_source)
```

Task: Write a program to find the sum of the digits of a given number.
