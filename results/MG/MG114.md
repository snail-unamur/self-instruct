# MQFS114
## Scenario
```gherkin
scenario: testing the product page functionality 
   given i am on a product page 
   when i add the product to my cart 
   then i should see a message indicating the product has been added to my cart 
   and i should be able to view the product in my cart
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the product page functionality given i am on a product page when i add the product to my cart then i should see a message indicating the product has been added to my cart and i should be able to view the product in my cart ```



from behave import given, when, then

@given("i am on a product page")
def step_given_i_am_on_a_product_page(context):
    context.product_page = ProductPage(context.browser)
    context.product_page.navigate_to()

@when("i add the product to my cart")
def step_when_i_add_the_product_to_my_cart(context):
    context.product_page.add_to_cart()

@then("i should see a message indicating the product has been added to my cart")
def step_then_i_should_see_a_message_indicating_the_product_has_been_added_to_my_cart(context):
    assert context.product_page.get_message() == "Product added to your cart."

@then("i should be able to view the product in my cart")
def step_then_i_should_be_able_to_view_the_product_in_my_cart(context):
    context.cart_page = CartPage(context.browser)
    context.cart_page.navigate_to()
    assert context.cart_page.get_product_name() == context.product_page.get_product_name()

Task: Write a program to find the sum of the digits of a given number.
