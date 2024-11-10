# MQFS106
## Scenario
```gherkin
scenario: testing the search functionality 
   given a website with a search bar 
   when the user enters a search term 
   and clicks search 
   then the website displays the search results for the entered term 
   when the user enters an invalid search term 
   then the website displays an error message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the search functionality given a website with a search bar when the user enters a search term and clicks search then the website displays the search results for the entered term when the user enters an invalid search term then the website displays an error message ```



from behave import given, when, then

@given("a website with a search bar")
def step_given_a_website_with_a_search_bar(context):
    context.website = Website()
    context.website.open()

@when("the user enters a search term and clicks search")
def step_when_the_user_enters_a_search_term_and_clicks_search(context):
    context.search_term = "test"
    context.website.search(context.search_term)

@then("the website displays the search results for the entered term")
def step_then_the_website_displays_the_search_results_for_the_entered_term(context):
    assert context.website.search_results == context.search_term

@when("the user enters an invalid search term")
def step_when_the_user_enters_an_invalid_search_term(context):
    context.search_term = "!@#$%^&*"
    context.website.search(context.search_term)

@then("the website displays an error message")
def step_then_the_website_displays_an_error_message(context):
    assert context.website.error_message == "Invalid search term"


class Website:
    def __init__(self):
        self.search_results = None
        self.error_message = None

    def open(self):
        pass

    def search(self, search_term):
        if not search_term.isalnum():
            self.error_message = "Invalid search term"
        else:
            self.search_results = search_term


Task: Write a program to find the sum of the digits of a given number.
