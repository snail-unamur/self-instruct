# HQFS82
## Scenario
```gherkin
scenario: i can see the details of a contact in my list of contacts 
   given i am on the contacts page 
   and i have a list of contacts 
   when i click on the 'details' button next to a contact in the list of contacts 
   then i should see the details of the contact
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can see the details of a contact in my list of contacts given i am on the contacts page and i have a list of contacts when i click on the 'details' button next to a contact in the list of contacts then i should see the details of the contact ```



from behave import given, when, then

@given("i am on the contacts page")
def step_impl(context):
    context.driver.get("http://localhost:8000/contacts")

@given("i have a list of contacts")
def step_impl(context):
    context.driver.find_element_by_css_selector("button.add-contact")

@when("i click on the 'details' button next to a contact in the list of contacts")
def step_impl(context):
    context.driver.find_element_by_css_selector("button.details").click()

@then("i should see the details of the contact")
def step_impl(context):
    assert context.driver.find_element_by_css_selector("h1.contact-name")

Task: Write a program to find the sum of the digits of a given number.
