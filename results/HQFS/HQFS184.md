# HQFS184
## Scenario
```gherkin
scenario: a user can search for a product 
   given i am on the homepage 
   when i enter a product name in the search bar 
   then i should be shown a list of products that match the search criteria 
   when i click on a product 
   then i should be taken to the product page where i can view more details about the product
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.browser.visit("http://www.example.com")

@when("i enter a product name in the search bar")
def step_impl(context):
    search_bar = context.browser.find_by_name("q")
    search_bar.fill("product name")
    search_bar.first.click()

@then("i should be shown a list of products that match the search criteria")
def step_impl(context):
    assert context.browser.is_text_present("product name")

@when("i click on a product")
def step_impl(context):
    product = context.browser.find_by_link_text("product name")
    product.first.click()

@then("i should be taken to the product page where i can view more details about the product")
def step_impl(context):
    assert context.browser.url.endswith("/product-name")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can search for a product given i am on the homepage when i enter a product name in the search bar then i should be shown a list of products that match the search criteria when i click on a product then i should be taken to the product page where i can view more details about the product ```



```python from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.browser.visit("http://www.example.com")

@when("i enter a product name in the search bar")
def step_impl(context):
    search_bar = context.browser.find_by_name("q")
    search_bar.fill("product name")
    search_bar.first.click()

@then("i should be shown a list of products that match the search criteria")
def step_impl(context):
    assert context.browser.is_text_present("product name")

@when("i click on a product")
def step_impl(context):
    product = context.browser.find_by_link_text("product name")
    product.first.click()

@then("i should be taken to the product page where i can view more details about the product")
def step_impl(context):
    assert context.browser.url.endswith("/product-name")
```

Task: Write a program to find the sum of the digits of a given number.
