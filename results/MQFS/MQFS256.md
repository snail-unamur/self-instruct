# MQFS256
## Scenario
```gherkin
scenario: testing the functionality of the "remove from cart" button 
   given i am on the cart page 
   and i have added "product-1" to my cart 
   when i click the "remove from cart" button for "product-1" 
   then i should see the product removed from my cart 
   and i should see the cart count updated to "0"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the cart page")
def step_given_i_am_on_the_cart_page(context):
    context.cart_page.navigate_to()

@given("i have added 'product-1' to my cart")
def step_given_i_have_added_product_1_to_my_cart(context):
    context.cart_page.add_product_to_cart('product-1')

@when("i click the 'remove from cart' button for 'product-1'")
def step_when_i_click_the_remove_from_cart_button_for_product_1(context):
    context.cart_page.remove_product_from_cart('product-1')

@then("i should see the product removed from my cart")
def step_then_i_should_see_the_product_removed_from_my_cart(context):
    assert context.cart_page.product_in_cart('product-1') == False

@then("i should see the cart count updated to '0'")
def step_then_i_should_see_the_cart_count_updated_to_0(context):
    assert context.cart_page.cart_count() == 0
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the "remove from cart" button given i am on the cart page and i have added "product-1" to my cart when i click the "remove from cart" button for "product-1" then i should see the product removed from my cart and i should see the cart count updated to "0" ```



```python from behave import given, when, then

@given("i am on the cart page")
def step_given_i_am_on_the_cart_page(context):
    context.cart_page.navigate_to()

@given("i have added 'product-1' to my cart")
def step_given_i_have_added_product_1_to_my_cart(context):
    context.cart_page.add_product_to_cart('product-1')

@when("i click the 'remove from cart' button for 'product-1'")
def step_when_i_click_the_remove_from_cart_button_for_product_1(context):
    context.cart_page.remove_product_from_cart('product-1')

@then("i should see the product removed from my cart")
def step_then_i_should_see_the_product_removed_from_my_cart(context):
    assert context.cart_page.product_in_cart('product-1') == False

@then("i should see the cart count updated to '0'")
def step_then_i_should_see_the_cart_count_updated_to_0(context):
    assert context.cart_page.cart_count() == 0
```

Task: Write a program to find the sum of the digits of a given number.
