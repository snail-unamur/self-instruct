# MQFS189
## Scenario
```gherkin
scenario: 
   given i am on the login page 
   when i enter the username "testuser" 
   and i enter the password "testpassword" 
   and i click on the login button 
   then i should be logged in 
   and redirected to the homepage
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the login page")
def step_given_i_am_on_the_login_page(context):
    context.browser.get("https://www.example.com/login")

@when("i enter the username 'testuser'")
def step_when_i_enter_the_username(context):
    username_field = context.browser.find_element_by_name("username")
    username_field.send_keys("testuser")

@when("i enter the password 'testpassword'")
def step_when_i_enter_the_password(context):
    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("testpassword")

@when("i click on the login button")
def step_when_i_click_on_the_login_button(context):
    login_button = context.browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

@then("i should be logged in and redirected to the homepage")
def step_then_i_should_be_logged_in_and_redirected_to_the_homepage(context):
    assert context.browser.current_url == "https://www.example.com/home"
    assert context.browser.find_element_by_xpath("//h1[contains(text(), 'Welcome')]")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i am on the login page when i enter the username "testuser" and i enter the password "testpassword" and i click on the login button then i should be logged in and redirected to the homepage ``` please note that these are just examples and you will need to modify them to fit your specific use case. also, you will need to have the necessary dependencies installed and properly configured for the behave framework to work.



```python from behave import given, when, then

@given("i am on the login page")
def step_given_i_am_on_the_login_page(context):
    context.browser.get("https://www.example.com/login")

@when("i enter the username 'testuser'")
def step_when_i_enter_the_username(context):
    username_field = context.browser.find_element_by_name("username")
    username_field.send_keys("testuser")

@when("i enter the password 'testpassword'")
def step_when_i_enter_the_password(context):
    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("testpassword")

@when("i click on the login button")
def step_when_i_click_on_the_login_button(context):
    login_button = context.browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

@then("i should be logged in and redirected to the homepage")
def step_then_i_should_be_logged_in_and_redirected_to_the_homepage(context):
    assert context.browser.current_url == "https://www.example.com/home"
    assert context.browser.find_element_by_xpath("//h1[contains(text(), 'Welcome')]")
```

Task: Write a program to find the sum of the digits of a given number.
