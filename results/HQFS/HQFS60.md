# HQFS60
## Scenario
```gherkin
scenario: 
   given a user is logged in 
   when the user navigates to the account settings page 
   then the user should see the account settings page 
   and the user should see a delete account button 
   when the user clicks the delete account button 
   then the user should see a confirmation dialog 
   and the user should see a confirm button 
   and the user should see a cancel button 
   when the user clicks the confirm button 
   then the user should see a success message 
   and the user should be logged out
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user is logged in when the user navigates to the account settings page then the user should see the account settings page and the user should see a delete account button when the user clicks the delete account button then the user should see a confirmation dialog and the user should see a confirm button and the user should see a cancel button when the user clicks the confirm button then the user should see a success message and the user should be logged out ```



```python from behave import given, when, then

@given("a user is logged in")
def step_given_a_user_is_logged_in(context):
    context.user = User()
    context.user.login()

@when("the user navigates to the account settings page")
def step_when_the_user_navigates_to_the_account_settings_page(context):
    context.account_settings_page = AccountSettingsPage()
    context.account_settings_page.navigate_to()

@then("the user should see the account settings page")
def step_then_the_user_should_see_the_account_settings_page(context):
    assert context.account_settings_page.is_displayed()

@then("the user should see a delete account button")
def step_then_the_user_should_see_a_delete_account_button(context):
    assert context.account_settings_page.delete_account_button.is_displayed()

@when("the user clicks the delete account button")
def step_when_the_user_clicks_the_delete_account_button(context):
    context.confirmation_dialog = ConfirmationDialog()
    context.account_settings_page.delete_account_button.click()

@then("the user should see a confirmation dialog")
def step_then_the_user_should_see_a_confirmation_dialog(context):
    assert context.confirmation_dialog.is_displayed()

@then("the user should see a confirm button")
def step_then_the_user_should_see_a_confirm_button(context):
    assert context.confirmation_dialog.confirm_button.is_displayed()

@then("the user should see a cancel button")
def step_then_the_user_should_see_a_cancel_button(context):
    assert context.confirmation_dialog.cancel_button.is_displayed()

@when("the user clicks the confirm button")
def step_when_the_user_clicks_the_confirm_button(context):
    context.success_
