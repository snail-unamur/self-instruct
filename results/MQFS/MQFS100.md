# MQFS100
## Scenario
```gherkin
scenario: testing the file upload feature 
   given i am on the file upload page 
   when i select a file to upload 
   then i should see the file name displayed 
   when i click the upload button 
   then i should see a success message 
   and the file should be uploaded to the server
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the file upload feature given i am on the file upload page when i select a file to upload then i should see the file name displayed when i click the upload button then i should see a success message and the file should be uploaded to the server ```



from behave import given, when, then

@given("i am on the file upload page")
def step(context):
    context.browser.get("http://www.example.com/upload")

@when("i select a file to upload")
def step(context):
    context.file_input = context.browser.find_element_by_name("file")
    context.file_input.send_keys("/path/to/my/file")

@then("i should see the file name displayed")
def step(context):
    assert context.file_input.get_attribute("value") == "/path/to/my/file"

@when("i click the upload button")
def step(context):
    context.browser.find_element_by_name("upload").click()

@then("i should see a success message and the file should be uploaded to the server")
def step(context):
    assert "File uploaded successfully" in context.browser.page_source
    # Additional checks to confirm the file was uploaded to the server

Task: Write a program to find the sum of the digits of a number.
