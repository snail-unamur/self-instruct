# HQFS203
## Scenario
```gherkin
scenario: i can view a user's account balance 
   given a user with account balance of 100 
   when i navigate to the user's account page 
   then i should see the user's account balance of 100
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with account balance of 100")
def step_impl(context):
    context.user = User("test_user")
    context.user.balance = 100

@when("i navigate to the user's account page")
def step_impl(context):
    context.account_page = AccountPage(context.browser)
    context.account_page.navigate_to()

@then("i should see the user's account balance of 100")
def step_impl(context):
    assert context.account_page.get_balance() == 100
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view a user's account balance given a user with account balance of 100 when i navigate to the user's account page then i should see the user's account balance of 100 ```



```python from behave import given, when, then

@given("a user with account balance of 100")
def step_impl(context):
    context.user = User("test_user")
    context.user.balance = 100

@when("i navigate to the user's account page")
def step_impl(context):
    context.account_page = AccountPage(context.browser)
    context.account_page.navigate_to()

@then("i should see the user's account balance of 100")
def step_impl(context):
    assert context.account_page.get_balance() == 100
```

Task: Write a program to print the first 100 prime numbers.
