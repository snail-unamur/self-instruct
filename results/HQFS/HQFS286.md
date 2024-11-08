# HQFS286
## Scenario
```gherkin
scenario: the user can log in with the correct credentials 
   given i am on the login page 
   then i fill in the email field with "kea@gmail.com" 
   and i fill in the password field with "123456" 
   and i press the login button 
   then i should be logged in
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the user can log in with the correct credentials given i am on the login page then i fill in the email field with "kea@gmail.com" and i fill in the password field with "123456" and i press the login button then i should be logged in ```



from behave import given, when, then

@given("i am on the login page")
def step_given_i_am_on_the_login_page(context):
    pass

@when("i fill in the email field with {email}")
def step_when_i_fill_in_the_email_field_with(context, email):
    context.email_field.send_keys(email)

@when("i fill in the password field with {password}")
def step_when_i_fill_in_the_password_field_with(context, password):
    context.password_field.send_keys(password)

@when("i press the login button")
def step_when_i_press_the_login_button(context):
    context.login_button.click()

@then("i should be logged in")
def step_then_i_should_be_logged_in(context):
    assert context.login_successful


Task: Write a program to find the sum of the digits of a given number.
