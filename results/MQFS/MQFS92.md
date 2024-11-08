# MQFS92
## Scenario
```gherkin
scenario: testing the checkout functionality 
   given i am on the cart page 
   when i click on the checkout button 
   then i should be redirected to the checkout page 
   and i should see the total price of the items in my cart 
   given i am on the cart page 
   when i click on the checkout button 
   then i should be redirected to the checkout page 
   and i should see the total price of the items in my cart 
   and i should be able to enter my shipping 
   and billing information 
   and i should be able to select a payment method 
   and i should be able to confirm my order 
   then i should receive a confirmation email 
   and i should be redirected to the order confirmation page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the checkout functionality given i am on the cart page when i click on the checkout button then i should be redirected to the checkout page and i should see the total price of the items in my cart given i am on the cart page when i click on the checkout button then i should be redirected to the checkout page and i should see the total price of the items in my cart and i should be able to enter my shipping and billing information and i should be able to select a payment method and i should be able to confirm my order then i should receive a confirmation email and i should be redirected to the order confirmation page ```



```python from behave import given, when, then

@given("i am on the cart page")
def step_given_i_am_on_the_cart_page(context):
    context.driver.get("http://www.example.com/cart")

@when("i click on the checkout button")
def step_when_i_click_on_the_checkout_button(context):
    checkout_button = context.driver.find_element_by_id("checkout-button")
    checkout_button.click()

@then("i should be redirected to the checkout page")
def step_then_i_should_be_redirected_to_the_checkout_page(context):
    assert context.driver.current_url == "http://www.example.com/checkout"

@then("i should see the total price of the items in my cart")
def step_then_i_should_see_the_total_price_of_the_items_in_my_cart(context):
    total_price = context.driver.find_element_by_id("total-price")
    assert total_price.text != ""

@given("i am on the cart page")
def step_given_i_am_on_the_cart_page_2(context):
    context.driver.get("http://www.example.com/cart")

@when("i click on the checkout button")
def step_when_i_click_on_the_checkout_button_2(context):
    checkout_button = context.driver.find_element_by_id("checkout-button")
    checkout_button.click()

@then("i should be redirected to the checkout page")
def step_then_i_should_be_redirected_to_the_checkout_page_2(context):
    assert context.driver.current_url == "http://www.example.com/checkout"

@then("i should see the total price of the items in my cart")
def step_then_i_should_see_the_total_price_of_the_items_in_
