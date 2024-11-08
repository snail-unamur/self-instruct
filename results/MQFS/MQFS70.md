# MQFS70
## Scenario
```gherkin
scenario: testing the shopping cart feature 
   given you are on the product details page 
   when you click the add to cart button 
   then the product should be added to your shopping cart 
   and you should see a notification confirming the addition 
   when you click the view cart button 
   then you should be redirected to the shopping cart page 
   and you should see the product in your shopping cart 
   when you click the remove button next to the product 
   then the product should be removed from your shopping cart 
   and you should see a notification confirming the removal 
   when you click the checkout button 
   then you should be redirected to the checkout page 
   and you should see the contents of your shopping cart 
   and you should be able to enter your shipping 
   and billing information 
   and complete the purchase
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the shopping cart feature given you are on the product details page when you click the add to cart button then the product should be added to your shopping cart and you should see a notification confirming the addition when you click the view cart button then you should be redirected to the shopping cart page and you should see the product in your shopping cart when you click the remove button next to the product then the product should be removed from your shopping cart and you should see a notification confirming the removal when you click the checkout button then you should be redirected to the checkout page and you should see the contents of your shopping cart and you should be able to enter your shipping and billing information and complete the purchase ```



from behave import given, when, then

@given("you are on the product details page")
def step_given_you_are_on_the_product_details_page(context):
    context.browser.get("http://www.example.com/products/123")

@when("you click the add to cart button")
def step_when_you_click_the_add_to_cart_button(context):
    add_to_cart_button = context.browser.find_element_by_id("add-to-cart")
    add_to_cart_button.click()

@then("the product should be added to your shopping cart")
def step_then_the_product_should_be_added_to_your_shopping_cart(context):
    assert "Product added" in context.browser.find_element_by_css_selector(".notification").text

@then("you should see a notification confirming the addition")
def step_then_you_should_see_a_notification_confirming_the_addition(context):
    pass

@when("you click the view cart button")
def step_when_you_click_the_view_cart_button(context):
    view_cart_button = context.browser.find_element_by_id("view-cart")
    view_cart_button.click()

@then("you should be redirected to the shopping cart page")
def step_then_you_should_be_redirected_to_the_shopping_cart_page(context):
    assert context.browser.current_url == "http://www.example.com/cart"

@then("you should see the product in your shopping cart")
def step_then_you_should_see_the_product_in_your_shopping_cart(context):
    assert context.browser.find_element_by_css_selector(".product-name").text == "Product Name"

@when("you click the remove button next to the product")
def step_when_you_click_the_remove_button_next_to_the_product(context):
    remove_button = context.browser.find_element_by
