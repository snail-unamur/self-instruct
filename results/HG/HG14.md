# HQFS14
## Scenario
```gherkin
scenario: user is able to create a new account with correct credentials 
   given the user is on the signup page 
   when the user enters the correct credentials 
   then the user should be able to create a new account successfully
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user is able to create a new account with correct credentials given the user is on the signup page when the user enters the correct credentials then the user should be able to create a new account successfully ``` here are the python implementations of the step functions for the given gherkin scenarios using the behave bdd testing framework:



from behave import given, when, then

@given("the user is on the signup page")
def step_given_the_user_is_on_the_signup_page(context):
    context.browser.get("https://www.example.com/signup")

@when("the user enters the correct credentials")
def step_when_the_user_enters_the_correct_credentials(context):
    username_field = context.browser.find_element_by_name("username")
    password_field = context.browser.find_element_by_name("password")
    username_field.send_keys("correct_username")
    password_field.send_keys("correct_password")

@then("the user should be able to create a new account successfully")
def step_then_the_user_should_be_able_to_create_a_new_account_successfully(context):
    submit_button = context.browser.find_element_by_name("submit")
    submit_button.click()
    assert "Account Created" in context.browser.page_source

Task: Write a program to find the sum of the digits of a given number.
