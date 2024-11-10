# MQFS35
## Scenario
```gherkin
scenario: testing the product management functionality 
   given i am an admin 
   when i go to the product management page 
   then i should see a list of all products 
   when i add a new product 
   then i should see the new product in the list 
   when i
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the product management functionality given i am an admin when i go to the product management page then i should see a list of all products when i add a new product then i should see the new product in the list when i

```

from behave import given, when, then

@given("i am an admin")
def step_given_i_am_an_admin(context):
    context.admin = Admin()
    context.admin.login()

@when("i go to the product management page")
def step_when_i_go_to_the_product_management_page(context):
    context.product_page = ProductPage()
    context.product_page.open()

@then("i should see a list of all products")
def step_then_i_should_see_a_list_of_all_products(context):
    assert context.product_page.is_products_displayed()

@when("i add a new product")
def step_when_i_add_a_new_product(context):
    context.new_product = Product()
    context.product_page.add_product(context.new_product)

@then("i should see the new product in the list")
def step_then_i_should_see_the_new_product_in_the_list(context):
    assert context.new_product in context.product_page.get_products()

Task: Write a program to find the sum of the digits of a number.
