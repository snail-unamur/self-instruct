# MQFS143
## Scenario
```gherkin
scenario: a user is able to view a list of all products 
   given i am logged in to the system 
   when i click on the view products button 
   then i should be able to view a list of all products
```


## Python Implementation
```python
from behave import given, when, then

@given("i am logged in to the system")
def step_impl(context):
    context.logged_in = True

@when("i click on the view products button")
def step_impl(context):
    context.view_products_clicked = True

@then("i should be able to view a list of all products")
def step_impl(context):
    assert context.logged_in
    assert context.view_products_clicked
    assert len(context.products) > 0
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user is able to view a list of all products given i am logged in to the system when i click on the view products button then i should be able to view a list of all products ```



```python from behave import given, when, then

@given("i am logged in to the system")
def step_impl(context):
    context.logged_in = True

@when("i click on the view products button")
def step_impl(context):
    context.view_products_clicked = True

@then("i should be able to view a list of all products")
def step_impl(context):
    assert context.logged_in
    assert context.view_products_clicked
    assert len(context.products) > 0
```

Task: Write a program to find the sum of the digits of a given number.
