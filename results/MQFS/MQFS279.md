# MQFS279
## Scenario
```gherkin
scenario: 
   given a user with a name, age, 
   and email 
   when the user is created 
   then the user is stored in the database with the 
   given name, age, 
   and email
```


## Python Implementation
```python
from behave import given, when, then
from your_project.models import User

@given("a user with a name, age, and email")
def step_impl(context):
    context.name = "John Doe"
    context.age = 30
    context.email = "johndoe@example.com"

@when("the user is created")
def step_impl(context):
    User.objects.create(name=context.name, age=context.age, email=context.email)

@then("the user is stored in the database with the given name, age, and email")
def step_impl(context):
    user = User.objects.get(name=context.name, age=context.age, email=context.email)
    assert user.name == context.name
    assert user.age == context.age
    assert user.email == context.email
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a user with a name, age, and email when the user is created then the user is stored in the database with the given name, age, and email ```



```python from behave import given, when, then
from your_project.models import User

@given("a user with a name, age, and email")
def step_impl(context):
    context.name = "John Doe"
    context.age = 30
    context.email = "johndoe@example.com"

@when("the user is created")
def step_impl(context):
    User.objects.create(name=context.name, age=context.age, email=context.email)

@then("the user is stored in the database with the given name, age, and email")
def step_impl(context):
    user = User.objects.get(name=context.name, age=context.age, email=context.email)
    assert user.name == context.name
    assert user.age == context.age
    assert user.email == context.email
```

Task: Write a program to find the sum of the digits of a given number.
