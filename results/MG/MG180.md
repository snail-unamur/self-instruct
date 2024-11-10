# MQFS180
## Scenario
```gherkin
scenario: testing the add functionality 
   given i am on the homepage 
   when i enter a new item into the text box 
   and i click the add button 
   then the new item is displayed on the page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the add functionality given i am on the homepage when i enter a new item into the text box and i click the add button then the new item is displayed on the page ```



from behave import given, when, then

@given("i am on the homepage")
def step_given_i_am_on_the_homepage(context):
    context.browser.get("http://localhost:8000")

@when("i enter a new item into the text box")
def step_when_i_enter_a_new_item_into_the_text_box(context):
    context.text_box = context.browser.find_element_by_name("item")
    context.text_box.send_keys("A new item")

@when("i click the add button")
def step_when_i_click_the_add_button(context):
    context.add_button = context.browser.find_element_by_name("add")
    context.add_button.click()

@then("the new item is displayed on the page")
def step_then_the_new_item_is_displayed_on_the_page(context):
    context.new_item = context.browser.find_element_by_xpath("//li[contains(text(), 'A new item')]")
    assert context.new_item.is_displayed()

Task: Write a program to find the sum of the digits of a given number.
