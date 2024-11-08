# HQFS271
## Scenario
```gherkin
scenario: an authenticated user can list all logs 
   given that the user has valid credentials 
   and the

user is authorized to access the logs


   Given an authenticated user

   When the user requests to list all logs

   Then the user should see a list of all logs

Scenario: an unauthenticated user cannot list all logs


   Given an unauthenticated user

   When the user requests to list all logs

   Then the user should see an error message

Scenario: an authenticated user cannot list all logs if the user is not authorized


   Given an authenticated user

   When the user requests to list all logs

   And the user is not authorized

   Then the user should see an error message
```


## Python Implementation
```python
from behave import given, when, then

@given("an authenticated user")
def step_given_an_authenticated_user(context):
    context.user = User(is_authenticated=True)

@given("an unauthenticated user")
def step_given_an_unauthenticated_user(context):
    context.user = User(is_authenticated=False)

@when("the user requests to list all logs")
def step_when_the_user_requests_to_list_all_logs(context):
    context.response = context.user.list_logs()

@then("the user should see a list of all logs")
def step_then_the_user_should_see_a_list_of_all_logs(context):
    assert context.response == list(Log.objects.all())

@then("the user should see an error message")
def step_then_the_user_should_see_an_error_message(context):
    assert "error" in context.response

@given("the user is not authorized")
def step_given_the_user_is_not_authorized(context):
    context.user.is_authorized = False
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: an authenticated user can list all logs given that the user has valid credentials and the

user is authorized to access the logs

Given an authenticated user
When the user requests to list all logs
Then the user should see a list of all logs

Scenario: an unauthenticated user cannot list all logs

Given an unauthenticated user
When the user requests to list all logs
Then the user should see an error message

Scenario: an authenticated user cannot list all logs if the user is not authorized

Given an authenticated user
When the user requests to list all logs
And the user is not authorized
Then the user should see an error message
```

```python
from behave import given, when, then

@given("an authenticated user")
def step_given_an_authenticated_user(context):
    context.user = User(is_authenticated=True)

@given("an unauthenticated user")
def step_given_an_unauthenticated_user(context):
    context.user = User(is_authenticated=False)

@when("the user requests to list all logs")
def step_when_the_user_requests_to_list_all_logs(context):
    context.response = context.user.list_logs()

@then("the user should see a list of all logs")
def step_then_the_user_should_see_a_list_of_all_logs(context):
    assert context.response == list(Log.objects.all())

@then("the user should see an error message")
def step_then_the_user_should_see_an_error_message(context):
    assert "error" in context.response

@given("the user is not authorized")
def step_given_the_user_is_not_authorized(context):
    context.user.is_authorized = False
```
