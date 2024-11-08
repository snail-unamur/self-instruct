# MQFS248
## Scenario
```gherkin
scenario: testing the add to cart functionality 
   given the user is on the details page for a product 
   when the user clicks the add to cart button 
   then the product should be added to the shopping cart 
   when the user has added multiple products to the shopping cart 
   then the user should be able to view the shopping cart 
   and see all of the added products
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the add to cart functionality given the user is on the details page for a product when the user clicks the add to cart button then the product should be added to the shopping cart when the user has added multiple products to the shopping cart then the user should be able to view the shopping cart and see all of the added products ```



from behave import given, when, then

@given("the user is on the details page for a product")
def step_given(context):
    context.browser.get("https://www.example.com/products/1")

@when("the user clicks the add to cart button")
def step_when(context):
    context.browser.find_element_by_id("add-to-cart-button").click()

@then("the product should be added to the shopping cart")
def step_then(context):
    assert "Product 1" in context.browser.find_element_by_id("shopping-cart").text

@given("the user has added multiple products to the shopping cart")
def step_given_multiple_products(context):
    context.browser.get("https://www.example.com/products/1")
    context.browser.find_element_by_id("add-to-cart-button").click()
    context.browser.get("https://www.example.com/products/2")
    context.browser.find_element_by_id("add-to-cart-button").click()

@then("the user should be able to view the shopping cart and see all of the added products")
def step_then_view_shopping_cart(context):
    context.browser.get("https://www.example.com/shopping-cart")
    assert "Product 1" in context.browser.find_element_by_id("shopping-cart").text
    assert "Product 2" in context.browser.find_element_by_id("shopping-cart").text
