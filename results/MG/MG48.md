# MQFS48
## Scenario
```gherkin
scenario: a user can filter products by price 
   given a user is on the product search page 
   when the user enters a minimum price 
   and a maximum price in the price filter 
   and clicks the search button 
   then the products within the specified price range should be displayed on the search results page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can filter products by price given a user is on the product search page when the user enters a minimum price and a maximum price in the price filter and clicks the search button then the products within the specified price range should be displayed on the search results page ```



from behave import given, when, then

@given("a user is on the product search page")
def step_given(context):
    context.browser.get("https://www.example.com/products")

@when("the user enters a minimum price and a maximum price in the price filter and clicks the search button")
def step_when(context):
    context.browser.find_element_by_id("min-price").send_keys("10")
    context.browser.find_element_by_id("max-price").send_keys("50")
    context.browser.find_element_by_id("search-button").click()

@then("the products within the specified price range should be displayed on the search results page")
def step_then(context):
    products = context.browser.find_elements_by_class_name("product")
    for product in products:
        price = float(product.find_element_by_class_name("price").text.strip("$"))
        assert 10 <= price <= 50

Task: Write a program to find the sum of the digits of a given number.
