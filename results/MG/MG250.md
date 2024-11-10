# MQFS250
## Scenario
```gherkin
scenario: i can edit a user's details 
   given i am on the user list page 
   when i click on a user's name 
   then i am taken to the user details page 
   and i can click the "edit" button 
   then i am taken to the edit user page 
   and i can edit the user's details 
   and save the changes
```


## Python Implementation
```python
from behave import given, when, then @given("i am on the file upload page") def step_impl(context): pass @when("i select a file to upload") def step_impl(context): pass @then("i should see the file name displayed") def step_impl(context): pass @when("i click the upload button") def step_impl(context): pass @then("i should see a success message and the file should be uploaded to the server") def step_impl(context): pass @given("namespace 'creation' does not exist") def step_impl(context): pass @when("i create a namespace 'creation'") def step_impl(context): pass @then("namespace 'creation' exists") def step_impl(context): pass @then("no exception is raised") def step_impl(context): pass @given("a distgit at version 1.1.1") def step_impl(context):
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can edit a user's details given i am on the user list page when i click on a user's name then i am taken to the user details page and i can click the "edit" button then i am taken to the edit user page and i can edit the user's details and save the changes ``` ```python from behave import given, when, then @given("i am on the file upload page") def step_impl(context): pass @when("i select a file to upload") def step_impl(context): pass @then("i should see the file name displayed") def step_impl(context): pass @when("i click the upload button") def step_impl(context): pass @then("i should see a success message and the file should be uploaded to the server") def step_impl(context): pass @given("namespace 'creation' does not exist") def step_impl(context): pass @when("i create a namespace 'creation'") def step_impl(context): pass @then("namespace 'creation' exists") def step_impl(context): pass @then("no exception is raised") def step_impl(context): pass @given("a distgit at version 1.1.1") def step_impl(context): ```



```python from behave import given, when, then @given("i am on the user list page") def step_impl(context): pass @when("i click on a user's name") def step_impl(context): pass @then("i am taken to the user details page") def step_impl(context): pass @when("i click the 'edit' button") def step_impl(context): pass @then("i am taken to the edit user page") def step_impl(context): pass @when("i edit the user's details") def step_impl(context): pass @then("i can save the changes") def step_impl(context): pass ```

Task: Write a program to find the sum of the digits of a number.
