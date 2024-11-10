# MQFS233
## Scenario
```gherkin
scenario: testing the search functionality 
   given the user is on the search page 
   when the user enters a search term 
   then the search results should be displayed 
   when the user clicks on a search result 
   then the user should be taken to the corresponding page 
   when the user enters an invalid search term 
   then an error message should be displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the search functionality given the user is on the search page when the user enters a search term then the search results should be displayed when the user clicks on a search result then the user should be taken to the corresponding page when the user enters an invalid search term then an error message should be displayed ```



from behave import given, when, then

@given("the user is on the search page")
def step_given_the_user_is_on_the_search_page(context):
    context.driver.get("https://www.example.com/search")

@when("the user enters a search term")
def step_when_the_user_enters_a_search_term(context):
    search_box = context.driver.find_element_by_name("q")
    search_box.send_keys("test")
    search_box.submit()

@then("the search results should be displayed")
def step_then_the_search_results_should_be_displayed(context):
    assert context.driver.find_element_by_class_name("search-results")

@when("the user clicks on a search result")
def step_when_the_user_clicks_on_a_search_result(context):
    search_result = context.driver.find_element_by_xpath("//a[@href='/test']")
    search_result.click()

@then("the user should be taken to the corresponding page")
def step_then_the_user_should_be_taken_to_the_corresponding_page(context):
    assert context.driver.current_url == "https://www.example.com/test"

@when("the user enters an invalid search term")
def step_when_the_user_enters_an_invalid_search_term(context):
    search_box = context.driver.find_element_by_name("q")
    search_box.send_keys("invalid")
    search_box.submit()

@then("an error message should be displayed")
def step_then_an_error_message_should_be_displayed(context):
    assert context.driver.find_element_by_class_name("error-message")
