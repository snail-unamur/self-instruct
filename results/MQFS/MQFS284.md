# MQFS284
## Scenario
```gherkin
scenario: i can create a new user account 
   given i am on the home page 
   when i click on the create account button 
   then i should be redirected to the create account page 
   when i enter a valid email address 
   and password 
   then i should be redirected to the home page 
   when i check my email 
   then i should have received a confirmation email 
   when i click on the confirmation link 
   then i should be redirected to the home page
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the home page")
def step_given_i_am_on_the_home_page(context):
    context.home_page = HomePage(context.browser)
    context.home_page.navigate_to()

@when("i click on the create account button")
def step_when_i_click_on_the_create_account_button(context):
    context.create_account_page = context.home_page.click_create_account_button()

@when("i enter a valid email address and password")
def step_when_i_enter_a_valid_email_address_and_password(context):
    context.create_account_page.enter_email("test@example.com")
    context.create_account_page.enter_password("password")
    context.create_account_page.submit()

@then("i should be redirected to the home page")
def step_then_i_should_be_redirected_to_the_home_page(context):
    assert context.browser.current_url == context.home_page.url

@then("when i check my email then i should have received a confirmation email")
def step_then_when_i_check_my_email_then_i_should_have_received_a_confirmation_email(context):
    # TODO: Implement email checking
    pass

@then("when i click on the confirmation link then i should be redirected to the home page")
def step_then_when_i_click_on_the_confirmation_link_then_i_should_be_redirected_to_the_home_page(context):
    # TODO: Implement email link clicking
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can create a new user account given i am on the home page when i click on the create account button then i should be redirected to the create account page when i enter a valid email address and password then i should be redirected to the home page when i check my email then i should have received a confirmation email when i click on the confirmation link then i should be redirected to the home page ```



```python from behave import given, when, then

@given("i am on the home page")
def step_given_i_am_on_the_home_page(context):
    context.home_page = HomePage(context.browser)
    context.home_page.navigate_to()

@when("i click on the create account button")
def step_when_i_click_on_the_create_account_button(context):
    context.create_account_page = context.home_page.click_create_account_button()

@when("i enter a valid email address and password")
def step_when_i_enter_a_valid_email_address_and_password(context):
    context.create_account_page.enter_email("test@example.com")
    context.create_account_page.enter_password("password")
    context.create_account_page.submit()

@then("i should be redirected to the home page")
def step_then_i_should_be_redirected_to_the_home_page(context):
    assert context.browser.current_url == context.home_page.url

@then("when i check my email then i should have received a confirmation email")
def step_then_when_i_check_my_email_then_i_should_have_received_a_confirmation_email(context):
    # TODO: Implement email checking
    pass

@then("when i click on the confirmation link then i should be redirected to the home page")
def step_then_when_i_click_on_the_confirmation_link_then_i_should_be_redirected_to_the_home_page(context):
    # TODO: Implement email link clicking
    pass
```

Task: Write a program to find the sum of the digits of a given number.
