# MQFS158
## Scenario
```gherkin
scenario: user registers 
   given the user is on the registration page 
   when the user enters their name 
   and the user enters their email 
   and the user enters their password 
   and the user confirms their password 
   and the user clicks the register button 
   then the user is registered
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the registration page")
def step_given_the_user_is_on_the_registration_page(context):
    context.browser.get("http://localhost:8000/register")

@when("the user enters their name")
def step_when_the_user_enters_their_name(context):
    context.browser.find_element_by_name("name").send_keys("John Doe")

@when("the user enters their email")
def step_when_the_user_enters_their_email(context):
    context.browser.find_element_by_name("email").send_keys("johndoe@example.com")

@when("the user enters their password")
def step_when_the_user_enters_their_password(context):
    context.browser.find_element_by_name("password").send_keys("password123")

@when("the user confirms their password")
def step_when_the_user_confirms_their_password(context):
    context.browser.find_element_by_name("confirm_password").send_keys("password123")

@when("the user clicks the register button")
def step_when_the_user_clicks_the_register_button(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("the user is registered")
def step_then_the_user_is_registered(context):
    assert "Registration successful" in context.browser.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user registers given the user is on the registration page when the user enters their name and the user enters their email and the user enters their password and the user confirms their password and the user clicks the register button then the user is registered ```



```python from behave import given, when, then

@given("the user is on the registration page")
def step_given_the_user_is_on_the_registration_page(context):
    context.browser.get("http://localhost:8000/register")

@when("the user enters their name")
def step_when_the_user_enters_their_name(context):
    context.browser.find_element_by_name("name").send_keys("John Doe")

@when("the user enters their email")
def step_when_the_user_enters_their_email(context):
    context.browser.find_element_by_name("email").send_keys("johndoe@example.com")

@when("the user enters their password")
def step_when_the_user_enters_their_password(context):
    context.browser.find_element_by_name("password").send_keys("password123")

@when("the user confirms their password")
def step_when_the_user_confirms_their_password(context):
    context.browser.find_element_by_name("confirm_password").send_keys("password123")

@when("the user clicks the register button")
def step_when_the_user_clicks_the_register_button(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("the user is registered")
def step_then_the_user_is_registered(context):
    assert "Registration successful" in context.browser.page_source
```

Task: Write a program to print the first 100 prime numbers.
