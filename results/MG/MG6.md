# MQFS6
## Scenario
```gherkin
scenario: testing the cart functionality 
   given i am on the product page 
   when i add a product to the cart 
   and i go to the cart page 
   then i should see the product in the cart 
   when i remove the product from the cart 
   then i should not see the product in the cart
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the cart functionality given i am on the product page when i add a product to the cart and i go to the cart page then i should see the product in the cart when i remove the product from the cart then i should not see the product in the cart ```



from behave import given, when, then

@given("i am on the product page")
def step_given_i_am_on_the_product_page(context):
    context.product_page = ProductPage()
    context.product_page.navigate()

@when("i add a product to the cart")
def step_when_i_add_a_product_to_the_cart(context):
    context.product = context.product_page.add_product_to_cart()

@when("i go to the cart page")
def step_when_i_go_to_the_cart_page(context):
    context.cart_page = CartPage()
    context.cart_page.open()

@then("i should see the product in the cart")
def step_then_i_should_see_the_product_in_the_cart(context):
    assert context.cart_page.product_in_cart(context.product)

@when("i remove the product from the cart")
def step_when_i_remove_the_product_from_the_cart(context):
    context.cart_page.remove_product_from_cart(context.product)

@then("i should not see the product in the cart")
def step_then_i_should_not_see_the_product_in_the_cart(context):
    assert not context.cart_page.product_in_cart(context.product)


Task: Write a program to find the sum of the digits of a number.
