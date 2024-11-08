# HQFS101
## Scenario
```gherkin
scenario: user is able to add a new contact 
   given i am logged in 
   when i go to the contacts page 
   and i click on the "add contact" button 
   and i fill out the form with the following details: | name | email | phone | | john | john@gmail.com | 1234567890 | 
   then i click on the "save" button 
   then i should see the new contact in the contacts list 
   and the contact details should match the ones i entered
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    pass

@when("i go to the contacts page")
def step_impl(context):
    pass

@when("i click on the \"add contact\" button")
def step_impl(context):
    pass

@when("i fill out the form with the following details:")
def step_impl(context):
    context.execute_steps(
        """
        | Given I fill in "name" with "john"                  |
        | And I fill in "email" with "john@gmail.com"          |
        | And I fill in "phone" with "1234567890"              |
        """
    )

@when("i click on the \"save\" button")
def step_impl(context):
    pass

@then("i should see the new contact in the contacts list")
def step_impl(context):
    pass

@then("the contact details should match the ones i entered")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user is able to add a new contact given i am logged in when i go to the contacts page and i click on the "add contact" button and i fill out the form with the following details: | name | email | phone | | john | john@gmail.com | 1234567890 | then i click on the "save" button then i should see the new contact in the contacts list and the contact details should match the ones i entered ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    pass

@when("i go to the contacts page")
def step_impl(context):
    pass

@when("i click on the \"add contact\" button")
def step_impl(context):
    pass

@when("i fill out the form with the following details:")
def step_impl(context):
    context.execute_steps(
        """
        | Given I fill in "name" with "john"                  |
        | And I fill in "email" with "john@gmail.com"          |
        | And I fill in "phone" with "1234567890"              |
        """
    )

@when("i click on the \"save\" button")
def step_impl(context):
    pass

@then("i should see the new contact in the contacts list")
def step_impl(context):
    pass

@then("the contact details should match the ones i entered")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
