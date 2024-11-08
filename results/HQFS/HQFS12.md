# HQFS12
## Scenario
```gherkin
scenario: one project with two metrics 
   and two tags 
   and one value 
   given i have a project with name "kalibro" 
   and two metrics with names "coverage" 
   and "duplications" 
   and two tags with names "release" 
   and "production" 
   and a value of 50 for the metric "coverage" 
   when i ask for all the projects 
   then i should get a list with the 
   given project 
   and the 
   given metrics 
   and the 
   given tags 
   and the 
   given value
```


## Python Implementation
```python
from behave import given, when, then

@given("i have a project with name {project_name} and two metrics with names {metric_names} and two tags with names {tag_names} and a value of {value} for the metric {metric_name}")
def step_impl(context, project_name, metric_names, tag_names, value, metric_name):
    context.project = {
        "name": project_name,
        "metrics": [{
            "name": metric_name,
            "value": value
        }],
        "tags": [{
            "name": tag_names
        }]
    }

@when("i ask for all the projects")
def step_impl(context):
    context.projects = [context.project]

@then("i should get a list with the given project and the given metrics and the given tags and the given value")
def step_impl(context):
    assert context.projects[0]["name"] == context.project["name"]
    assert context.projects[0]["metrics"] == context.project["metrics"]
    assert context.projects[0]["tags"] == context.project["tags"]
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: one project with two metrics and two tags and one value given i have a project with name "kalibro" and two metrics with names "coverage" and "duplications" and two tags with names "release" and "production" and a value of 50 for the metric "coverage" when i ask for all the projects then i should get a list with the given project and the given metrics and the given tags and the given value ```



```python from behave import given, when, then

@given("i have a project with name {project_name} and two metrics with names {metric_names} and two tags with names {tag_names} and a value of {value} for the metric {metric_name}")
def step_impl(context, project_name, metric_names, tag_names, value, metric_name):
    context.project = {
        "name": project_name,
        "metrics": [{
            "name": metric_name,
            "value": value
        }],
        "tags": [{
            "name": tag_names
        }]
    }

@when("i ask for all the projects")
def step_impl(context):
    context.projects = [context.project]

@then("i should get a list with the given project and the given metrics and the given tags and the given value")
def step_impl(context):
    assert context.projects[0]["name"] == context.project["name"]
    assert context.projects[0]["metrics"] == context.project["metrics"]
    assert context.projects[0]["tags"] == context.project["tags"]
```

Task: Write a program to find the sum of the digits of a given number.
