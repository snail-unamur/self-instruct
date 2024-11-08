# MQFS39
## Scenario
```gherkin
scenario: user can update the quantity of an item in the shopping cart 
   given i am on the shopping cart page 
   when i update the quantity of an item 
   then the updated quantity should be saved
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the shopping cart page")
def step_given_i_am_on_the_shopping_cart_page(context):
    context.execute_steps("given i am logged in")
    context.execute_steps("given i am on the shopping cart page")

@when("i update the quantity of an item")
def step_when_i_update_the_quantity_of_an_item(context):
    context.execute_steps("when i fill in the quantity field with 5")
    context.execute_steps("when i press the update button")

@then("the updated quantity should be saved")
def step_then_the_updated_quantity_should_be_saved(context):
    assert context.response.json['quantity'] == 5
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can update the quantity of an item in the shopping cart given i am on the shopping cart page when i update the quantity of an item then the updated quantity should be saved ```



```python from behave import given, when, then

@given("i am on the shopping cart page")
def step_given_i_am_on_the_shopping_cart_page(context):
    context.execute_steps("given i am logged in")
    context.execute_steps("given i am on the shopping cart page")

@when("i update the quantity of an item")
def step_when_i_update_the_quantity_of_an_item(context):
    context.execute_steps("when i fill in the quantity field with 5")
    context.execute_steps("when i press the update button")

@then("the updated quantity should be saved")
def step_then_the_updated_quantity_should_be_saved(context):
    assert context.response.json['quantity'] == 5
```

Task: Write a program to find the sum of the digits of a given number.
