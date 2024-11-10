# HQFS237
## Scenario
```gherkin
scenario: user is able to login to their account 
   given i am on the homepage 
   when i click on the login button 
   then i am taken to the login page 
   and i fill in the form with valid information 
   and i submit the form 
   then i am taken to the account dashboard page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user is able to login to their account given i am on the homepage when i click on the login button then i am taken to the login page and i fill in the form with valid information and i submit the form then i am taken to the account dashboard page ```



from behave import given, when, then

@given("i am on the homepage")
def step_impl(context):
    context.driver.get("http://www.example.com")

@when("i click on the login button")
def step_impl(context):
    context.driver.find_element_by_id("login_button").click()

@then("i am taken to the login page")
def step_impl(context):
    assert context.driver.current_url == "http://www.example.com/login"

@when("i fill in the form with valid information")
def step_impl(context):
    context.driver.find_element_by_id("username").send_keys("testuser")
    context.driver.find_element_by_id("password").send_keys("testpassword")

@when("i submit the form")
def step_impl(context):
    context.driver.find_element_by_id("login_form").submit()

@then("i am taken to the account dashboard page")
def step_impl(context):
    assert context.driver.current_url == "http://www.example.com/account"
