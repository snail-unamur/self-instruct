# HQFS120
## Scenario
```gherkin
scenario: 
   given a list of numbers, i want to find the average of the numbers 
   given a list of numbers: [1, 2, 3, 4, 5] 
   when i find the average of the numbers 
   then the average should be 3.0
```


## Python Implementation
```python
from behave import given, when, then import requests @given("i prepare environment for tests run") def step_given(context): pass @when("i register an employee with name {name} and job {job}") def step_when(context, name, job): context.response = requests.post( "http://localhost:8000/api/employees/", json={"name": name, "job": job}, headers={"authorization": "bearer <token>"} ) @then("i verify that status code is {status_code}") def step_then(context, status_code): assert context.response.status_code == int(status_code) @then("i verify that response contains {name} as {attribute} attribute") def step_then(context, name, attribute): assert name in context.response.json()[attribute]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, i want to find the average of the numbers given a list of numbers: [1, 2, 3, 4, 5] when i find the average of the numbers then the average should be 3.0 ``` for each task, you should provide a python file with the necessary step definitions for the given scenario. the step definitions should use the behave bdd testing framework. here is an example of how the python file for the first scenario might look like: ```python from behave import given, when, then import requests @given("i prepare environment for tests run") def step_given(context): pass @when("i register an employee with name {name} and job {job}") def step_when(context, name, job): context.response = requests.post( "http://localhost:8000/api/employees/", json={"name": name, "job": job}, headers={"authorization": "bearer <token>"} ) @then("i verify that status code is {status_code}") def step_then(context, status_code): assert context.response.status_code == int(status_code) @then("i verify that response contains {name} as {attribute} attribute") def step_then(context, name, attribute): assert name in context.response.json()[attribute] ``` note that the implementation of the step functions may vary depending on the specifics of the system under test. the provided examples are meant to serve as a starting point for the implementation.



```python from behave import given, when, then @given("a list of numbers") def step_given(context): context.numbers = [1, 2, 3, 4, 5] @when("i find the average of the numbers") def step_when(context): context.average = sum(context.numbers) / len(context.numbers) @then("the average should be {avg:.1f}") def step_then(context, avg): assert round(context.average, 1) == round(float(avg), 1) ```
