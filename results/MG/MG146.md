# MQFS146
## Scenario
```gherkin
scenario: testing the edit functionality 
   given i am logged in as an admin 
   and i am on the user list page 
   when i click on the edit button for a user 
   then i should see the edit user form 
   and i should see the name field 
   and i should see the email field 
   and i should see the password field 
   and i should see the confirm password field 
   when i update the user details 
   then i should see the success message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the edit functionality given i am logged in as an admin and i am on the user list page when i click on the edit button for a user then i should see the edit user form and i should see the name field and i should see the email field and i should see the password field and i should see the confirm password field when i update the user details then i should see the success message ```



```python from behave import given, when, then

@given("i am logged in as an admin")
def step_impl(context):
    context.admin = Admin(username="admin", password="password")
    context.admin.login()

@given("i am on the user list page")
def step_impl(context):
    context.driver.get(context.base_url + "/admin/users")

@when("i click on the edit button for a user")
def step_impl(context):
    context.user = User.get_by_id(1)
    context.driver.find_element_by_id("edit_user_button").click()

@then("i should see the edit user form")
def step_impl(context):
    assert context.driver.find_element_by_id("edit_user_form")

@then("i should see the name field")
def step_impl(context):
    assert context.driver.find_element_by_id("name_field")

@then("i should see the email field")
def step_impl(context):
    assert context.driver.find_element_by_id("email_field")

@then("i should see the password field")
def step_impl(context):
    assert context.driver.find_element_by_id("password_field")

@then("i should see the confirm password field")
def step_impl(context):
    assert context.driver.find_element_by_id("confirm_password_field")

@when("i update the user details")
def step_impl(context):
    context.driver.find_element_by_id("name_field").send_keys("new_name")
    context.driver.find_element_by_id("email_field").send_keys("new_email@example.com")
    context.driver.find_element_by_id("password_field").send_keys("new_password")
    context.driver.find_element_by_id("confirm_password_field").send_keys("new_password")
    context.driver.find_element_by_id("update_button").click()
