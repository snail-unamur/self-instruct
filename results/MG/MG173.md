# MQFS173
## Scenario
```gherkin
scenario: a user can register 
   and login to the website 
   given a user visits the website 
   when the user clicks on the "register" button 
   then the user should see the registration form 
   when the user fills out the registration form with valid information 
   then the user should be registered 
   and logged in 
   when the user clicks on the "logout" button 
   then the user should be logged out
```


## Python Implementation
```python
from behave import given, when, then

@given("a user visits the website")
def step("I open the website home page")

@when("the user clicks on the 'register' button")
 def step_impl(context):
 context.browser.find_element_by_id("register-button").click()

@then("the user should see the registration form")
 def step_impl(context):
 assert context.browser.find_element_by_id("register-form")

@when("the user fills out the registration form with valid information")
 def step_impl(context):
 context.browser.find_element_by_id("username").send_keys("testuser")
 context.browser.find_element_by_id("email").send_keys("testuser@example.com")
 context.browser.find_element_by_id("password").send_keys("testpassword")
 context.browser.find_element_by_id("register-button").click()

@then("the user should be registered and logged in")
 def step_impl(context):
 assert context.browser.find_element_by_id("logout-button")

@when("the user clicks on the 'logout' button")
 def step_impl(context):
 context.browser.find_element_by_id("logout-button").click()

@then("the user should be logged out")
 def step_impl(context):
 assert not context.browser.find_element_by_id("logout-button")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can register and login to the website given a user visits the website when the user clicks on the "register" button then the user should see the registration form when the user fills out the registration form with valid information then the user should be registered and logged in when the user clicks on the "logout" button then the user should be logged out ```



```python from behave import given, when, then

@given("a user visits the website")
def step("I open the website home page")

@when("the user clicks on the 'register' button")
 def step_impl(context):
 context.browser.find_element_by_id("register-button").click()

@then("the user should see the registration form")
 def step_impl(context):
 assert context.browser.find_element_by_id("register-form")

@when("the user fills out the registration form with valid information")
 def step_impl(context):
 context.browser.find_element_by_id("username").send_keys("testuser")
 context.browser.find_element_by_id("email").send_keys("testuser@example.com")
 context.browser.find_element_by_id("password").send_keys("testpassword")
 context.browser.find_element_by_id("register-button").click()

@then("the user should be registered and logged in")
 def step_impl(context):
 assert context.browser.find_element_by_id("logout-button")

@when("the user clicks on the 'logout' button")
 def step_impl(context):
 context.browser.find_element_by_id("logout-button").click()

@then("the user should be logged out")
 def step_impl(context):
 assert not context.browser.find_element_by_id("logout-button")
 ```

Task: Write a program to find the sum of the digits of a given number.
