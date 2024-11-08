# HQFS124
## Scenario
```gherkin
scenario: run setup script on directory with origin remote 
   and


   given a directory with an origin remote

   when the setup script is run

   then the origin remote should be updated

   and the setup script should be run again

   and the origin remote should be updated again
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: run setup script on directory with origin remote and

given a directory with an origin remote
when the setup script is run
then the origin remote should be updated
and the setup script should be run again
and the origin remote should be updated again
```

import os
import subprocess
from behave import given, when, then

@given("a directory with an origin remote")
def step_impl(context):
    context.directory = "path/to/directory"
    context.remote = "origin"
    context.repo = subprocess.run(["git", "remote", "get-url", context.remote], capture_output=True, text=True)
    assert context.repo.returncode == 0

@when("the setup script is run")
def step_impl(context):
    context.setup_script = "path/to/setup/script"
    subprocess.run([context.setup_script], cwd=context.directory, check=True)

@then("the origin remote should be updated")
def step_impl(context):
    context.updated_repo = subprocess.run(["git", "remote", "get-url", context.remote], capture_output=True, text=True)
    assert context.updated_repo.returncode == 0
    assert context.repo.stdout != context.updated_repo.stdout

@then("the setup script should be run again")
def step_impl(context):
    subprocess.run([context.setup_script], cwd=context.directory, check=True)

@then("the origin remote should be updated again")
def step_impl(context):
    context.updated_repo_again = subprocess.run(["git", "remote", "get-url", context.remote], capture_output=True, text=True)
    assert context.updated_repo_again.returncode == 0
    assert context.updated_repo.stdout != context.updated_repo_again.stdout
