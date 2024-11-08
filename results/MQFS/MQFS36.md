# MQFS36
## Scenario
```gherkin
scenario: user registration 
   given website "http://qa_dashboard.test.thinkmobiles.com:8085" 
   when user click on register button 
   then appears registration form 
   when user fill in the form with valid data 
   then user should be registered successfully
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user registration given website "http://qa_dashboard.test.thinkmobiles.com:8085" when user click on register button then appears registration form when user fill in the form with valid data then user should be registered successfully ```



from behave import given, when, then
import time

@given("website {url}")
def step_given_website(context, url):
    context.browser.get(url)

@when("user click on register button")
def step_when_click_register(context):
    context.browser.find_element_by_xpath("//a[@href='/register']").click()

@when("user fill in the form with valid data")
def step_when_fill_form(context):
    context.browser.find_element_by_xpath("//input[@name='first_name']").send_keys("John")
    context.browser.find_element_by_xpath("//input[@name='last_name']").send_keys("Doe")
    context.browser.find_element_by_xpath("//input[@name='email']").send_keys("john.doe@test.com")
    context.browser.find_element_by_xpath("//input[@name='password']").send_keys("123456")
    context.browser.find_element_by_xpath("//input[@name='confirm_password']").send_keys("123456")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("user should be registered successfully")
def step_then_registered_successfully(context):
    time.sleep(5)
    assert context.browser.find_element_by_xpath("//div[@class='alert alert-success']")

Task: Write a program to find the sum of the digits of a given number.
