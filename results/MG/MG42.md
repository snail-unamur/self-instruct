# MQFS42
## Scenario
```gherkin
scenario: testing the create organization functionality 
   given i am logged in 
   when i click on the create organization button 
   then i should be redirected to the create organization page 
   when i enter a valid organization name 
   and i click on the create button 
   then i should be redirected to the organization page 
   and i should see the new organization in the list of organizations
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the create organization functionality given i am logged in when i click on the create organization button then i should be redirected to the create organization page when i enter a valid organization name and i click on the create button then i should be redirected to the organization page and i should see the new organization in the list of organizations ```



from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i click on the create organization button")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[@href='/organizations/create']").click()

@then("i should be redirected to the create organization page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/organizations/create"

@when("i enter a valid organization name")
def step_impl(context):
    context.browser.find_element_by_name("name").send_keys("Test Org")

@when("i click on the create button")
def step_impl(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be redirected to the organization page")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/organizations/1"

@then("i should see the new organization in the list of organizations")
def step_impl(context):
    assert context.browser.find_element_by_xpath("//td[contains(text(), 'Test Org')]")

Task: Write a program to find the sum of the digits of a given number.
