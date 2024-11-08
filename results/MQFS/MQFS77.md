# MQFS77
## Scenario
```gherkin
scenario: testing the search functionality 
   given i am on the homepage 
   when i search for a product 
   then i should see a list of products that match my search criteria 
   when i click on a product 
   then i should be taken to the product page 
   when i search for a product that does not exist 
   then i should see a message saying that the product was not found
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.driver.get("http://www.example.com")

@when("i search for a product")
def step_impl(context):
    context.search_box = context.driver.find_element_by_name("q")
    context.search_box.send_keys("product")
    context.search_box.submit()

@then("i should see a list of products that match my search criteria")
def step_impl(context):
    products = context.driver.find_elements_by_class_name("product")
    assert len(products) > 0

@when("i click on a product")
def step_impl(context):
    context.product = context.driver.find_element_by_link_text("product")
    context.product.click()

@then("i should be taken to the product page")
def step_impl(context):
    assert context.driver.current_url == "http://www.example.com/product"

@when("i search for a product that does not exist")
def step_impl(context):
    context.search_box = context.driver.find_element_by_name("q")
    context.search_box.send_keys("non-existent-product")
    context.search_box.submit()

@then("i should see a message saying that the product was not found")
def step_impl(context):
    assert context.driver.find_element_by_class_name("error").text == "Product not found"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the search functionality given i am on the homepage when i search for a product then i should see a list of products that match my search criteria when i click on a product then i should be taken to the product page when i search for a product that does not exist then i should see a message saying that the product was not found ```



```python from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.driver.get("http://www.example.com")

@when("i search for a product")
def step_impl(context):
    context.search_box = context.driver.find_element_by_name("q")
    context.search_box.send_keys("product")
    context.search_box.submit()

@then("i should see a list of products that match my search criteria")
def step_impl(context):
    products = context.driver.find_elements_by_class_name("product")
    assert len(products) > 0

@when("i click on a product")
def step_impl(context):
    context.product = context.driver.find_element_by_link_text("product")
    context.product.click()

@then("i should be taken to the product page")
def step_impl(context):
    assert context.driver.current_url == "http://www.example.com/product"

@when("i search for a product that does not exist")
def step_impl(context):
    context.search_box = context.driver.find_element_by_name("q")
    context.search_box.send_keys("non-existent-product")
    context.search_box.submit()

@then("i should see a message saying that the product was not found")
def step_impl(context):
    assert context.driver.find_element_by_class_name("error").text == "Product not found"
```

Task: Write a program to find the sum of the digits of a given number.
