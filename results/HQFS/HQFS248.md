# HQFS248
## Scenario
```gherkin
scenario: editing a user's information 
   given i am on the user edit page 
   when i update the user's information 
   then the user's information should be updated
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the user edit page")
def step_impl(context):
    context.driver.get("http://localhost:8000/users/1/edit")

@when("i update the user's information")
def step_impl(context):
    context.user.first_name = "NewFirstName"
    context.user.last_name = "NewLastName"
    context.user.email = "newemail@example.com"
    context.user.save()

@then("the user's information should be updated")
def step_impl(context):
    user = User.objects.get(pk=1)
    assert user.first_name == "NewFirstName"
    assert user.last_name == "NewLastName"
    assert user.email == "newemail@example.com"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: editing a user's information given i am on the user edit page when i update the user's information then the user's information should be updated ```



```python from behave import given, when, then

@given("i am on the user edit page")
def step_impl(context):
    context.driver.get("http://localhost:8000/users/1/edit")

@when("i update the user's information")
def step_impl(context):
    context.user.first_name = "NewFirstName"
    context.user.last_name = "NewLastName"
    context.user.email = "newemail@example.com"
    context.user.save()

@then("the user's information should be updated")
def step_impl(context):
    user = User.objects.get(pk=1)
    assert user.first_name == "NewFirstName"
    assert user.last_name == "NewLastName"
    assert user.email == "newemail@example.com"
```

Task: Write a program to find the sum of the digits of a given number.
