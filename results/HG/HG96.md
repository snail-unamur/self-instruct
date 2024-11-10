# HQFS96
## Scenario
```gherkin
scenario: testing the login functionality 
   given i am on the login page 
   when i enter my email address 
   and password 
   and click the "log in" button 
   then i should be redirected to the home page 
   and i should see a welcome message with my name
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the login functionality given i am on the login page when i enter my email address and password and click the "log in" button then i should be redirected to the home page and i should see a welcome message with my name ```



from behave import given, when, then

@given("i am on the login page")
def step_given_i_am_on_the_login_page(context):
    context.browser.get("https://www.example.com/login")

@when("i enter my email address and password and click the \"log in\" button")
def step_when_i_enter_my_email_address_and_password_and_click_the_log_in_button(context):
    email_field = context.browser.find_element_by_name("email")
    email_field.send_keys("test@example.com")

    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("test123")

    login_button = context.browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

@then("i should be redirected to the home page")
def step_then_i_should_be_redirected_to_the_home_page(context):
    assert context.browser.current_url == "https://www.example.com/"

@then("i should see a welcome message with my name")
def step_then_i_should_see_a_welcome_message_with_my_name(context):
    welcome_message = context.browser.find_element_by_xpath("//div[@class='welcome-message']")
    assert "Welcome, test" in welcome_message.text

Task: Write a program to find the sum of the digits of a given number.
