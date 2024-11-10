# HQFS135
## Scenario
```gherkin
scenario: 
   given a user has an account with the following details: | username | password | email | | --- | --- | --- | | user1 | pass1 | user1@gmail.com | 
   when the user clicks on the password reset link 
   then the user should be taken to a page where they can reset their password
```


## Python Implementation
```python
from behave import given, when, then

@given("a user has an account with the following details:")
def step_impl(context):
    context.user = User(username="user1", password="pass1", email="user1@gmail.com")

@when("the user clicks on the password reset link")
def step_impl(context):
    context.user.reset_password_link()

@then("the user should be taken to a page where they can reset their password")
def step_impl(context):
    assert context.user.current_page.url == "password_reset_page_url"

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def reset_password_link(self):
        # code to click on the password reset link
        pass

class Page:
    def __init__(self, url):
        self.url = url

password_reset_page = Page("password_reset_page_url")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user has an account with the following details: | username | password | email | | --- | --- | --- | | user1 | pass1 | user1@gmail.com | when the user clicks on the password reset link then the user should be taken to a page where they can reset their password ```



```python from behave import given, when, then

@given("a user has an account with the following details:")
def step_impl(context):
    context.user = User(username="user1", password="pass1", email="user1@gmail.com")

@when("the user clicks on the password reset link")
def step_impl(context):
    context.user.reset_password_link()

@then("the user should be taken to a page where they can reset their password")
def step_impl(context):
    assert context.user.current_page.url == "password_reset_page_url"

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def reset_password_link(self):
        # code to click on the password reset link
        pass

class Page:
    def __init__(self, url):
        self.url = url

password_reset_page = Page("password_reset_page_url")
```

Task: Write a program to find the sum of the digits of a given number.
