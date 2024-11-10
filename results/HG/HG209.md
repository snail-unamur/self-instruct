# HQFS209
## Scenario
```gherkin
scenario: user can filter tasks on the board 
   given the user is on the board page 
   when the user enters a filter string in the filter text box 
   then only tasks matching the filter string should be displayed on the board
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can filter tasks on the board given the user is on the board page when the user enters a filter string in the filter text box then only tasks matching the filter string should be displayed on the board ```



from behave import given, when, then

@given("the user is on the board page")
def step(context):
    context.board_page.open()

@when("the user enters a filter string in the filter text box")
def step(context):
    context.board_page.enter_filter_string("filter_string")

@then("only tasks matching the filter string should be displayed on the board")
def step(context):
    assert context.board_page.get_displayed_tasks() == ["task_matching_filter_string"]

Task: Write a program to find the sum of the digits of a given number.
