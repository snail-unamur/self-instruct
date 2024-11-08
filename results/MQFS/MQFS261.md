# MQFS261
## Scenario
```gherkin
scenario: i can view the total value of the inventory 
   given an inventory management system with a list of products 
   when i click on the total value button 
   then i should see the total value of the inventory, calculated as the sum of the quantity of each product multiplied by its price
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view the total value of the inventory given an inventory management system with a list of products when i click on the total value button then i should see the total value of the inventory, calculated as the sum of the quantity of each product multiplied by its price ```



from behave import given, when, then
from inventory_system import InventorySystem

@given("an inventory management system with a list of products")
def step(context):
    context.inventory_system = InventorySystem()

@when("i click on the total value button")
def step(context):
    context.inventory_system.click_total_value_button()

@then("i should see the total value of the inventory")
def step(context):
    assert context.inventory_system.total_value() is not None

@then("calculated as the sum of the quantity of each product multiplied by its price")
def step(context):
    total_value = 0
    for product in context.inventory_system.products:
        total_value += product.quantity * product.price
    assert context.inventory_system.total_value() == total_value


Task: Write a program to find the sum of the digits of a number.
