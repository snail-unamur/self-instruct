# HQFS149
## Scenario
```gherkin
scenario: a user can view their account details 
   given i am a registered user 
   when i visit my account details page 
   then i should see my account details including my name, email, 
   and address
```


## Python Implementation
```python
from behave import given, when, then

@given("i am a registered user")
def step_given_i_am_a_registered_user(context):
    context.user = User("John Doe", "johndoe@example.com", "123 Main St")

@when("i visit my account details page")
def step_when_i_visit_my_account_details_page(context):
    context.page = AccountDetailsPage(context.user)

@then("i should see my account details including my name, email, and address")
def step_then_i_should_see_my_account_details_including_my_name_email_and_address(context):
    assert context.page.name_field.value == context.user.name
    assert context.page.email_field.value == context.user.email
    assert context.page.address_field.value == context.user.address
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view their account details given i am a registered user when i visit my account details page then i should see my account details including my name, email, and address ``` solution:

```python
from behave import given, when, then

@given("i am a registered user")
def step_given_i_am_a_registered_user(context):
    context.user = User("John Doe", "johndoe@example.com", "123 Main St")

@when("i visit my account details page")
def step_when_i_visit_my_account_details_page(context):
    context.page = AccountDetailsPage(context.user)

@then("i should see my account details including my name, email, and address")
def step_then_i_should_see_my_account_details_including_my_name_email_and_address(context):
    assert context.page.name_field.value == context.user.name
    assert context.page.email_field.value == context.user.email
    assert context.page.address_field.value == context.user.address
```
Task: Write a program to find the sum of the digits of a given number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a given number using recursion.
