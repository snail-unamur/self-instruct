# MQFS172
## Scenario
```gherkin
scenario: testing the edit functionality 
   given i am logged in as an admin 
   when i edit a user with username "johndoe" 
   and i change the username to "janedoe" 
   and i click on the save button 
   then the user with username "johndoe" should now have the username "janedoe"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in as an admin")
def step_impl(context):
    context.admin = Admin()
    context.admin.login()

@when("i edit a user with username \"johndoe\"")
def step_impl(context):
    context.user = User()
    context.user.username = "johndoe"
    context.user.load()
    context.user.edit()

@when("i change the username to \"janedoe\"")
def step_impl(context):
    context.user.username = "janedoe"

@when("i click on the save button")
def step_impl(context):
    context.user.save()

@then("the user with username \"johndoe\" should now have the username \"janedoe\"")
def step_impl(context):
    user = User()
    user.username = "johndoe"
    user.load()
    assert user.username == "janedoe"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit functionality given i am logged in as an admin when i edit a user with username "johndoe" and i change the username to "janedoe" and i click on the save button then the user with username "johndoe" should now have the username "janedoe" ```



```python from behave import given, when, then

@given("i am logged in as an admin")
def step_impl(context):
    context.admin = Admin()
    context.admin.login()

@when("i edit a user with username \"johndoe\"")
def step_impl(context):
    context.user = User()
    context.user.username = "johndoe"
    context.user.load()
    context.user.edit()

@when("i change the username to \"janedoe\"")
def step_impl(context):
    context.user.username = "janedoe"

@when("i click on the save button")
def step_impl(context):
    context.user.save()

@then("the user with username \"johndoe\" should now have the username \"janedoe\"")
def step_impl(context):
    user = User()
    user.username = "johndoe"
    user.load()
    assert user.username == "janedoe"
```

Task: Write a program to find the sum of the digits of a given number.
