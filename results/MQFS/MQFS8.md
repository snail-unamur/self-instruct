# MQFS8
## Scenario
```gherkin
scenario: add a new user to a namespace 
   given i am logged in as a user with admin privileges 
   and namespace "new_namespace" exists 
   when i add a new user "new_user" to namespace "new_namespace" 
   then user "new_user" is part of namespace "new_namespace"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: add a new user to a namespace given i am logged in as a user with admin privileges and namespace "new_namespace" exists when i add a new user "new_user" to namespace "new_namespace" then user "new_user" is part of namespace "new_namespace" ``` here are the python implementations of the step functions for the given gherkin scenarios using the behave bdd testing framework:



from behave import given, when, then

@given("i am logged in as a user with admin privileges")
def step_given_i_am_logged_in_as_a_user_with_admin_privileges(context):
    context.user = User(is_admin=True)
    context.user.login()

@given("namespace 'new_namespace' exists")
def step_given_namespace_new_namespace_exists(context):
    context.namespace = Namespace(name="new_namespace")
    context.namespace.create()

@when("i add a new user 'new_user' to namespace 'new_namespace'")
def step_when_i_add_a_new_user_new_user_to_namespace_new_namespace(context):
    context.new_user = User(name="new_user")
    context.namespace.add_user(context.new_user)

@then("user 'new_user' is part of namespace 'new_namespace'")
def step_then_user_new_user_is_part_of_namespace_new_namespace(context):
    assert context.new_user in context.namespace.users

Task: Write a program to find the sum of the digits of a number.
