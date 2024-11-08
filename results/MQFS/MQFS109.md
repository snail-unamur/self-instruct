# MQFS109
## Scenario
```gherkin
scenario: a user wants to search for a book in the library 
   given the user is on the library page 
   when the user enters a search term in the search bar 
   and the user clicks on the "search" button 
   then only the books that match the search term should be displayed in the library 
   and the user should be taken back to the library page
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the library page")
def step_given_the_user_is_on_the_library_page(context):
    context.driver.get("http://library.com")

@when("the user enters a search term in the search bar")
def step_when_the_user_enters_a_search_term_in_the_search_bar(context):
    search_bar = context.driver.find_element_by_name("search")
    search_bar.send_keys("book title")

@when("the user clicks on the 'search' button")
def step_when_the_user_clicks_on_the_search_button(context):
    search_button = context.driver.find_element_by_name("search_button")
    search_button.click()

@then("only the books that match the search term should be displayed in the library")
def step_then_only_the_books_that_match_the_search_term_should_be_displayed_in_the_library(context):
    books = context.driver.find_elements_by_class_name("book")
    for book in books:
        assert "book title" in book.text

@then("the user should be taken back to the library page")
def step_then_the_user_should_be_taken_back_to_the_library_page(context):
    assert context.driver.current_url == "http://library.com"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user wants to search for a book in the library given the user is on the library page when the user enters a search term in the search bar and the user clicks on the "search" button then only the books that match the search term should be displayed in the library and the user should be taken back to the library page ```



```python from behave import given, when, then

@given("the user is on the library page")
def step_given_the_user_is_on_the_library_page(context):
    context.driver.get("http://library.com")

@when("the user enters a search term in the search bar")
def step_when_the_user_enters_a_search_term_in_the_search_bar(context):
    search_bar = context.driver.find_element_by_name("search")
    search_bar.send_keys("book title")

@when("the user clicks on the 'search' button")
def step_when_the_user_clicks_on_the_search_button(context):
    search_button = context.driver.find_element_by_name("search_button")
    search_button.click()

@then("only the books that match the search term should be displayed in the library")
def step_then_only_the_books_that_match_the_search_term_should_be_displayed_in_the_library(context):
    books = context.driver.find_elements_by_class_name("book")
    for book in books:
        assert "book title" in book.text

@then("the user should be taken back to the library page")
def step_then_the_user_should_be_taken_back_to_the_library_page(context):
    assert context.driver.current_url == "http://library.com"
```

Task: Write a program to find the sum of the digits of a given number.
