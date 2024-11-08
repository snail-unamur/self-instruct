# HQFS171
## Scenario
```gherkin
scenario: a user can register 
   and login to the website 
   given i am on the website registration page 
   when i fill in the registration form with the following data: | username | password | email | | testuser | testpassword | testuser@example.com | 
   and i submit the registration form 
   then i should be registered 
   and logged in 
   and i should be redirected to the homepage 
   given i am on the website login page 
   when i fill in the login form with the following data: | username | password | | testuser | testpassword | 
   and i submit the login form 
   then i should be logged in 
   and i should be redirected to the homepage
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can register and login to the website given i am on the website registration page when i fill in the registration form with the following data: | username | password | email | | testuser | testpassword | testuser@example.com | and i submit the registration form then i should be registered and logged in and i should be redirected to the homepage given i am on the website login page when i fill in the login form with the following data: | username | password | | testuser | testpassword | and i submit the login form then i should be logged in and i should be redirected to the homepage ```



```python from behave import given, when, then

@given("i am on the website registration page")
def step_given_i_am_on_the_website_registration_page(context):
    context.browser.get("http://www.example.com/register")

@when("i fill in the registration form with the following data:")
def step_when_i_fill_in_the_registration_form_with_the_following_data(context):
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")
    context.browser.find_element_by_name("email").send_keys("testuser@example.com")

@when("i submit the registration form")
def step_when_i_submit_the_registration_form(context):
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@then("i should be registered and logged in")
def step_then_i_should_be_registered_and_logged_in(context):
    assert "Logout" in context.browser.page_source

@then("i should be redirected to the homepage")
def step_then_i_should_be_redirected_to_the_homepage(context):
    assert context.browser.current_url == "http://www.example.com/"

@given("i am on the website login page")
def step_given_i_am_on_the_website_login_page(context):
    context.browser.get("http://www.example.com/login")

@when("i fill in the login form with the following data:")
def step_when_i_fill_in_the_login_form_with_the_following_data(context):
    context.browser.find_element_by_name("username").send_keys("testuser")
    context.browser.find_element_by_name("password").send_keys("testpassword")

@when("i submit the login
