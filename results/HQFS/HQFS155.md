# HQFS155
## Scenario
```gherkin
scenario: create a new user 
   given i am on the create user page 
   when i fill in the form with the following details: first name: "john" last name: "doe" email: "[johndoe@example.com](mailto:johndoe@example.com)" password: "password" 
   then i should see the confirmation message "user created successfully"
```


## Python Implementation
```python
from behave import given, when, then @given("namespace 'deletion' exists") def step_given_namespace_exists(context): # implementation to check if namespace 'deletion' exists pass @when("i delete a namespace 'deletion'") def step_when_delete_namespace(context): # implementation to delete namespace 'deletion' pass @then("the namespace is deleted and i can no longer access it") def step_then_namespace_deleted(context): # implementation to check if namespace 'deletion' is deleted pass @then("i should be redirected to the homepage with a message 'namespace 'deletion' has been deleted'") def step_then_redirected_homepage(context): # implementation to check if redirected to homepage with message pass @then("i should see a confirmation message") def step_then_confirmation_message(context): # implementation to check if confirmation message is displayed pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am on the create user page when i fill in the form with the following details: first name: "john" last name: "doe" email: "[johndoe@example.com](mailto:johndoe@example.com)" password: "password" then i should see the confirmation message "user created successfully" ``` here are the python implementations of the step functions for the given gherkin scenarios using the behave bdd testing framework: 1. ```python from behave import given, when, then @given("namespace 'deletion' exists") def step_given_namespace_exists(context): # implementation to check if namespace 'deletion' exists pass @when("i delete a namespace 'deletion'") def step_when_delete_namespace(context): # implementation to delete namespace 'deletion' pass @then("the namespace is deleted and i can no longer access it") def step_then_namespace_deleted(context): # implementation to check if namespace 'deletion' is deleted pass @then("i should be redirected to the homepage with a message 'namespace 'deletion' has been deleted'") def step_then_redirected_homepage(context): # implementation to check if redirected to homepage with message pass @then("i should see a confirmation message") def step_then_confirmation_message(context): # implementation to check if confirmation message is displayed pass ``` 2. ```

from behave import given, when, then

@given("i am on the create user page")
def step_given_on_create_user_page(context):
    # implementation to navigate to create user page
    pass

@when("i fill in the form with the following details: first name: {first_name} last name: {last_name} email: {email} password: {password}")
def step_when_fill_form(context, first_name, last_name, email, password):
    # implementation to fill the form with given details
    pass

@then("i should see the confirmation message {message}")
def step_then_confirmation_message(context, message):
    # implementation to check if confirmation message is displayed
    pass
```

Task: Write a program to find the sum of the digits of a given number.

def sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a given number using recursion.
