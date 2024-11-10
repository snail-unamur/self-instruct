# HQFS19
## Scenario
```gherkin
scenario: add product to cart 
   given i am on the blouse product page 
   when i click add to cart 
   then the product should be added to the cart 
   and i should be redirected to the cart page 
   and i should see the product in the cart 
   and i should see the product price in the cart 
   and i should see the total price in the cart 
   and i should see the option to update the cart
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add product to cart given i am on the blouse product page when i click add to cart then the product should be added to the cart and i should be redirected to the cart page and i should see the product in the cart and i should see the product price in the cart and i should see the total price in the cart and i should see the option to update the cart ```



from behave import given, when, then

@given("i am on the blouse product page")
def step_given_i_am_on_the_blouse_product_page(context):
    context.driver.get("http://blouse-page.com")

@when("i click add to cart")
def step_when_i_click_add_to_cart(context):
    context.element = context.driver.find_element_by_id("add-to-cart-button")
    context.element.click()

@then("the product should be added to the cart")
def step_then_the_product_should_be_added_to_the_cart(context):
    assert "product-name" in context.driver.page_source

@then("i should be redirected to the cart page")
def step_then_i_should_be_redirected_to_the_cart_page(context):
    assert context.driver.current_url == "http://cart-page.com"

@then("i should see the product in the cart")
def step_then_i_should_see_the_product_in_the_cart(context):
    assert "product-name" in context.driver.page_source

@then("i should see the product price in the cart")
def step_then_i_should_see_the_product_price_in_the_cart(context):
    price = context.driver.find_element_by_id("product-price")
    assert price.text == "$100.00"

@then("i should see the total price in the cart")
def step_then_i_should_see_the_total_price_in_the_cart(context):
    total = context.driver.find_element_by_id("total-price")
    assert total.text == "$100.00"

@then("i should see the option to update the cart")
def step_then_i_should_see_the_option_to_update_the_cart(context):
    assert context.driver.find_element_by_id("update-cart-button")
