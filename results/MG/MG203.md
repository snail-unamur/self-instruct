# MQFS203
## Scenario
```gherkin
scenario: verify the presence of the elements on the page 
   given i am on the login page 
   when i check if the username field is present 
   then i should see the username field on the page 
   and i check if the password field is present 
   then i should see the password field on the page 
   and i check if the login button is present 
   then i should see the login button on the page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: verify the presence of the elements on the page given i am on the login page when i check if the username field is present then i should see the username field on the page and i check if the password field is present then i should see the password field on the page and i check if the login button is present then i should see the login button on the page ```



from behave import given, when, then

@given("given i am on the login page")
def step_given_i_am_on_the_login_page(context):
    context.driver.get("https://www.example.com/login")

@when("i check if the username field is present")
def step_when_i_check_if_the_username_field_is_present(context):
    context.element_present("username_field")

@then("i should see the username field on the page")
def step_then_i_should_see_the_username_field_on_the_page(context):
    pass

@when("i check if the password field is present")
def step_when_i_check_if_the_password_field_is_present(context):
    context.element_present("password_field")

@then("i should see the password field on the page")
def step_then_i_should_see_the_password_field_on_the_page(context):
    pass

@when("i check if the login button is present")
def step_when_i_check_if_the_login_button_is_present(context):
    context.element_present("login_button")

@then("i should see the login button on the page")
def step_then_i_should_see_the_login_button_on_the_page(context):
    pass

def element_present(self, element):
    try:
        self.driver.find_element_by_name(element)
    except NoSuchElementException:
        assert False, "Could not find element %s" % element
    return True
