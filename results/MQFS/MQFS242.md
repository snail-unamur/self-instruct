# MQFS242
## Scenario
```gherkin
scenario: testing the create functionality 
   given a client 
   when the client creates a new item 
   then the item should be created 
   and the item should be returned in the response
```


## Python Implementation
```python
from behave import given, when, then

@given("a client")
def step_given_a_client(context):
    context.client = Client()

@when("the client creates a new item")
def step_when_the_client_creates_a_new_item(context):
    context.item = context.client.create_item()

@then("the item should be created and the item should be returned in the response")
def step_then_the_item_should_be_created_and_the_item_should_be_returned_in_the_response(context):
    assert context.item is not None
    assert context.client.response.status_code == 200
    assert context.client.response.json() == context.item
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the create functionality given a client when the client creates a new item then the item should be created and the item should be returned in the response ```



```python from behave import given, when, then

@given("a client")
def step_given_a_client(context):
    context.client = Client()

@when("the client creates a new item")
def step_when_the_client_creates_a_new_item(context):
    context.item = context.client.create_item()

@then("the item should be created and the item should be returned in the response")
def step_then_the_item_should_be_created_and_the_item_should_be_returned_in_the_response(context):
    assert context.item is not None
    assert context.client.response.status_code == 200
    assert context.client.response.json() == context.item
```

Task: Write a program to find the sum of the digits of a number.
