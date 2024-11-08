# MQFS232
## Scenario
```gherkin
scenario: testing the functionality of the wishlist page 
   given i am on the wishlist page 
   when i click the add to wishlist button on a product 
   then i should see the product in my wishlist with the correct quantity 
   and price
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the wishlist page")
def step_given_i_am_on_the_wishlist_page(context):
    context.wishlist_page.navigate_to()

@when("i click the add to wishlist button on a product")
def step_when_i_click_the_add_to_wishlist_button_on_a_product(context):
    context.product_page.add_to_wishlist()

@then("i should see the product in my wishlist with the correct quantity and price")
def step_then_i_should_see_the_product_in_my_wishlist_with_the_correct_quantity_and_price(context):
    context.wishlist_page.verify_product_in_wishlist()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the wishlist page given i am on the wishlist page when i click the add to wishlist button on a product then i should see the product in my wishlist with the correct quantity and price ```



```python from behave import given, when, then

@given("i am on the wishlist page")
def step_given_i_am_on_the_wishlist_page(context):
    context.wishlist_page.navigate_to()

@when("i click the add to wishlist button on a product")
def step_when_i_click_the_add_to_wishlist_button_on_a_product(context):
    context.product_page.add_to_wishlist()

@then("i should see the product in my wishlist with the correct quantity and price")
def step_then_i_should_see_the_product_in_my_wishlist_with_the_correct_quantity_and_price(context):
    context.wishlist_page.verify_product_in_wishlist()
```

Task: Write a program to find the sum of the digits of a given number.
