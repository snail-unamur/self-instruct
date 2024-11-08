# MQFS285
## Scenario
```gherkin
scenario: manage user permissions 
   given a user "john" exists 
   when i grant "john" the "admin" permission 
   then "john" has the "admin" permission 
   when i revoke "john" the "admin" permission 
   then "john" does not have the "admin" permission
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: manage user permissions given a user "john" exists when i grant "john" the "admin" permission then "john" has the "admin" permission when i revoke "john" the "admin" permission then "john" does not have the "admin" permission ```



from behave import given, when, then

@given("a user 'john' exists")
def step_given_a_user_john_exists(context):
    context.user = User("john")

@when("i grant 'john' the 'admin' permission")
def step_when_i_grant_john_the_admin_permission(context):
    context.permission = Permission("admin")
    context.user.permissions.append(context.permission)

@then("'john' has the 'admin' permission")
def step_then_john_has_the_admin_permission(context):
    assert context.permission in context.user.permissions

@when("i revoke 'john' the 'admin' permission")
def step_when_i_revoke_john_the_admin_permission(context):
    context.permission = Permission("admin")
    context.user.permissions.remove(context.permission)

@then("'john' does not have the 'admin' permission")
def step_then_john_does_not_have_the_admin_permission(context):
    assert context.permission not in context.user.permissions
