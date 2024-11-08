# HQFS146
## Scenario
```gherkin
scenario: 
   given a user with name "john doe" 
   and email "johndoe@example.com" 
   when i send an email to "johndoe@example.com" with subject "test" 
   and body "this is a test email" 
   then the email should be delivered to "john doe" with subject "test" 
   and body "this is a test email"
```


## Python Implementation
```python
from behave import given, when, then

@given("a user with name 'john doe' and email 'johndoe@example.com'")
def step_given_a_user_with_name_john_doe_and_email_johndoe_example_com(context):
    context.user = {"name": "john doe", "email": "johndoe@example.com"}

@when("i send an email to 'johndoe@example.com' with subject 'test' and body 'this is a test email'")
def step_when_i_send_an_email_to_johndoe_example_com_with_subject_test_and_body_this_is_a_test_email(context):
    context.email = {"to": "johndoe@example.com", "subject": "test", "body": "this is a test email"}

@then("the email should be delivered to 'john doe' with subject 'test' and body 'this is a test email'")
def step_then_the_email_should_be_delivered_to_john_doe_with_subject_test_and_body_this_is_a_test_email(context):
    assert context.email == {"to": "johndoe@example.com", "subject": "test", "body": "this is a test email"}
    assert context.user == {"name": "john doe", "email": "johndoe@example.com"}
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user with name "john doe" and email "johndoe@example.com" when i send an email to "johndoe@example.com" with subject "test" and body "this is a test email" then the email should be delivered to "john doe" with subject "test" and body "this is a test email" ```



```python from behave import given, when, then

@given("a user with name 'john doe' and email 'johndoe@example.com'")
def step_given_a_user_with_name_john_doe_and_email_johndoe_example_com(context):
    context.user = {"name": "john doe", "email": "johndoe@example.com"}

@when("i send an email to 'johndoe@example.com' with subject 'test' and body 'this is a test email'")
def step_when_i_send_an_email_to_johndoe_example_com_with_subject_test_and_body_this_is_a_test_email(context):
    context.email = {"to": "johndoe@example.com", "subject": "test", "body": "this is a test email"}

@then("the email should be delivered to 'john doe' with subject 'test' and body 'this is a test email'")
def step_then_the_email_should_be_delivered_to_john_doe_with_subject_test_and_body_this_is_a_test_email(context):
    assert context.email == {"to": "johndoe@example.com", "subject": "test", "body": "this is a test email"}
    assert context.user == {"name": "john doe", "email": "johndoe@example.com"}
```

Task: Write a program to find the sum of the digits of a number.
