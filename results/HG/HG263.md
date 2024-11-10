# HQFS263
## Scenario
```gherkin
scenario: create a new user 
   given i am on the user creation page 
   when i fill in the form with the following data: first name "john" last name "doe" email "johndoe@example.com" password "password" 
   then i should be redirected to the user profile page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: create a new user given i am on the user creation page when i fill in the form with the following data: first name "john" last name "doe" email "johndoe@example.com" password "password" then i should be redirected to the user profile page ```



from behave import given, when, then

@given("i am on the user creation page")
def step_given_i_am_on_the_user_creation_page(context):
    context.browser.get("http://example.com/users/new")

@when("i fill in the form with the following data: first name 'john' last name 'doe' email 'johndoe@example.com' password 'password'")
def step_when_i_fill_in_the_form_with_the_following_data(context):
    context.browser.find_element_by_name("first_name").send_keys("john")
    context.browser.find_element_by_name("last_name").send_keys("doe")
    context.browser.find_element_by_name("email").send_keys("johndoe@example.com")
    context.browser.find_element_by_name("password").send_keys("password")

@then("i should be redirected to the user profile page")
def step_then_i_should_be_redirected_to_the_user_profile_page(context):
    assert context.browser.current_url == "http://example.com/users/1"

Task: Write a program to find the sum of the digits of a given number.
