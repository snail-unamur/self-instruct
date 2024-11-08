# HQFS23
## Scenario
```gherkin
scenario: data access control 
   given a user 
   and a resource 
   when the user requests access to the resource 
   then the system should grant or deny access based on the user's permissions
```


## Python Implementation
```python
from behave import given, when, then

@given("a user and a resource")
def step_given_a_user_and_a_resource(context):
    context.user = User()
    context.resource = Resource()

@when("the user requests access to the resource")
def step_when_the_user_requests_access_to_the_resource(context):
    context.access_request = context.user.request_access_to(context.resource)

@then("the system should grant or deny access based on the user's permissions")
def step_then_the_system_should_grant_or_deny_access_based_on_the_user_s_permissions(context):
    if context.user.has_permission_to(context.resource):
        assert context.access_request.granted
    else:
        assert not context.access_request.granted
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: data access control given a user and a resource when the user requests access to the resource then the system should grant or deny access based on the user's permissions ```



```python from behave import given, when, then

@given("a user and a resource")
def step_given_a_user_and_a_resource(context):
    context.user = User()
    context.resource = Resource()

@when("the user requests access to the resource")
def step_when_the_user_requests_access_to_the_resource(context):
    context.access_request = context.user.request_access_to(context.resource)

@then("the system should grant or deny access based on the user's permissions")
def step_then_the_system_should_grant_or_deny_access_based_on_the_user_s_permissions(context):
    if context.user.has_permission_to(context.resource):
        assert context.access_request.granted
    else:
        assert not context.access_request.granted
```

Task: Write a program to find the sum of the digits of a given number.
