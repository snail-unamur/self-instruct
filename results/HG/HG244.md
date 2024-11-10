# HQFS244
## Scenario
```gherkin
scenario: user can add a new contact 
   given i am logged in 
   when i click on the "contacts" tab 
   then i should see the "add contact" button 
   when i click on the "add contact" button 
   then i should see the "add contact" form 
   when i fill out the "add contact" form with the following details: first name: "john" last name: "doe" email: "[johndoe@example.com](mailto:johndoe@example.com)" phone: "555-555-5555" 
   then i should see the confirmation message "contact added successfully"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    pass

@when("i click on the 'contacts' tab")
def step_impl(context):
    pass

@then("i should see the 'add contact' button")
def step_impl(context):
    pass

@when("i click on the 'add contact' button")
def step_impl(context):
    pass

@then("i should see the 'add contact' form")
def step_impl(context):
    pass

@when("i fill out the 'add contact' form with the following details: first name: 'john' last name: 'doe' email: '[johndoe@example.com](mailto:johndoe@example.com)' phone: '555-555-5555'")
def step_impl(context):
    pass

@then("i should see the confirmation message 'contact added successfully'")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can add a new contact given i am logged in when i click on the "contacts" tab then i should see the "add contact" button when i click on the "add contact" button then i should see the "add contact" form when i fill out the "add contact" form with the following details: first name: "john" last name: "doe" email: "[johndoe@example.com](mailto:johndoe@example.com)" phone: "555-555-5555" then i should see the confirmation message "contact added successfully" ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    pass

@when("i click on the 'contacts' tab")
def step_impl(context):
    pass

@then("i should see the 'add contact' button")
def step_impl(context):
    pass

@when("i click on the 'add contact' button")
def step_impl(context):
    pass

@then("i should see the 'add contact' form")
def step_impl(context):
    pass

@when("i fill out the 'add contact' form with the following details: first name: 'john' last name: 'doe' email: '[johndoe@example.com](mailto:johndoe@example.com)' phone: '555-555-5555'")
def step_impl(context):
    pass

@then("i should see the confirmation message 'contact added successfully'")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
