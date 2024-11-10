# MQFS225
## Scenario
```gherkin
scenario: a user wants to search for a specific blog post 
   given the user is on the blog list page 
   when the user enters a keyword into the search bar 
   then the user should be taken to the search results page where they can see a list of blog posts that match the keyword
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user wants to search for a specific blog post given the user is on the blog list page when the user enters a keyword into the search bar then the user should be taken to the search results page where they can see a list of blog posts that match the keyword ```



from behave import given, when, then

@given("the user is on the blog list page")
def step_impl(context):
    context.driver.get("http://www.example.com/blog")

@when("the user enters a keyword into the search bar")
def step_impl(context):
    search_box = context.driver.find_element_by_name("q")
    search_box.send_keys("Keyword")
    search_box.submit()

@then("the user should be taken to the search results page")
def step_impl(context):
    assert context.driver.current_url == "http://www.example.com/search"

@then("where they can see a list of blog posts that match the keyword")
def step_impl(context):
    assert "Keyword" in context.driver.page_source


Task: Write a program to find the sum of the digits of a given number.
