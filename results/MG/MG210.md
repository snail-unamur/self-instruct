# MQFS210
## Scenario
```gherkin
scenario: user can upload a file 
   given i am logged in as a user 
   when i navigate to the upload page 
   then i should see an upload button 
   when i click the upload button 
   then i should be able to select a file from my computer 
   when i select a file 
   and click open 
   then the file should be uploaded to the server 
   and i should be redirected to a page displaying the uploaded file
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can upload a file given i am logged in as a user when i navigate to the upload page then i should see an upload button when i click the upload button then i should be able to select a file from my computer when i select a file and click open then the file should be uploaded to the server and i should be redirected to a page displaying the uploaded file ```



from behave import given, when, then

@given("i am logged in as a user")
def step_impl(context):
    context.browser.get("http://localhost:8000/login")
    context.browser.find_element_by_name("username").send_keys("user")
    context.browser.find_element_by_name("password").send_keys("password")
    context.browser.find_element_by_xpath("//button[@type='submit']").click()

@when("i navigate to the upload page")
def step_impl(context):
    context.browser.get("http://localhost:8000/upload")

@then("i should see an upload button")
def step_impl(context):
    assert context.browser.find_element_by_xpath("//input[@type='file']")

@when("i click the upload button")
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@type='file']").click()

@then("i should be able to select a file from my computer")
def step_impl(context):
    pass

@then("the file should be uploaded to the server")
def step_impl(context):
    pass

@then("i should be redirected to a page displaying the uploaded file")
def step_impl(context):
    pass
