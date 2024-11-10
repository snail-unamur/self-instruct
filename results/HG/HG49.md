# HQFS49
## Scenario
```gherkin
scenario: testing the file upload service 
   given i have a file upload service 
   when i upload a file named "test.txt" with content "this is a test file" 
   then the file should be uploaded successfully 
   when i download the file named "test.txt" 
   then i should get the file with content "this is a test file
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the file upload service given i have a file upload service when i upload a file named "test.txt" with content "this is a test file" then the file should be uploaded successfully when i download the file named "test.txt" then i should get the file with content "this is a test file

```

from behave import given, when, then
import os

@given("i have a file upload service")
def step_given_i_have_a_file_upload_service(context):
    context.upload_service = FileUploadService()

@when("i upload a file named 'test.txt' with content 'this is a test file'")
def step_when_i_upload_a_file_named_test_txt_with_content_this_is_a_test_file(context):
    test_file = open("test.txt", "w")
    test_file.write("this is a test file")
    test_file.close()
    context.upload_service.upload_file("test.txt")

@then("the file should be uploaded successfully")
def step_then_the_file_should_be_uploaded_successfully(context):
    assert context.upload_service.file_uploaded("test.txt")

@when("i download the file named 'test.txt'")
def step_when_i_download_the_file_named_test_txt(context):
    context.downloaded_file = context.upload_service.download_file("test.txt")

@then("i should get the file with content 'this is a test file'")
def step_then_i_should_get_the_file_with_content_this_is_a_test_file(context):
    downloaded_file_content = open(context.downloaded_file, "r").read()
    assert downloaded_file_content == "this is a test file"
    os.remove(context.downloaded_file)

Task: Write a program to find the sum of the digits of a number.
