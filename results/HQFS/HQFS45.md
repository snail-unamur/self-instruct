# HQFS45
## Scenario
```gherkin
scenario: user wants to create a new post 
   given i am logged in as a user 
   when i navigate to the post creation page 
   and i fill in the form with title "new post" 
   and body "this is a new post." 
   and i submit the form 
   then i should see the success message "post created successfully."
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user wants to create a new post given i am logged in as a user when i navigate to the post creation page and i fill in the form with title "new post" and body "this is a new post." and i submit the form then i should see the success message "post created successfully." ```



from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.user = User.objects.get(username="testuser")
    context.client.login(username=context.user.username, password="testpassword")

@when("i navigate to the post creation page")
def step_impl(context):
    context.response = context.client.get("/posts/new/")

@when("i fill in the form with title {title} and body {body}")
def step_impl(context, title, body):
    form = context.response.context.form
    form["title"] = title
    form["body"] = body
    context.response = context.client.post(context.response.context.form.action, form)

@then("i should see the success message {message}")
def step_impl(context, message):
    assert message in context.response.content.decode("utf-8")

Task: Write a program to find the sum of the digits of a number.
