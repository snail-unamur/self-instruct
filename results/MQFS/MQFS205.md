# MQFS205
## Scenario
```gherkin
scenario: testing the login functionality 
   given the user is on the login page 
   when the user enters a valid username 
   and password 
   then the user should be taken to the dashboard page 
   when the user enters an invalid username 
   and password 
   then an error message should be displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given the user is on the login page when the user enters a valid username and password then the user should be taken to the dashboard page when the user enters an invalid username and password then an error message should be displayed ``` to implement the step functions for the given gherkin scenarios, you can use the behave bdd testing framework in python. here are the step functions for each scenario:



from behave import given, when, then

@given("the user is on the login page")
def step_given_the_user_is_on_the_login_page(context):
    context.driver.get("https://example.com/login")

@when("the user enters a valid username and password")
def step_when_the_user_enters_a_valid_username_and_password(context):
    context.username = "testuser"
    context.password = "testpassword"
    context.driver.find_element_by_name("username").send_keys(context.username)
    context.driver.find_element_by_name("password").send_keys(context.password)
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("the user should be taken to the dashboard page")
def step_then_the_user_should_be_taken_to_the_dashboard_page(context):
    assert context.driver.current_url == "https://example.com/dashboard"

@when("the user enters an invalid username and password")
def step_when_the_user_enters_an_invalid_username_and_password(context):
    context.username = "invaliduser"
    context.password = "invalidpassword"
    context.driver.find_element_by_name("username").send_keys(context.username)
    context.driver.find_element_by_name("password").send_keys(context.password)
    context.driver.find_element_by_xpath("//button[@type='submit']").click()

@then("an error message should be displayed")
def step_then_an_error_message_should_be_displayed(context):
    error_message = context.driver.find_element_by_xpath("//div[@class='error']").text
    assert "Invalid username or password" in error_message
