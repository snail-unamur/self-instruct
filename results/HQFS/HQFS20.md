# HQFS20
## Scenario
```gherkin
scenario: a user can edit their account details 
   given i am logged in 
   when i click on the edit account button 
   then i should be redirected to the edit account page 
   and i should see the current account details 
   and i can update the account details 
   and i can save the updated account details 
   then i should be redirected to the homepage 
   and i should see the updated account details
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit their account details given i am logged in when i click on the edit account button then i should be redirected to the edit account page and i should see the current account details and i can update the account details and i can save the updated account details then i should be redirected to the homepage and i should see the updated account details ```



```python from behave import given, when, then

@given("i am logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i click on the edit account button")
def step_impl(context):
    context.browser.get("http://localhost:8000/account")
    context.browser.find_element_by_xpath("//a[@href='/account/edit']").click()

@then("i should be redirected to the edit account page and i should see the current account details")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/account/edit"
    assert context.browser.find_element_by_name("first_name").get_attribute("value") == "Test"
    assert context.browser.find_element_by_name("last_name").get_attribute("value") == "User"
    assert context.browser.find_element_by_name("email").get_attribute("value") == "testuser@example.com"

@when("i update the account details")
def step_impl(context):
    context.browser.find_element_by_name("first_name").clear()
    context.browser.find_element_by_name("first_name").send_keys("New")
    context.browser.find_element_by_name("last_name").clear()
    context.browser.find_element_by_name("last_name").send_keys("Name")
    context.browser.find_element_by_name("email").clear()
    context.browser.find_element_by_name("email").send_keys("newname@example.com")

@when("i save the updated account details")
def step_impl(context):
    context.
