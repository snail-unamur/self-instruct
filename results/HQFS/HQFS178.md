# HQFS178
## Scenario
```gherkin
scenario: a user can view their order details 
   given i am a registered user 
   when i visit my order history page 
   then i should see a list of my previous orders 
   when i click on one of the orders 
   then i should be redirected to the order details page 
   and i should see the details of that order
```


## Python Implementation
```python
from behave import given, when, then

@given("i am a registered user")
def step_impl(context):
    context.user = User.objects.get(email="test@test.com")
    context.response = context.client.login(username=context.user.email, password="test")

@when("i visit my order history page")
def step_impl(context):
    context.response = context.client.get("/orders/")

@then("i should see a list of my previous orders")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Order 1" in context.response.content.decode("utf-8")
    assert "Order 2" in context.response.content.decode("utf-8")

@when("i click on one of the orders")
def step_impl(context):
    context.response = context.client.get("/orders/1/")

@then("i should be redirected to the order details page and i should see the details of that order")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Order 1 details" in context.response.content.decode("utf-8")
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can view their order details given i am a registered user when i visit my order history page then i should see a list of my previous orders when i click on one of the orders then i should be redirected to the order details page and i should see the details of that order ```



```python from behave import given, when, then

@given("i am a registered user")
def step_impl(context):
    context.user = User.objects.get(email="test@test.com")
    context.response = context.client.login(username=context.user.email, password="test")

@when("i visit my order history page")
def step_impl(context):
    context.response = context.client.get("/orders/")

@then("i should see a list of my previous orders")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Order 1" in context.response.content.decode("utf-8")
    assert "Order 2" in context.response.content.decode("utf-8")

@when("i click on one of the orders")
def step_impl(context):
    context.response = context.client.get("/orders/1/")

@then("i should be redirected to the order details page and i should see the details of that order")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Order 1 details" in context.response.content.decode("utf-8")
```

Task: Write a program to find the sum of the digits of a number.
