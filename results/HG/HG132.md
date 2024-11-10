# HQFS132
## Scenario
```gherkin
scenario: 
   given a user is on the login page 
   when they enter their email 
   and password 
   and click the login button 
   then they should be taken to their dashboard page 
   and they should see their name 
   and profile picture 
   and they should see a logout button
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is on the login page when they enter their email and password and click the login button then they should be taken to their dashboard page and they should see their name and profile picture and they should see a logout button ```



from behave import given, when, then

@given("a user is on the login page")
def step_given_a_user_is_on_the_login_page(context):
    context.browser.get("https://www.example.com/login")

@when("they enter their email and password and click the login button")
def step_when_they_enter_their_email_and_password_and_click_the_login_button(context):
    email_field = context.browser.find_element_by_name("email")
    email_field.send_keys("user@example.com")

    password_field = context.browser.find_element_by_name("password")
    password_field.send_keys("password")

    login_button = context.browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

@then("they should be taken to their dashboard page")
def step_then_they_should_be_taken_to_their_dashboard_page(context):
    assert context.browser.current_url == "https://www.example.com/dashboard"

@then("they should see their name and profile picture")
def step_then_they_should_see_their_name_and_profile_picture(context):
    assert context.browser.find_element_by_xpath("//img[@src='/profile-picture.jpg']")
    assert context.browser.find_element_by_xpath("//h1[contains(text(), 'User Name')]")

@then("they should see a logout button")
def step_then_they_should_see_a_logout_button(context):
    assert context.browser.find_element_by_xpath("//button[@type='button'][contains(text(), 'Logout')]")
