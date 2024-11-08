# MQFS138
## Scenario
```gherkin
scenario: testing the functionality of the search page 
   given i am on the search page 
   when i enter a search term 
   then i should see a list of products that match the search term 
   given i am on the search page 
   when i filter the search results by category 
   then i should see a list of products that match the filtered category 
   given i am on the search page 
   when i sort the search results by price 
   then i should see
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the functionality of the search page given i am on the search page when i enter a search term then i should see a list of products that match the search term given i am on the search page when i filter the search results by category then i should see a list of products that match the filtered category given i am on the search page when i sort the search results by price then i should see

```

from behave import given, when, then

@given("i am on the search page")
def step_given_i_am_on_the_search_page(context):
    context.search_page.navigate()

@when("i enter a search term")
def step_when_i_enter_a_search_term(context):
    context.search_term = "product"
    context.search_page.search(context.search_term)

@then("i should see a list of products that match the search term")
def step_then_i_should_see_a_list_of_products_that_match_the_search_term(context):
    assert context.search_page.get_products() == [
        "product1", "product2", "product3"
    ]

@when("i filter the search results by category")
def step_when_i_filter_the_search_results_by_category(context):
    context.search_page.filter_by_category("category1")

@then("i should see a list of products that match the filtered category")
def step_then_i_should_see_a_list_of_products_that_match_the_filtered_category(context):
    assert context.search_page.get_products() == [
        "product1", "product4", "product5"
    ]

@when("i sort the search results by price")
def step_when_i_sort_the_search_results_by_price(context):
    context.search_page.sort_by_price("asc")

@then("i should see a list of products that match the sorted price")
def step_then_i_should_see_a_list_of_products_that_match_the_sorted_price(context):
    assert context.search_page.get_products() == [
        "product6", "product7", "product8"
    ]


Task: Write a program to find the second largest number in a list.
