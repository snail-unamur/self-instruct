# HQFS270
## Scenario
```gherkin
scenario: user sets default address 
   given user is logged in 
   when user navigates to profile page 
   and user sets default address 
   then user sees default address set
```


## Python Implementation
```python
from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user navigates to profile page")
def step_impl(context):
    context.profile_page = ProfilePage(context.browser)
    context.profile_page.load()

@when("user sets default address")
def step_impl(context):
    context.profile_page.set_default_address()

@then("user sees default address set")
def step_impl(context):
    assert context.profile_page.is_default_address_set()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user sets default address given user is logged in when user navigates to profile page and user sets default address then user sees default address set ```



```python from behave import given, when, then

@given("user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("user navigates to profile page")
def step_impl(context):
    context.profile_page = ProfilePage(context.browser)
    context.profile_page.load()

@when("user sets default address")
def step_impl(context):
    context.profile_page.set_default_address()

@then("user sees default address set")
def step_impl(context):
    assert context.profile_page.is_default_address_set()
```

Task: Write a program to find the sum of the digits of a given number.
