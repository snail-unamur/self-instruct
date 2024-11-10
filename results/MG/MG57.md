# MQFS57
## Scenario
```gherkin
scenario: user is able to login 
   given user is on the login page 
   when user enters correct credentials 
   then user is logged in 
   and user is redirected to the home page 
   and user is able to see the welcome message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user is able to login given user is on the login page when user enters correct credentials then user is logged in and user is redirected to the home page and user is able to see the welcome message ```



from behave import given, when, then

@given("user is on the login page")
def step_impl(context):
    context.driver.get("https://www.example.com/login")

@when("user enters correct credentials")
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("testuser")
    context.driver.find_element_by_name("password").send_keys("testpassword")
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("user is logged in and user is redirected to the home page and user is able to see the welcome message")
def step_impl(context):
    assert context.driver.current_url == "https://www.example.com/home"
    assert context.driver.find_element_by_xpath("//h1[contains(text(), 'Welcome')]")

Task: Write a program to find the sum of the digits of a given number.
