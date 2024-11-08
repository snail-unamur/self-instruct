# HQFS47
## Scenario
```gherkin
scenario: user can upload a file 
   given i am on the upload page 
   when i select a file 
   and i click the upload button 
   then the file is uploaded 
   and i am taken to the success page
```


## Python Implementation
```python
from behave import given, when, then @given("i am on the upload page") def step_given_i_am_on_the_upload_page(context): context.driver.get("http://www.example.com/upload") @when("i select a file and i click the upload button") def step_when_i_select_a_file_and_i_click_the_upload_button(context): file_input = context.driver.find_element_by_id("file-input") file_input.send_keys("/path/to/file") upload_button = context.driver.find_element_by_id("upload-button") upload_button.click() @then("the file is uploaded and i am taken to the success page") def step_then_the_file_is_uploaded_and_i_am_taken_to_the_success_page(context): assert context.driver.current_url == "http://www.example.com/success"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can upload a file given i am on the upload page when i select a file and i click the upload button then the file is uploaded and i am taken to the success page ``` ```python from behave import given, when, then @given("i am on the upload page") def step_given_i_am_on_the_upload_page(context): context.driver.get("http://www.example.com/upload") @when("i select a file and i click the upload button") def step_when_i_select_a_file_and_i_click_the_upload_button(context): file_input = context.driver.find_element_by_id("file-input") file_input.send_keys("/path/to/file") upload_button = context.driver.find_element_by_id("upload-button") upload_button.click() @then("the file is uploaded and i am taken to the success page") def step_then_the_file_is_uploaded_and_i_am_taken_to_the_success_page(context): assert context.driver.current_url == "http://www.example.com/success" ```

Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number using recursion.
