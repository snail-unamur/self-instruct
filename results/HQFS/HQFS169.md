# HQFS169
## Scenario
```gherkin
scenario: a user can add products to their cart 
   given the user is on the product details page 
   when the user clicks the add to cart button 
   then the user should see a message indicating that the product has been added to their cart 
   and the user should be able to view their cart 
   and the user should see the product



from behave import 
   given, 
   when, 
   then

@
   given("the user is on the product details page")
def step_impl(context):
    context.browser.get("https://www.example.com/products/123")

@
   when("the user clicks the add to cart button")
def step_impl(context):
    add_to_cart_button = context.browser.find_element_by_id("add-to-cart-button")
    add_to_cart_button.click()

@
   then("the user should see a message indicating that the product has been added to their cart")
def step_impl(context):
    assert "Product added to cart" in context.browser.page_source

@
   then("the user should be able to view their cart")
def step_impl(context):
    view_cart_button = context.browser.find_element_by_id("view-cart-button")
    view_cart_button.click()

@
   then("the user should see the product")
def step_impl(context):
    assert "Product Name" in context.browser.page_source
    assert "Product Description" in context.browser.page_source
    assert "Product Price" in context.browser.page_source
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add products to their cart given the user is on the product details page when the user clicks the add to cart button then the user should see a message indicating that the product has been added to their cart and the user should be able to view their cart and the user should see the product



from behave import given, when, then

@given("the user is on the product details page")
def step_impl(context):
    context.browser.get("https://www.example.com/products/123")

@when("the user clicks the add to cart button")
def step_impl(context):
    add_to_cart_button = context.browser.find_element_by_id("add-to-cart-button")
    add_to_cart_button.click()

@then("the user should see a message indicating that the product has been added to their cart")
def step_impl(context):
    assert "Product added to cart" in context.browser.page_source

@then("the user should be able to view their cart")
def step_impl(context):
    view_cart_button = context.browser.find_element_by_id("view-cart-button")
    view_cart_button.click()

@then("the user should see the product")
def step_impl(context):
    assert "Product Name" in context.browser.page_source
    assert "Product Description" in context.browser.page_source
    assert "Product Price" in context.browser.page_source

```

Task: Write a program to find the sum of the digits of a given number.
