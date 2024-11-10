# MQFS150
## Scenario
```gherkin
scenario: testing a simple web server 
   given i have a web server running on port 8080 
   when i send a get request to "/" 
   then i should get a response with status code 200 
   and the response body should be "hello, world!"
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing a simple web server given i have a web server running on port 8080 when i send a get request to "/" then i should get a response with status code 200 and the response body should be "hello, world!" ```



from behave import given, when, then
import requests

@given("i have a web server running on port 8080")
def step_given_web_server_running(context):
    context.server_url = "http://localhost:8080"

@when("i send a get request to \"/\"")
def step_when_send_get_request(context):
    context.response = requests.get(context.server_url)

@then("i should get a response with status code 200")
def step_then_status_code_200(context):
    assert context.response.status_code == 200

@then("the response body should be \"hello, world!\"")
def step_then_response_body(context):
    assert context.response.text == "hello, world!"

Task: Write a program to find the sum of the digits of a given number.
