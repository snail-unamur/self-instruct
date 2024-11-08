# HQFS133
## Scenario
```gherkin
scenario: i can update a user 
   given a user with id 123 
   and the user has name "john doe" 
   and the user has email "[johndoe@example.com](mailto:johndoe@example.com)" 
   when i update the user with id 123 with name "jane doe" 
   and i update the user with id 123 with email "[janedoe@example.com](mailto:janedoe@example.com)" 
   then the user with id 123 has name "jane doe" 
   and the user with id 123 has email "[janedoe@example.com](mailto:janedoe@example.com)"
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a user with id 123 and the user has name 'john doe' and the user has email 'johndoe@example.com'")
def step_impl(context):
    context.user = {"id": 123, "name": "john doe", "email": "johndoe@example.com"}

@when("i update the user with id 123 with name 'jane doe'")
def step_impl(context):
    context.user["name"] = "jane doe"

@when("i update the user with id 123 with email 'janedoe@example.com'")
def step_impl(context):
    context.user["email"] = "janedoe@example.com"

@then("the user with id 123 has name 'jane doe'")
def step_impl(context):
    assert context.user["name"] == "jane doe"

@then("the user with id 123 has email 'janedoe@example.com'")
def step_impl(context):
    assert context.user["email"] == "janedoe@example.com"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can update a user given a user with id 123 and the user has name "john doe" and the user has email "[johndoe@example.com](mailto:johndoe@example.com)" when i update the user with id 123 with name "jane doe" and i update the user with id 123 with email "[janedoe@example.com](mailto:janedoe@example.com)" then the user with id 123 has name "jane doe" and the user with id 123 has email "[janedoe@example.com](mailto:janedoe@example.com)" ```



```python from behave import given, when, then

@given("i have a user with id 123 and the user has name 'john doe' and the user has email 'johndoe@example.com'")
def step_impl(context):
    context.user = {"id": 123, "name": "john doe", "email": "johndoe@example.com"}

@when("i update the user with id 123 with name 'jane doe'")
def step_impl(context):
    context.user["name"] = "jane doe"

@when("i update the user with id 123 with email 'janedoe@example.com'")
def step_impl(context):
    context.user["email"] = "janedoe@example.com"

@then("the user with id 123 has name 'jane doe'")
def step_impl(context):
    assert context.user["name"] == "jane doe"

@then("the user with id 123 has email 'janedoe@example.com'")
def step_impl(context):
    assert context.user["email"] == "janedoe@example.com"
```

Task: Write a program to find the sum of the digits of a number.
