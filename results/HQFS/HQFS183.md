# HQFS183
## Scenario
```gherkin
scenario: 
   given i am on the login page 
   when i enter my email 
   and password 
   and click submit 
   then i should be logged in
```


## Python Implementation
```python
from behave import given, when, then @given("i am on the login page") def step_given_i_am_on_the_login_page(context): pass @when("i enter my email and password and click submit") def step_when_i_enter_my_email_and_password_and_click_submit(context): pass @then("i should be logged in") def step_then_i_should_be_logged_in(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given i am on the login page when i enter my email and password and click submit then i should be logged in ``` ```python from behave import given, when, then @given("i am on the login page") def step_given_i_am_on_the_login_page(context): pass @when("i enter my email and password and click submit") def step_when_i_enter_my_email_and_password_and_click_submit(context): pass @then("i should be logged in") def step_then_i_should_be_logged_in(context): pass ```



```python from behave import given, when, then @given("i am on the login page") def step_given_i_am_on_the_login_page(context): context.browser.get('https://www.example.com/login') @when("i enter my email and password and click submit") def step_when_i_enter_my_email_and_password_and_click_submit(context): email_field = context.browser.find_element_by_name('email') email_field.send_keys('test@example.com') password_field = context.browser.find_element_by_name('password') password_field.send_keys('password') submit_button = context.browser.find_element_by_xpath("//button[@type='submit']") submit_button.click() @then("i should be logged in") def step_then_i_should_be_logged_in(context): logged_in_element = context.browser.find_element_by_xpath("//div[contains(text(), 'Welcome')]") assert logged_in_element.is_displayed() ```

Task: Write a program to find the sum of the digits of a number.
