# MQFS128
## Scenario
```gherkin
scenario: adding a new product to the cart 
   given website "http://qa_dashboard.test.thinkmobiles.com:8085" 
   when user clicks on the product 
   then user is redirected to the product page 
   when user clicks on the "add to cart" button 
   then user is redirected to the cart page 
   and the product is added to the cart
```


## Python Implementation
```python
from behave import given, when, then

@given("website '{url}' is opened")
def step_impl(context, url):
    context.driver.get(url)

@when("user clicks on the product")
def step_impl(context):
    context.product = context.driver.find_element_by_xpath("//div[@class='product-card']")
    context.product.click()

@then("user is redirected to the product page")
def step_impl(context):
    assert context.driver.current_url == "http://qa_dashboard.test.thinkmobiles.com:8085/product/1"

@when("user clicks on the 'add to cart' button")
def step_impl(context):
    context.add_to_cart_button = context.driver.find_element_by_xpath("//button[@class='btn btn-primary']")
    context.add_to_cart_button.click()

@then("user is redirected to the cart page and the product is added to the cart")
def step_impl(context):
    assert context.driver.current_url == "http://qa_dashboard.test.thinkmobiles.com:8085/cart"
    assert context.driver.find_element_by_xpath("//td[contains(text(), 'Product 1')]")
    assert context.driver.find_element_by_xpath("//td[contains(text(), '1')]")
    assert context.driver.find_element_by_xpath("//td[contains(text(), '$100')]")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: adding a new product to the cart given website "http://qa_dashboard.test.thinkmobiles.com:8085" when user clicks on the product then user is redirected to the product page when user clicks on the "add to cart" button then user is redirected to the cart page and the product is added to the cart ```



```python from behave import given, when, then

@given("website '{url}' is opened")
def step_impl(context, url):
    context.driver.get(url)

@when("user clicks on the product")
def step_impl(context):
    context.product = context.driver.find_element_by_xpath("//div[@class='product-card']")
    context.product.click()

@then("user is redirected to the product page")
def step_impl(context):
    assert context.driver.current_url == "http://qa_dashboard.test.thinkmobiles.com:8085/product/1"

@when("user clicks on the 'add to cart' button")
def step_impl(context):
    context.add_to_cart_button = context.driver.find_element_by_xpath("//button[@class='btn btn-primary']")
    context.add_to_cart_button.click()

@then("user is redirected to the cart page and the product is added to the cart")
def step_impl(context):
    assert context.driver.current_url == "http://qa_dashboard.test.thinkmobiles.com:8085/cart"
    assert context.driver.find_element_by_xpath("//td[contains(text(), 'Product 1')]")
    assert context.driver.find_element_by_xpath("//td[contains(text(), '1')]")
    assert context.driver.find_element_by_xpath("//td[contains(text(), '$100')]")
```

Task: Write a program to find the sum of the digits of a given number.
