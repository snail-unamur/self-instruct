# HQFS281
## Scenario
```gherkin
scenario: a user can delete their order 
   given i am a client 
   and i have made orders 
   when i visit the url for a specific order 
   and i click the delete button 
   then i should no longer see that order in my order history
```


## Python Implementation
```python
from behave import given, when, then

@given("i am a client and i have made orders")
def step_given(context):
    context.client = Client()
    context.orders = [Order(id=i) for i in range(5)]
    context.client.orders = context.orders

@when("i visit the url for a specific order")
def step_when(context):
    context.order = context.orders[2]
    context.response = context.client.get(f"/orders/{context.order.id}")

@when("i click the delete button")
def step_when_2(context):
    context.response = context.client.delete(f"/orders/{context.order.id}")

@then("i should no longer see that order in my order history")
def step_then(context):
    context.response = context.client.get("/orders")
    assert context.order not in context.response.json()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can delete their order given i am a client and i have made orders when i visit the url for a specific order and i click the delete button then i should no longer see that order in my order history ```



```python from behave import given, when, then

@given("i am a client and i have made orders")
def step_given(context):
    context.client = Client()
    context.orders = [Order(id=i) for i in range(5)]
    context.client.orders = context.orders

@when("i visit the url for a specific order")
def step_when(context):
    context.order = context.orders[2]
    context.response = context.client.get(f"/orders/{context.order.id}")

@when("i click the delete button")
def step_when_2(context):
    context.response = context.client.delete(f"/orders/{context.order.id}")

@then("i should no longer see that order in my order history")
def step_then(context):
    context.response = context.client.get("/orders")
    assert context.order not in context.response.json()
```

Task: Write a program to find the sum of the digits of a number.
