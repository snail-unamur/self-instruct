# MQFS265
## Scenario
```gherkin
scenario: manage package repositories 
   given a package repository "http://example.com/repo" 
   when i add the package repository 
   then the package repository is added 
   and no exception is raised 
   when i remove the package repository 
   then the package repository is removed 
   and no exception is raised
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: manage package repositories given a package repository "http://example.com/repo" when i add the package repository then the package repository is added and no exception is raised when i remove the package repository then the package repository is removed and no exception is raised ```



from behave import given, when, then

@given("a package repository \"{repo}\"")
def step_given_a_package_repository(context, repo):
    context.repo = repo

@when("i add the package repository")
def step_when_i_add_the_package_repository(context):
    context.result = context.repo.add()

@then("the package repository is added and no exception is raised")
def step_then_the_package_repository_is_added_and_no_exception_is_raised(context):
    assert context.result is None

@when("i remove the package repository")
def step_when_i_remove_the_package_repository(context):
    context.result = context.repo.remove()

@then("the package repository is removed and no exception is raised")
def step_then_the_package_repository_is_removed_and_no_exception_is_raised(context):
    assert context.result is None


Task: Write a program to find the sum of the digits of a number.
