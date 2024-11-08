# HQFS243
## Scenario
```gherkin
scenario: user wants to edit a comment on a post 
   given user is logged in 
   and on the post page 
   when user clicks on the edit button for the comment 
   then

user is taken to the edit comment page

   when user edits the comment

   and user clicks on the save button

   then the comment is updated

   and user is taken back to the post page
```


## Python Implementation
```python
from behave import given, when, then

@given("user is logged in and on the post page")
def step_impl(context):
    context.execute_steps("Given user is logged in")
    context.execute_steps("Given user is on the post page")

@when("user clicks on the edit button for the comment")
def step_impl(context):
    context.post_page.click_edit_comment_button()

@then("user is taken to the edit comment page")
def step_impl(context):
    assert context.edit_comment_page.current_url == context.edit_comment_page.url

@when("user edits the comment")
def step_impl(context):
    context.edit_comment_page.edit_comment("new comment text")

@when("user clicks on the save button")
def step_impl(context):
    context.edit_comment_page.click_save_button()

@then("the comment is updated")
def step_impl(context):
    assert context.post_page.get_comment_text() == "new comment text"

@then("user is taken back to the post page")
def step_impl(context):
    assert context.post_page.current_url == context.post_page.url
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to edit a comment on a post given user is logged in and on the post page when user clicks on the edit button for the comment then

user is taken to the edit comment page
when user edits the comment
and user clicks on the save button
then the comment is updated
and user is taken back to the post page
```

```python from behave import given, when, then

@given("user is logged in and on the post page")
def step_impl(context):
    context.execute_steps("Given user is logged in")
    context.execute_steps("Given user is on the post page")

@when("user clicks on the edit button for the comment")
def step_impl(context):
    context.post_page.click_edit_comment_button()

@then("user is taken to the edit comment page")
def step_impl(context):
    assert context.edit_comment_page.current_url == context.edit_comment_page.url

@when("user edits the comment")
def step_impl(context):
    context.edit_comment_page.edit_comment("new comment text")

@when("user clicks on the save button")
def step_impl(context):
    context.edit_comment_page.click_save_button()

@then("the comment is updated")
def step_impl(context):
    assert context.post_page.get_comment_text() == "new comment text"

@then("user is taken back to the post page")
def step_impl(context):
    assert context.post_page.current_url == context.post_page.url
```

Task: Write a program to find the sum of the digits of a number.
