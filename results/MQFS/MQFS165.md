# MQFS165
## Scenario
```gherkin
scenario: testing the delete functionality 
   given you are on the homepage 
   when you click the delete button 
   then the item is deleted 
   and you are taken back to the homepage
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete functionality given you are on the homepage when you click the delete button then the item is deleted and you are taken back to the homepage ```



from behave import given, when, then

@given("you are on the homepage")
def step_impl(context):
    context.browser.get("http://localhost:8000")

@when("you click the delete button")
def step_impl(context):
    context.browser.find_element_by_id("delete").click()

@then("the item is deleted and you are taken back to the homepage")
def step_impl(context):
    assert "No items here!" in context.browser.page_source
    assert context.browser.current_url == "http://localhost:8000"

Task: Write a program to find the sum of the digits of a given number.
