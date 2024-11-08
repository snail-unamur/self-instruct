# HQFS215
## Scenario
```gherkin
None
```


## Python Implementation
```python
from behave import given, when, then import subprocess @given("we compose 'docker-compose-1.yml'") def step_given_compose_docker_compose_1_yml(context): pass @when("requesting '/network/peers' from 'vp0'") def step_when_requesting_network_peers_from_vp0(context): context.response = subprocess.run( ['docker-compose', '-f', 'docker-compose-1.yml', 'run', '--rm', 'vp0', 'curl', 'http://localhost:5001/network/peers'], capture_output=true, text=true ) @then("i should get a json response with array 'peers' contains '1' elements") def step_then_json_response_with_peers_contains_1_elements(context): assert context.response.returncode == 0 assert 'peers' in context.response.stdout assert len(context.response.stdout.split('peers')[1].strip('[]').split(',')) == 1
```


## Raw Text
Peers list test, single peer issue ```python from behave import given, when, then import subprocess @given("we compose 'docker-compose-1.yml'") def step_given_compose_docker_compose_1_yml(context): pass @when("requesting '/network/peers' from 'vp0'") def step_when_requesting_network_peers_from_vp0(context): context.response = subprocess.run( ['docker-compose', '-f', 'docker-compose-1.yml', 'run', '--rm', 'vp0', 'curl', 'http://localhost:5001/network/peers'], capture_output=true, text=true ) @then("i should get a json response with array 'peers' contains '1' elements") def step_then_json_response_with_peers_contains_1_elements(context): assert context.response.returncode == 0 assert 'peers' in context.response.stdout assert len(context.response.stdout.split('peers')[1].strip('[]').split(',')) == 1 ```



```python
from behave import given, when, then
import subprocess

@given("we compose 'docker-compose-1.yml'")
def step_given_compose_docker_compose_1_yml(context):
    pass

@when("requesting '/network/peers' from 'vp0'")
def step_when_requesting_network_peers_from_vp0(context):
    context.response = subprocess.run(
        ['docker-compose', '-f', 'docker-compose-1.yml', 'run', '--rm', 'vp0', 'curl', 'http://localhost:5001/network/peers'],
        capture_output=True,
        text=True
    )

@then("i should get a json response with array 'peers' contains '1' elements")
def step_then_json_response_with_peers_contains_1_elements(context):
    assert context.response.returncode == 0
    assert 'peers' in context.response.stdout
    assert len(context.response.stdout.split('peers')[1].strip('[]').split(',')) == 1
```
