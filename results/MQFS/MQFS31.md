# MQFS31
## Scenario
```gherkin
scenario: testing the add to cart functionality 
   given you are on a product page 
   when you click the add to cart button 
   then the product should be added to your cart 
   and you should see a message indicating that the product has been added 
   when you view your cart 
   then you should see the product listed there 
   when you increase the quantity of the product in your cart 
   then the total cost should be updated accordingly 
   when you decrease the quantity of the product in your cart 
   then the total cost should be updated accordingly 
   when you remove the product from your cart 
   then the product should no longer be listed there 
   and the total cost should be updated accordingly
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the add to cart functionality given you are on a product page when you click the add to cart button then the product should be added to your cart and you should see a message indicating that the product has been added when you view your cart then you should see the product listed there when you increase the quantity of the product in your cart then the total cost should be updated accordingly when you decrease the quantity of the product in your cart then the total cost should be updated accordingly when you remove the product from your cart then the product should no longer be listed there and the total cost should be updated accordingly ```



```python from behave import given, when, then

@given("you are on a product page")
def step_given_you_are_on_a_product_page(context):
    context.product_page = ProductPage()
    context.product_page.open()

@when("you click the add to cart button")
def step_when_you_click_the_add_to_cart_button(context):
    context.product_page.click_add_to_cart_button()

@then("the product should be added to your cart")
def step_then_the_product_should_be_added_to_your_cart(context):
    context.cart_page = CartPage()
    context.cart_page.open()
    assert context.cart_page.product_in_cart(context.product_page.product_name)

@then("you should see a message indicating that the product has been added")
def step_then_you_should_see_a_message_indicating_that_the_product_has_been_added(context):
    assert context.cart_page.message_displayed()

@then("when you view your cart then you should see the product listed there")
def step_then_when_you_view_your_cart_then_you_should_see_the_product_listed_there(context):
    context.cart_page.open()
    assert context.cart_page.product_in_cart(context.product_page.product_name)

@then("when you increase the quantity of the product in your cart then the total cost should be updated accordingly")
def step_then_when_you_increase_the_quantity_of_the_product_in_your_cart_then_the_total_cost_should_be_updated_accordingly(context):
    context.cart_page.increase_quantity()
    assert context.cart_page.total_cost_cost_updated()

@then("when you decrease the quantity of the product in your cart then the total cost should be updated accordingly")
def step_then_when_you_decrease_the_quantity_of_
