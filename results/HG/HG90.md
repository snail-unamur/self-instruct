# HQFS90
## Scenario
```gherkin
scenario: testing the api endpoint for adding a new product 
   given i have a rest api endpoint for adding a new product 
   when i send a post request with the following payload: |name|price|description| |new product|10.00|this is a new product| 
   then i should receive a status code of 201 
   and i should receive a response with the following format: |id|name|price|description| |1|new product|10.00|this is a new product|
```


## Python Implementation
```python
from behave import given, when, then
import requests
import json

@given("i have a rest api endpoint for adding a new product")
def step():
    pass

@when("i send a post request with the following payload:")
def step(context):
    payload = json.loads(context.text)
    response = requests.post("http://localhost:8000/api/products", data=json.dumps(payload), headers={"Content-Type": "application/json"})
    context.response = response

@then("i should receive a status code of 201")
def step(context):
    assert context.response.status_code == 201

@then("i should receive a response with the following format:")
def step(context):
    response_json = context.response.json()
    assert response_json.get("id") is not None
    assert response_json.get("name") == "new product"
    assert response_json.get("price") == 10.00
    assert response_json.get("description") == "this is a new product"
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the api endpoint for adding a new product given i have a rest api endpoint for adding a new product when i send a post request with the following payload: |name|price|description| |new product|10.00|this is a new product| then i should receive a status code of 201 and i should receive a response with the following format: |id|name|price|description| |1|new product|10.00|this is a new product| ```



```python from behave import given, when, then
import requests
import json

@given("i have a rest api endpoint for adding a new product")
def step():
    pass

@when("i send a post request with the following payload:")
def step(context):
    payload = json.loads(context.text)
    response = requests.post("http://localhost:8000/api/products", data=json.dumps(payload), headers={"Content-Type": "application/json"})
    context.response = response

@then("i should receive a status code of 201")
def step(context):
    assert context.response.status_code == 201

@then("i should receive a response with the following format:")
def step(context):
    response_json = context.response.json()
    assert response_json.get("id") is not None
    assert response_json.get("name") == "new product"
    assert response_json.get("price") == 10.00
    assert response_json.get("description") == "this is a new product"
```
