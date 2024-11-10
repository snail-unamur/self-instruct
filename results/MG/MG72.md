# MQFS72
## Scenario
```gherkin
scenario: testing the delete functionality 
   given i am logged in 
   and i am on the homepage 
   when i click on the delete button for a post 
   then the post should be deleted 
   and i should be redirected to the homepage 
   when i click on the delete button for a post that does not exist 
   then i should see an error message
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete functionality given i am logged in and i am on the homepage when i click on the delete button for a post then the post should be deleted and i should be redirected to the homepage when i click on the delete button for a post that does not exist then i should see an error message ```



from behave import given, when, then

@given("i am logged in and i am on the homepage")
def step_given(context):
    context.execute_steps("given i am logged in")
    context.execute_steps("given i am on the homepage")

@when("i click on the delete button for a post")
def step_when(context):
    context.post.delete()

@then("the post should be deleted and i should be redirected to the homepage")
def step_then(context):
    assert context.post.is_deleted()
    assert context.browser.current_url == context.base_url

@when("i click on the delete button for a post that does not exist")
def step_when_delete_non_existing_post(context):
    context.post.delete_non_existing()

@then("i should see an error message")
def step_then_see_error_message(context):
    assert context.post.error_message_is_displayed()


class Post:
    def __init__(self, context):
        self.context = context

    def delete(self):
        self.context.browser.visit(self.context.base_url + "/post/delete")

    def delete_non_existing(self):
        self.context.browser.visit(self.context.base_url + "/post/delete_non_existing")

    def is_deleted(self):
        # Check if the post is deleted
        pass

    def error_message_is_displayed(self):
        # Check if the error message is displayed
        pass


class Browser:
    def __init__(self, context):
        self.context = context

    def visit(self, url):
        # Visit the url
        pass

    def current_url(self):
        # Get the current url
        pass


class LoggedInUser:
    def __init__(self, context):
        self.context = context

    def login(self):
        # Log the user in
        pass


class HomePage:
    def __init__(self, context
