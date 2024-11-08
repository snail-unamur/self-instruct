# MQFS181
## Scenario
```gherkin
scenario: testing the search functionality 
   given the user is on the homepage 
   when the user enters a search term 
   and clicks the search button 
   then the search results are displayed 
   when the user enters an invalid search term 
   then no results are displayed 
   when the user clicks the search button with an empty search bar 
   then no results are displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the search functionality given the user is on the homepage when the user enters a search term and clicks the search button then the search results are displayed when the user enters an invalid search term then no results are displayed when the user clicks the search button with an empty search bar then no results are displayed ```



```python from behave import given, when, then

@given("the user is on the homepage")
def step_given_the_user_is_on_the_homepage(context):
    context.browser.get("http://www.example.com")

@when("the user enters a search term and clicks the search button")
def step_when_the_user_enters_a_search_term_and_clicks_the_search_button(context):
    search_box = context.browser.find_element_by_name("q")
    search_box.send_keys("test")
    search_box.submit()

@then("the search results are displayed")
def step_then_the_search_results_are_displayed(context):
    assert context.browser.find_element_by_class_name("search-results")

@when("the user enters an invalid search term")
def step_when_the_user_enters_an_invalid_search_term(context):
    search_box = context.browser.find_element_by_name("q")
    search_box.send_keys("asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfas
