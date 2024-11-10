# HQFS8
## Scenario
```gherkin
scenario: user is able to remove a product from the cart 
   given user is on the cart page 
   when user clicks on the remove button 
   then user is able to see the product removed from the cart
```


## Python Implementation
```python
from behave import given, when, then

@given("user is on the cart page")
def step_given_user_is_on_cart_page(context):
    context.cart_page.navigate_to_cart_page()

@when("user clicks on the remove button")
def step_when_user_clicks_on_remove_button(context):
    context.cart_page.click_remove_button()

@then("user is able to see the product removed from the cart")
def step_then_user_is_able_to_see_product_removed_from_cart(context):
    context.cart_page.verify_product_is_removed()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user is able to remove a product from the cart given user is on the cart page when user clicks on the remove button then user is able to see the product removed from the cart ```



```python from behave import given, when, then

@given("user is on the cart page")
def step_given_user_is_on_cart_page(context):
    context.cart_page.navigate_to_cart_page()

@when("user clicks on the remove button")
def step_when_user_clicks_on_remove_button(context):
    context.cart_page.click_remove_button()

@then("user is able to see the product removed from the cart")
def step_then_user_is_able_to_see_product_removed_from_cart(context):
    context.cart_page.verify_product_is_removed()
```

Task: Write a program to find the sum of the digits of a given number.
