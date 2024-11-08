# HQFS28
## Scenario
```gherkin
scenario: i can view a list of all users 
   given i am logged in as an admin 
   when i navigate to the "users" page 
   then i should see a list of all users 
   when i click on a user 
   then i should see the user details page 
   when i click on the edit button 
   then i should see a form to edit the user details 
   when i edit the user details 
   and click on the submit button 
   then i should see the updated user details in the list of all users 
   when i click on the delete button 
   then i should see a confirmation dialog 
   when i confirm the deletion 
   then i should see the user removed from the list of all users
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can view a list of all users given i am logged in as an admin when i navigate to the "users" page then i should see a list of all users when i click on a user then i should see the user details page when i click on the edit button then i should see a form to edit the user details when i edit the user details and click on the submit button then i should see the updated user details in the list of all users when i click on the delete button then i should see a confirmation dialog when i confirm the deletion then i should see the user removed from the list of all users ```



```python from behave import given, when, then

@given("i am logged in as an admin")
def step_impl(context):
    context.admin = Admin(username="admin", password="password")
    context.admin.login()

@when("i navigate to the 'users' page")
def step_impl(context):
    context.s = UsersPage(context.driver)
    context.s.visit()

@then("i should see a list of all users")
def step_impl(context):
    assert context.s.users_exist()

@when("i click on a user")
def step_impl(context):
    context.user = context.s.click_on_user()

@then("i should see the user details page")
def step_impl(context):
    assert context.user.on_user_details_page()

@when("i click on the edit button")
def step_impl(context):
    context.user_form = context.user.click_edit()

@then("i should see a form to edit the user details")
def step_impl(context):
    assert context.user_form.on_edit_form()

@when("i edit the user details and click on the submit button")
def step_impl(context):
    context.user_form.edit(firstname="New", lastname="Name")
    context.user_form.submit()

@then("i should see the updated user details in the list of all users")
def step_impl(context):
    assert context.s.user_in_list(context.user.firstname, context.user.lastname)

@when("i click on the delete button")
def step_impl(context):
    context.delete_dialog = context.user.click_delete()

@then("i should see a confirmation dialog")
def step_impl(context):
    assert context.delete_dialog.on_delete_dialog()

@when("i confirm the deletion")
def step_impl(context):
    context.delete_dialog.confirm()

@then("i should see the user removed from the list of all users")
def step_impl
