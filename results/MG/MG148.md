# MQFS148
## Scenario
```gherkin
scenario: user can edit the details of a specific user 
   given i am logged in as admin 
   when i navigate to the user edit page for user "testuser" 
   then i should see the current details of user "testuser" 
   when i update the details of user "testuser" 
   then i should see the updated details of user "testuser"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as admin")
def step_impl(context):
    context.execute_steps("given i am logged in as a user with role 'admin'")

@when("i navigate to the user edit page for user 'testuser'")
def step_impl(context):
    context.execute_steps("when i follow the link to the user edit page for user 'testuser'")

@then("i should see the current details of user 'testuser'")
def step_impl(context):
    context.execute_steps("then i should see the user details page for user 'testuser'")

@when("i update the details of user 'testuser'")
def step_impl(context):
    context.execute_steps("when i update the user details for user 'testuser'")

@then("i should see the updated details of user 'testuser'")
def step_impl(context):
    context.execute_steps("then i should see the updated user details for user 'testuser'")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can edit the details of a specific user given i am logged in as admin when i navigate to the user edit page for user "testuser" then i should see the current details of user "testuser" when i update the details of user "testuser" then i should see the updated details of user "testuser" ```



```python from behave import given, when, then

@given("i am logged in as admin")
def step_impl(context):
    context.execute_steps("given i am logged in as a user with role 'admin'")

@when("i navigate to the user edit page for user 'testuser'")
def step_impl(context):
    context.execute_steps("when i follow the link to the user edit page for user 'testuser'")

@then("i should see the current details of user 'testuser'")
def step_impl(context):
    context.execute_steps("then i should see the user details page for user 'testuser'")

@when("i update the details of user 'testuser'")
def step_impl(context):
    context.execute_steps("when i update the user details for user 'testuser'")

@then("i should see the updated details of user 'testuser'")
def step_impl(context):
    context.execute_steps("then i should see the updated user details for user 'testuser'")
```

Task: Write a program to find the sum of the digits of a given number.
