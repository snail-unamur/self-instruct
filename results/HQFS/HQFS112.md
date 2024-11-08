# HQFS112
## Scenario
```gherkin
scenario: user registers 
   given user is on the registration page 
   when user fills out the registration form 
   then user is registered
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user registers given user is on the registration page when user fills out the registration form then user is registered ```



from behave import given, when, then

@given("user is on the registration page")
def step(context):
    context.browser.get("https://example.com/register")

@when("user fills out the registration form")
def step(context):
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("email").send_keys("testuser@example.com")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_name("submit").click()

@then("user is registered")
def step(context):
    assert context.browser.find_element_by_id("registered")

Task: Write a program to find the sum of the digits of a given number.
