# HQFS65
## Scenario
```gherkin
scenario: update a user's data 
   given i am on the user update page 
   and i am logged in as an admin 
   when i update the user data with the following data |first name|last name|email|password| |mauricio|chaves|mauricio.chaves.jun

ior@gmail.com|password123|

   then the user's data should be updated
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: update a user's data given i am on the user update page and i am logged in as an admin when i update the user data with the following data |first name|last name|email|password| |mauricio|chaves|mauricio.chaves.jun

ior@gmail.com|password123|
then the user's data should be updated
```

from behave import given, when, then
from behave.runner import Context

@given("i am on the user update page")
def step_impl(context: Context):
    context.update_page.navigate()

@given("i am logged in as an admin")
def step_impl(context: Context):
    context.login_page.login_as_admin()

@when("i update the user data with the following data")
def step_impl(context: Context):
    context.update_page.update_user_data(
        first_name="mauricio",
        last_name="chaves",
        email="mauricio.chaves.junior@gmail.com",
        password="password123",
    )

@then("the user's data should be updated")
def step_impl(context: Context):
    assert context.update_page.is_user_data_updated()


Task: Write a program to find the sum of the digits of a number.
