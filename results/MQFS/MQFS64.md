# MQFS64
## Scenario
```gherkin
scenario: 
   given i am on my new list page 
   when i add an item to my list 
   and click the "save" button 
   then i should be taken back to my list page 
   and see my new item listed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i am on my new list page when i add an item to my list and click the "save" button then i should be taken back to my list page and see my new item listed ```



from behave import given, when, then

@given("i am on my new list page")
def step_given_i_am_on_my_new_list_page(context):
    context.driver.get("http://localhost:8000/lists/new")

@when("i add an item to my list and click the 'save' button")
def step_when_i_add_an_item_to_my_list_and_click_the_save_button(context):
    context.list_page.add_item("item 1")
    context.list_page.click_save()

@then("i should be taken back to my list page and see my new item listed")
def step_then_i_should_be_taken_back_to_my_list_page_and_see_my_new_item_listed(context):
    assert context.list_page.is_displayed()
    assert context.list_page.get_item_text(0) == "item 1"

class ListPage(object):
    def __init__(self, context):
        self.context = context

    def add_item(self, item):
        inputbox = self.context.driver.find_element_by_id("id_new_item")
        inputbox.send_keys(item)

    def click_save(self):
        button = self.context.driver.find_element_by_id("save_button")
        button.click()

    def is_displayed(self):
        return self.context.driver.find_element_by_id("list_page")

    def get_item_text(self, index):
        item_text = self.context.driver.find_elements_by_class_name("item")[index].text
        return item_text
