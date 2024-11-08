# HQFS80
## Scenario
```gherkin
scenario: user searches for a product 
   given i am on the product page 
   when i enter a search term in the search bar 
   then the products matching the search term are displayed
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the product page")
def step_given_i_am_on_the_product_page(context):
    context.browser.get("https://www.example.com/products")

@when("i enter a search term in the search bar")
def step_when_i_enter_a_search_term_in_the_search_bar(context):
    search_bar = context.browser.find_element_by_name("search")
    search_bar.send_keys("product")
    search_bar.submit()

@then("the products matching the search term are displayed")
def step_then_the_products_matching_the_search_term_are_displayed(context):
    products = context.browser.find_elements_by_class_name("product")
    assert len(products) > 0
    for product in products:
        assert "product" in product.text.lower()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user searches for a product given i am on the product page when i enter a search term in the search bar then the products matching the search term are displayed ```



```python from behave import given, when, then

@given("i am on the product page")
def step_given_i_am_on_the_product_page(context):
    context.browser.get("https://www.example.com/products")

@when("i enter a search term in the search bar")
def step_when_i_enter_a_search_term_in_the_search_bar(context):
    search_bar = context.browser.find_element_by_name("search")
    search_bar.send_keys("product")
    search_bar.submit()

@then("the products matching the search term are displayed")
def step_then_the_products_matching_the_search_term_are_displayed(context):
    products = context.browser.find_elements_by_class_name("product")
    assert len(products) > 0
    for product in products:
        assert "product" in product.text.lower()
```

Task: Write a program to find the sum of the digits of a given number.
