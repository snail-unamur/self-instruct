# MQFS241
## Scenario
```gherkin
scenario: i can edit my account information 
   given i am on the home page 
   when i click on my account 
   then i should be redirected to the account page 
   when i click on edit account 
   then i should be redirected to the edit account page 
   when i enter new account information 
   then i should be redirected to the account page 
   when i check my account information 
   then my new account information should be displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can edit my account information given i am on the home page when i click on my account then i should be redirected to the account page when i click on edit account then i should be redirected to the edit account page when i enter new account information then i should be redirected to the account page when i check my account information then my new account information should be displayed ```



from behave import given, when, then

@given("i am on the home page")
def step(context):
    context.browser.get("http://www.example.com")

@when("i click on my account")
def step(context):
    context.browser.find_element_by_link_text("My Account").click()

@then("i should be redirected to the account page")
def step(context):
    assert context.browser.current_url == "http://www.example.com/account"

@when("i click on edit account")
def step(context):
    context.browser.find_element_by_link_text("Edit Account").click()

@then("i should be redirected to the edit account page")
def step(context):
    assert context.browser.current_url == "http://www.example.com/edit-account"

@when("i enter new account information")
def step(context):
    context.browser.find_element_by_name("name").send_keys("New Name")
    context.browser.find_element_by_name("email").send_keys("newemail@example.com")

@then("i should be redirected to the account page")
def step(context):
    context.browser.find_element_by_link_text("Save").click()
    assert context.browser.current_url == "http://www.example.com/account"

@then("my new account information should be displayed")
def step(context):
    assert context.browser.find_element_by_name("name").get_attribute("value") == "New Name"
    assert context.browser.find_element_by_name("email").get_attribute("value") == "newemail@example.com"

Task: Write a program to find the sum of the digits of a number.
