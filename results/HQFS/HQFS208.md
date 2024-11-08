# HQFS208
## Scenario
```gherkin
scenario: testing the search functionality 
   given the user is on the home page 
   when the user enters a search term 
   then the user should see a list of results 
   and the user should see the number of results 
   and the user should see the relevant results
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the home page")
def step_given_the_user_is_on_the_home_page(context):
    context.driver.get("http://www.example.com")

@when("the user enters a search term")
def step_when_the_user_enters_a_search_term(context):
    search_box = context.driver.find_element_by_name("q")
    search_box.send_keys("behave")
    search_box.submit()

@then("the user should see a list of results")
def step_then_the_user_should_see_a_list_of_results(context):
    assert "results" in context.driver.page_source

@then("the user should see the number of results")
def step_then_the_user_should_see_the_number_of_results(context):
    assert "about" in context.driver.page_source

@then("the user should see the relevant results")
def step_then_the_user_should_see_the_relevant_results(context):
    assert "behave" in context.driver.page_source
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the search functionality given the user is on the home page when the user enters a search term then the user should see a list of results and the user should see the number of results and the user should see the relevant results ```



```python from behave import given, when, then

@given("the user is on the home page")
def step_given_the_user_is_on_the_home_page(context):
    context.driver.get("http://www.example.com")

@when("the user enters a search term")
def step_when_the_user_enters_a_search_term(context):
    search_box = context.driver.find_element_by_name("q")
    search_box.send_keys("behave")
    search_box.submit()

@then("the user should see a list of results")
def step_then_the_user_should_see_a_list_of_results(context):
    assert "results" in context.driver.page_source

@then("the user should see the number of results")
def step_then_the_user_should_see_the_number_of_results(context):
    assert "about" in context.driver.page_source

@then("the user should see the relevant results")
def step_then_the_user_should_see_the_relevant_results(context):
    assert "behave" in context.driver.page_source
```

Task: Write a program to find the sum of the digits of a given number.
