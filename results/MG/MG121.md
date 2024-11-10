# MQFS121
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the update functionality given a user with id 12345 and name "jane doe" when i navigate to the user page then i see an edit button for the user when i

click the edit button then i see a form to update the user's name and email when i update the user's name to "jane doe smith" and email to "[jane.doe.smith@gmail.com](mailto:jane.doe.smith@gmail.com)" then i see the updated name and email on the user page

from behave import given, when, then

@given("a user with id 12345 and name 'jane doe'")
def step_given_a_user_with_id_12345_and_name_jane_doe(context):
    context.user = {
        "id": 12345,
        "name": "jane doe",
        "email": "jane.doe@gmail.com"
    }

@when("i navigate to the user page")
def step_when_i_navigate_to_the_user_page(context):
    pass

@when("i see an edit button for the user")
def step_when_i_see_an_edit_button_for_the_user(context):
    pass

@when("i click the edit button")
def step_when_i_click_the_edit_button(context):
    pass

@when("i see a form to update the user's name and email")
def step_when_i_see_a_form_to_update_the_user_s_name_and_email(context):
    pass

@when("i update the user's name to 'jane doe smith' and email to '[jane.doe.smith@gmail.com](mailto:jane.doe.smith@gmail.com)'")
def step_when_i_update_the_user_s_name_to_jane_doe_smith_and_email_to_jane.doe.smithgmail.com(context):
    context.user["name"] = "jane doe smith"
    context.user["email"] = "jane.doe.smith@gmail.com"

@then("i see the updated name and email on
