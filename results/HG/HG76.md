# HQFS76
## Scenario
```gherkin
scenario: user edits a post 
   given the user is on the homepage 
   when the user clicks on the "edit" button for a post 
   then the user should be redirected to the "edit post" page 
   when the user edits the title 
   and body of the post 
   then the user should be able to save the changes 
   and the user should be redirected to the post page 
   and the post should be updated with the new title 
   and body
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is on the homepage")
def step_given_the_user_is_on_the_homepage(context):
    context.homepage = HomePage(context.browser)
    context.homepage.load()

@when("the user clicks on the 'edit' button for a post")
def step_when_the_user_clicks_on_the_edit_button_for_a_post(context):
    post = context.homepage.get_random_post()
    context.edit_post_page = post.click_edit_button()

@then("the user should be redirected to the 'edit post' page")
def step_then_the_user_should_be_redirected_to_the_edit_post_page(context):
    assert isinstance(context.edit_post_page, EditPostPage)

@when("the user edits the title and body of the post")
def step_when_the_user_edits_the_title_and_body_of_the_post(context):
    context.edit_post_page.edit("New Title", "New Body")

@then("the user should be able to save the changes")
def step_then_the_user_should_be_able_to_save_the_changes(context):
    post_page = context.edit_post_page.click_save()

@then("the user should be redirected to the post page")
def step_then_the_user_should_be_redirected_to_the_post_page(context):
    assert isinstance(post_page, PostPage)

@then("the post should be updated with the new title and body")
def step_then_the_post_should_be_updated_with_the_new_title_and_body(context):
    post = context.homepage.get_random_post()
    assert post.title == "New Title"
    assert post.body == "New Body"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user edits a post given the user is on the homepage when the user clicks on the "edit" button for a post then the user should be redirected to the "edit post" page when the user edits the title and body of the post then the user should be able to save the changes and the user should be redirected to the post page and the post should be updated with the new title and body ```



```python from behave import given, when, then

@given("the user is on the homepage")
def step_given_the_user_is_on_the_homepage(context):
    context.homepage = HomePage(context.browser)
    context.homepage.load()

@when("the user clicks on the 'edit' button for a post")
def step_when_the_user_clicks_on_the_edit_button_for_a_post(context):
    post = context.homepage.get_random_post()
    context.edit_post_page = post.click_edit_button()

@then("the user should be redirected to the 'edit post' page")
def step_then_the_user_should_be_redirected_to_the_edit_post_page(context):
    assert isinstance(context.edit_post_page, EditPostPage)

@when("the user edits the title and body of the post")
def step_when_the_user_edits_the_title_and_body_of_the_post(context):
    context.edit_post_page.edit("New Title", "New Body")

@then("the user should be able to save the changes")
def step_then_the_user_should_be_able_to_save_the_changes(context):
    post_page = context.edit_post_page.click_save()

@then("the user should be redirected to the post page")
def step_then_the_user_should_be_redirected_to_the_post_page(context):
    assert isinstance(post_page, PostPage)

@then("the post should be updated with the new title and body")
def step_then_the_post_should_be_updated_with_the_new_title_and_body(context):
    post = context.homepage.get_random_post()
    assert post.title == "New Title"
    assert post.body == "New Body"
```

Task: Write a program to find the sum of the digits of a number.
