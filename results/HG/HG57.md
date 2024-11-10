# HQFS57
## Scenario
```gherkin
scenario: testing the email service 
   given the email service is running 
   when i send an email to "john@example.com" 
   then the email should be delivered to "john@example.com" 
   when i send an email to "jane@example.com" 
   then the email should be delivered to "jane@example.com" 
   when i send an email to "jim@example.com" 
   then the email should be delivered to "jim@example.com"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the email service given the email service is running when i send an email to "john@example.com" then the email should be delivered to "john@example.com" when i send an email to "jane@example.com" then the email should be delivered to "jane@example.com" when i send an email to "jim@example.com" then the email should be delivered to "jim@example.com" ```



```python from behave import given, when, then

@given("the email service is running")
def step_given_the_email_service_is_running(context):
    context.email_service = EmailService()
    context.email_service.start()

@when("i send an email to {email}")
def step_when_i_send_an_email_to(context, email):
    context.email = Email(email)
    context.email_service.send_email(context.email)

@then("the email should be delivered to {email}")
def step_then_the_email_should_be_delivered_to(context, email):
    assert context.email_service.delivered_emails[-1].recipient == email

@given("the email service is running")
def step_given_the_email_service_is_running(context):
    context.email_service = EmailService()
    context.email_service.start()

@when("i send an email to {email}")
def step_when_i_send_an_email_to(context, email):
    context.email = Email(email)
    context.email_service.send_email(context.email)

@then("the email should be delivered to {email}")
def step_then_the_email_should_be_delivered_to(context, email):
    assert context.email_service.delivered_emails[-1].recipient == email

@given("the email service is running")
def step_given_the_email_service_is_running(context):
    context.email_service = EmailService()
    context.email_service.start()

@when("i send an email to {email}")
def step_when_i_send_an_email_to(context, email):
    context.email = Email(email)
    context.email_service.send_email(context.email)

@then("the email should be delivered to {email}")
def step_then_the_email_should_be_delivered_to(context, email):
    assert context.email_
