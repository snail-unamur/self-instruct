# MQFS237
## Scenario
```gherkin
scenario: user can checkout their cart 
   given i am logged in 
   and i have products in my cart 
   when i go to the checkout page 
   then i should see a summary of my order 
   and i should be able to enter my shipping information 
   and i should be able to select a payment method 
   and i should be able to confirm my order 
   then my order should be processed 
   and i should be redirected to the order confirmation page
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    pass

@given("i have products in my cart")
def step_impl(context):
    pass

@when("i go to the checkout page")
def step_impl(context):
    pass

@then("i should see a summary of my order")
def step_impl(context):
    pass

@then("i should be able to enter my shipping information")
def step_impl(context):
    pass

@then("i should be able to select a payment method")
def step_impl(context):
    pass

@then("i should be able to confirm my order")
def step_impl(context):
    pass

@then("my order should be processed")
def step_impl(context):
    pass

@then("i should be redirected to the order confirmation page")
def step_impl(context):
    pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can checkout their cart given i am logged in and i have products in my cart when i go to the checkout page then i should see a summary of my order and i should be able to enter my shipping information and i should be able to select a payment method and i should be able to confirm my order then my order should be processed and i should be redirected to the order confirmation page ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    pass

@given("i have products in my cart")
def step_impl(context):
    pass

@when("i go to the checkout page")
def step_impl(context):
    pass

@then("i should see a summary of my order")
def step_impl(context):
    pass

@then("i should be able to enter my shipping information")
def step_impl(context):
    pass

@then("i should be able to select a payment method")
def step_impl(context):
    pass

@then("i should be able to confirm my order")
def step_impl(context):
    pass

@then("my order should be processed")
def step_impl(context):
    pass

@then("i should be redirected to the order confirmation page")
def step_impl(context):
    pass
```

Task: Write a program to find the sum of the digits of a given number.
