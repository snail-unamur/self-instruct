# MQFS228
## Scenario
```gherkin
scenario: testing the product page functionality 
   given the user is on the homepage 
   when the user clicks on a product 
   then the product page is displayed 
   when the user clicks the back button 
   then the user is taken back to the homepage 
   when the user adds the product to the cart 
   then the product is added to the cart 
   and the cart count is updated
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the product page functionality given the user is on the homepage when the user clicks on a product then the product page is displayed when the user clicks the back button then the user is taken back to the homepage when the user adds the product to the cart then the product is added to the cart and the cart count is updated ```



from behave import given, when, then

@given("the user is on the homepage")
def step_given_the_user_is_on_the_homepage(context):
    context.homepage = HomePage()
    context.homepage.open()

@when("the user clicks on a product")
def step_when_the_user_clicks_on_a_product(context):
    context.product_page = context.homepage.click_on_product()

@then("the product page is displayed")
def step_then_the_product_page_is_displayed(context):
    assert context.product_page.is_displayed()

@when("the user clicks the back button")
def step_when_the_user_clicks_the_back_button(context):
    context.homepage = context.product_page.click_back_button()

@then("the user is taken back to the homepage")
def step_then_the_user_is_taken_back_to_the_homepage(context):
    assert context.homepage.is_displayed()

@when("the user adds the product to the cart")
def step_when_the_user_adds_the_product_to_the_cart(context):
    context.cart_page = context.product_page.add_product_to_cart()

@then("the product is added to the cart and the cart count is updated")
def step_then_the_product_is_added_to_the_cart_and_the_cart_count_is_updated(context):
    assert context.cart_page.is_displayed()
    assert context.cart_page.get_cart_count() > 0

Task: Write a program to find the sum of the digits of a given number.
