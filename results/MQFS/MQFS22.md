# MQFS22
## Scenario
```gherkin
scenario: a user can delete a product from the inventory 
   given a user is logged in 
   when the user navigates to the inventory page 
   then the user should see a delete button next to each product 
   when the user clicks the delete button for a product 
   then the product should be removed from the inventory page 
   and the user should be taken back to the inventory page
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the inventory page")
def step_impl(context):
    context.page = InventoryPage()
    context.page.load()

@then("the user should see a delete button next to each product")
def step_impl(context):
    for product in context.page.products:
        assert product.delete_button

@when("the user clicks the delete button for a product")
def step_impl(context):
    product_to_delete = context.page.products[0]
    product_to_delete.delete_button.click()

@then("the product should be removed from the inventory page")
def step_impl(context):
    assert product_to_delete not in context.page.products

@then("the user should be taken back to the inventory page")
def step_impl(context):
    assert context.page.current_url == context.page.base_url + "inventory"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete a product from the inventory given a user is logged in when the user navigates to the inventory page then the user should see a delete button next to each product when the user clicks the delete button for a product then the product should be removed from the inventory page and the user should be taken back to the inventory page ```



```python from behave import given, when, then

@given("a user is logged in")
def step_impl(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the inventory page")
def step_impl(context):
    context.page = InventoryPage()
    context.page.load()

@then("the user should see a delete button next to each product")
def step_impl(context):
    for product in context.page.products:
        assert product.delete_button

@when("the user clicks the delete button for a product")
def step_impl(context):
    product_to_delete = context.page.products[0]
    product_to_delete.delete_button.click()

@then("the product should be removed from the inventory page")
def step_impl(context):
    assert product_to_delete not in context.page.products

@then("the user should be taken back to the inventory page")
def step_impl(context):
    assert context.page.current_url == context.page.base_url + "inventory"
```

Task: Write a program to find the sum of the digits of a number.
