# HQFS119
## Scenario
```gherkin
scenario: i can find house prices by date, location 
   and type 
   given a house price search engine with july 2016 data 
   and i am on the search page 
   when i enter the start date of 14 july 
   and i enter an end date of 21 july 
   and i enter a location of "london" 
   and i select the type of property as "flat" 
   and i click the search button 
   then all house prices should be for sales between 14 july 
   and 21 july in london for flats.
```


## Python Implementation
```python
from behave import given, when, then @given("a configured git repo with multiple kramdown drafts") def step_given_a_configured_git_repo_with_multiple_kramdown_drafts(context): pass @when("the draft is broken") def step_when_the_draft_is_broken(context): pass @when("a non-broken draft is committed") def step_when_a_non_broken_draft_is_committed(context): pass @then("it succeeds") def step_then_it_succeeds(context): pass @given("i am logged in as a user") def step_given_i_am_logged_in_as_a_user(context): pass @when("i navigate to my posts page") def step_when_i_navigate_to_my_posts_page(context): pass @then("i should see a button to add a new post")

def step_then_i_should_see_a_button_to_add_a_new_post(context):
    assert context.browser.find_element_by_id("new-post-button")
@when("i click the button")
def step_when_i_click_the_button(context):
    context.browser.find_element_by_id("new-post-button").click()
@then("i should be taken to the new post page")
def step_then_i_should_be_taken_to_the_new_post_page(context):
    assert context.browser.current_url == "https://example.com/posts/new"
@when("i enter a title")
def step_when_i_enter_a_title(context):
    context.browser.find_element_by_id("title").send_keys("My new post")
@when("i enter a body")
def step_when_i_enter_a_body(context):
    context.browser.find_element_by_id("body").send_keys("This is the body of my new post")
@when("i click the publish button")
def step_when_i_click_the_publish_button(context):
    context.browser.find_element_by_id("publish-button").click()
@then("i should be taken to the post page")
def step_then_i_should_be_taken_to_the_post_page(context):
    assert context.browser.current_url == "https://example.com/posts/my-new-post"
@then("i should see the post title")
def step_then_i_should_see_the_post_title(context):
    assert context.browser.find_element_by_id("title").text == "My new post"
@then("i should see the post body")
def step_then_i_should_see_the_post_body(context):
    assert context.browser.find_element_by_id("body").text == "This is the body of my new post"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can find house prices by date, location and type given a house price search engine with july 2016 data and i am on the search page when i enter the start date of 14 july and i enter an end date of 21 july and i enter a location of "london" and i select the type of property as "flat" and i click the search button then all house prices should be for sales between 14 july and 21 july in london for flats. ``` ```python from behave import given, when, then @given("a configured git repo with multiple kramdown drafts") def step_given_a_configured_git_repo_with_multiple_kramdown_drafts(context): pass @when("the draft is broken") def step_when_the_draft_is_broken(context): pass @when("a non-broken draft is committed") def step_when_a_non_broken_draft_is_committed(context): pass @then("it succeeds") def step_then_it_succeeds(context): pass @given("i am logged in as a user") def step_given_i_am_logged_in_as_a_user(context): pass @when("i navigate to my posts page") def step_when_i_navigate_to_my_posts_page(context): pass @then("i should see a button to add a new post")

def step_then_i_should_see_a_button_to_add_a_new_post(context):
    assert context.browser.find_element_by_id("new-post-button")
@when("i click the button")
def step_when_i_click_the_button(context):
    context.browser.find_element_by_id("new-post-button").click()
@then("i should be taken to the new post page")
def step_then_i_should_be_taken_to_the_new_post_page(context):
    assert context.browser.current_url == "https://example.com/posts/new"
@when("i enter a title")
def step_when_i_enter_a_title(context):
    context.browser.find_element_by_id("title").send_keys("My new post")
@when("i enter a body")
def step_when_i_enter_a_body(context):
    context.browser.find_element_by_id("body").send_keys("This is the body of my new post")
@when("i click the publish button")
def step_when_i_click_the_publish_button(context):
    context.browser.find_element_by_id("publish-button").click()
@then("i should be taken to the post page")
def step_then_i_should_be_taken_to_the_post_page(context):
    assert context.browser.current_url == "https://example.com/posts/my-new-post"
@then("i should see the post title")
def step_then_i_should_see_the_post_title(context):
    assert context.browser.find_element_by_id("title").text == "My new post"
@then("i should see the post body")
def step_then_i_should_see_the_post_body(context):
    assert context.browser.find_element_by_id("body").text == "This is the body of my new post"
```

```python from behave import given, when, then

@given("a house
