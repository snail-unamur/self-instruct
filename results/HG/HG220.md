# HQFS220
## Scenario
```gherkin
scenario: testing the file upload functionality 
   given a user with username "johndoe" 
   and password "pass123" 
   when the user logs in with username "johndoe" 
   and password "pass12323" 
   then the user is not logged in 
   and 
   when the user tries to upload a file with invalid format 
   then the file is not uploaded 
   and an error message is displayed
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the file upload functionality given a user with username "johndoe" and password "pass123" when the user logs in with username "johndoe" and password "pass12323" then the user is not logged in and when the user tries to upload a file with invalid format then the file is not uploaded and an error message is displayed ```



from behave import given, when, then

@given("a user with username 'johndoe' and password 'pass123'")
def step_impl(context):
    context.user = User("johndoe", "pass123")

@when("the user logs in with username 'johndoe' and password 'pass12323'")
def step_impl(context):
    context.user.login("pass12323")

@then("the user is not logged in")
def step_impl(context):
    assert not context.user.is_logged_in

@when("the user tries to upload a file with invalid format")
def step_impl(context):
    context.file = File("invalid.txt")
    context.result = context.user.upload_file(context.file)

@then("the file is not uploaded")
def step_impl(context):
    assert not context.file.is_uploaded

@then("an error message is displayed")
def step_impl(context):
    assert context.result.contains("Invalid format")

Task: Write a program to find the sum of the digits of a number.
