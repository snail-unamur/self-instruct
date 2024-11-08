# HQFS110
## Scenario
```gherkin
scenario: adding a new contact to the address book 
   given an address book with the following

| first name | last name | email                 | phone number |
    | John       | Doe      | john.doe@gmail.com    | 1234567890   |
    | Jane       | Doe      | jane.doe@gmail.com    | 2345678901   |
    | John       | Smith    | john.smith@gmail.com  | 3456789012   |
    
   when a new contact is added with the following details
    | first name | last name | email                 | phone number |
    | Mary       | Smith    | mary.smith@gmail.com  | 4567890123   |
    
   then the address book should look like this
    | first name | last name | email                 | phone number |
    | John       | Doe      | john.doe@gmail.com    | 1234567890   |
    | Jane       | Doe      | jane.doe@gmail.com    | 2345678901   |
    | John       | Smith    | john.smith@gmail.com  | 3456789012   |
    | Mary       | Smith    | mary.smith@gmail.com  | 4567890123   |
```


## Python Implementation
```python
from behave import given, when, then

@given("an address book with the following")
def step(context, table):
    context.address_book = table

@when("a new contact is added with the following details")
def step(context, table):
    context.new_contact = table
    context.address_book.extend([context.new_contact.pop()])

@then("the address book should look like this")
def step(context, table):
    assert context.address_book == table
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new contact to the address book given an address book with the following

| first name | last name | email                 | phone number |
    | John       | Doe      | john.doe@gmail.com    | 1234567890   |
    | Jane       | Doe      | jane.doe@gmail.com    | 2345678901   |
    | John       | Smith    | john.smith@gmail.com  | 3456789012   |
    when a new contact is added with the following details
    | first name | last name | email                 | phone number |
    | Mary       | Smith    | mary.smith@gmail.com  | 4567890123   |
    then the address book should look like this
    | first name | last name | email                 | phone number |
    | John       | Doe      | john.doe@gmail.com    | 1234567890   |
    | Jane       | Doe      | jane.doe@gmail.com    | 2345678901   |
    | John       | Smith    | john.smith@gmail.com  | 3456789012   |
    | Mary       | Smith    | mary.smith@gmail.com  | 4567890123   |
```

```python
from behave import given, when, then

@given("an address book with the following")
def step(context, table):
    context.address_book = table

@when("a new contact is added with the following details")
def step(context, table):
    context.new_contact = table
    context.address_book.extend([context.new_contact.pop()])

@then("the address book should look like this")
def step(context, table):
    assert context.address_book == table
```

Task: Write a program to find the sum of the digits of a given number.
