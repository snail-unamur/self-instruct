# MQFS75
## Scenario
```gherkin
scenario: user can upload a file 
   given user is on the homepage 
   when user clicks on the "upload" button 
   then user is redirected to the upload page 
   and user sees a form to upload a file with a file input 
   and a submit button 
   when user selects a file 
   and clicks on the submit button 
   then user is redirected to the homepage 
   and user sees the uploaded file with the title, author, 
   and date
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can upload a file given user is on the homepage when user clicks on the "upload" button then user is redirected to the upload page and user sees a form to upload a file with a file input and a submit button when user selects a file and clicks on the submit button then user is redirected to the homepage and user sees the uploaded file with the title, author, and date ```



from behave import given, when, then

@given("user is on the homepage")
def step_given_user_is_on_homepage(context):
    context.homepage = HomePage()
    context.homepage.open()

@when("user clicks on the 'upload' button")
def step_when_user_clicks_on_upload_button(context):
    context.upload_page = context.homepage.click_upload_button()

@then("user is redirected to the upload page and user sees a form to upload a file with a file input and a submit button")
def step_then_user_is_redirected_to_upload_page(context):
    context.assertIsInstance(context.upload_page, UploadPage)
    context.assertUploadFormIsDisplayed()

@when("user selects a file and clicks on the submit button")
def step_when_user_selects_a_file_and_clicks_on_submit_button(context):
    context.upload_page.select_file()
    context.homepage = context.upload_page.click_submit_button()

@then("user is redirected to the homepage and user sees the uploaded file with the title, author, and date")
def step_then_user_is_redirected_to_homepage_and_user_sees_uploaded_file(context):
    context.assertIsInstance(context.homepage, HomePage)
    context.assertUploadedFileIsDisplayed()


Task: Write a program to find the sum of the digits of a number.
