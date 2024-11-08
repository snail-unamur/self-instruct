# MQFS23
## Scenario
```gherkin
scenario: testing the functionality of the "search" button 
   given i am on the homepage 
   and i have entered "product-1" in the search bar 
   when i click the "search" button 
   then i should see the search results page for "product-1"
```


## Python Implementation
```python
from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.driver.get("http://www.example.com")

@given("i have entered 'product-1' in the search bar")
def step_given_i_have_entered_product_1_in_the_search_bar(context):
    search_bar = context.driver.find_element_by_name("search")
    search_bar.send_keys("product-1")

@when("i click the 'search' button")
def step_when_i_click_the_search_button(context):
    search_button = context.driver.find_element_by_name("search_button")
    search_button.click()

@then("i should see the search results page for 'product-1'")
def step_then_i_should_see_the_search_results_page_for_product_1(context):
    assert "search_results" in context.driver.current_url
    assert "product-1" in context.driver.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the "search" button given i am on the homepage and i have entered "product-1" in the search bar when i click the "search" button then i should see the search results page for "product-1" ```



```python from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.driver.get("http://www.example.com")

@given("i have entered 'product-1' in the search bar")
def step_given_i_have_entered_product_1_in_the_search_bar(context):
    search_bar = context.driver.find_element_by_name("search")
    search_bar.send_keys("product-1")

@when("i click the 'search' button")
def step_when_i_click_the_search_button(context):
    search_button = context.driver.find_element_by_name("search_button")
    search_button.click()

@then("i should see the search results page for 'product-1'")
def step_then_i_should_see_the_search_results_page_for_product_1(context):
    assert "search_results" in context.driver.current_url
    assert "product-1" in context.driver.page_source
```

Task: Write a program to find the sum of the digits of a given number.
