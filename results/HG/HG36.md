# HQFS36
## Scenario
```gherkin
scenario: a user can edit an existing route 
   given a user is logged in as an admin 
   when they navigate to the "routes" page 
   and they edit an existing route 
   then the edited route should be saved
```


## Python Implementation
```python
from behave import given, when, then

@given("a user is logged in as an admin")
def step_impl(context):
    context.user = User(is_admin=True)
    context.user.login()

@when("they navigate to the 'routes' page")
def step_impl(context):
    context.routes_page = RoutesPage()
    context.routes_page.load()

@when("they edit an existing route")
def step_impl(context):
    context.existing_route = Route(name="Existing Route")
    context.routes_page.edit_route(context.existing_route)

@then("the edited route should be saved")
def step_impl(context):
    assert context.routes_page.get_route_by_name("Existing Route") == context.existing_route
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit an existing route given a user is logged in as an admin when they navigate to the "routes" page and they edit an existing route then the edited route should be saved ```



```python from behave import given, when, then

@given("a user is logged in as an admin")
def step_impl(context):
    context.user = User(is_admin=True)
    context.user.login()

@when("they navigate to the 'routes' page")
def step_impl(context):
    context.routes_page = RoutesPage()
    context.routes_page.load()

@when("they edit an existing route")
def step_impl(context):
    context.existing_route = Route(name="Existing Route")
    context.routes_page.edit_route(context.existing_route)

@then("the edited route should be saved")
def step_impl(context):
    assert context.routes_page.get_route_by_name("Existing Route") == context.existing_route
```

Task: Write a program to find the sum of the digits of a given number.
