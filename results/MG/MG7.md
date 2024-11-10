# MQFS7
## Scenario
```gherkin
scenario: the user can log in with their credentials 
   given i am on the landing page 
   when i enter the email "mauricio.chaves.junior@live.com" 
   and i enter the password "123456" 
   and i click on the "log in" button 
   then i should be logged in
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the user can log in with their credentials given i am on the landing page when i enter the email "mauricio.chaves.junior@live.com" and i enter the password "123456" and i click on the "log in" button then i should be logged in ```



from behave import given, when, then

@given("i am on the landing page")
def step_given_i_am_on_the_landing_page(context):
    context.browser.get("http://www.example.com/login")

@when("i enter the email {email} and i enter the password {password} and i click on the log in button")
def step_when_i_enter_the_email_and_i_enter_the_password_and_i_click_on_the_log_in_button(context, email, password):
    email_field = context.browser.find_element_by_name("email")
    email_field.send_keys(email)
    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys(password)
    context.browser.find_element_by_name("login").click()

@then("i should be logged in")
def step_then_i_should_be_logged_in(context):
    assert context.browser.current_url == "http://www.example.com/dashboard"

Task: Write a program to find the sum of the digits of a given number.
