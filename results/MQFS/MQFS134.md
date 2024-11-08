# MQFS134
## Scenario
```gherkin
scenario: testing the account creation functionality 
   given i am on the account creation page 
   when i enter the correct account details 
   then i am taken to the account creation confirmation page 
   and my account is created successfully
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the account creation page")
def step_given_i_am_on_the_account_creation_page(context):
    context.account_creation_page.navigate()

@when("i enter the correct account details")
def step_when_i_enter_the_correct_account_details(context):
    context.account_creation_page.enter_account_details()

@then("i am taken to the account creation confirmation page and my account is created successfully")
def step_then_i_am_taken_to_the_account_creation_confirmation_page_and_my_account_is_created_successfully(context):
    context.account_creation_page.submit_account_details()
    context.account_creation_confirmation_page.should_be_displayed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the account creation functionality given i am on the account creation page when i enter the correct account details then i am taken to the account creation confirmation page and my account is created successfully ```



```python from behave import given, when, then

@given("i am on the account creation page")
def step_given_i_am_on_the_account_creation_page(context):
    context.account_creation_page.navigate()

@when("i enter the correct account details")
def step_when_i_enter_the_correct_account_details(context):
    context.account_creation_page.enter_account_details()

@then("i am taken to the account creation confirmation page and my account is created successfully")
def step_then_i_am_taken_to_the_account_creation_confirmation_page_and_my_account_is_created_successfully(context):
    context.account_creation_page.submit_account_details()
    context.account_creation_confirmation_page.should_be_displayed()
```

Task: Write a program to find the sum of the digits of a given number.
