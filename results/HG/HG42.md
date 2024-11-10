# HQFS42
## Scenario
```gherkin
scenario: manage existing namespaces creation 
   given namespace "creation" exists 
   when i create a namespace "creation" 
   then an objectalreadyexistsexception is raised
```


## Python Implementation
```python
from behave import given, when, then @given("namespace 'creation' exists") def step_given_namespace_creation_exists(context): # code to create the namespace "creation" @when("i create a namespace 'creation'") def step_when_i_create_a_namespace_creation(context): # code to create the namespace "creation" @then("an objectalreadyexistsexception is raised") def step_then_an_object_already_exists_exception_is_raised(context): try: # code to create the namespace "creation" assert false, "an objectalreadyexistsexception should have been raised" except exception as e: assert isinstance(e, objectalreadyexistsexception)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: manage existing namespaces creation given namespace "creation" exists when i create a namespace "creation" then an objectalreadyexistsexception is raised ``` ```python from behave import given, when, then @given("namespace 'creation' exists") def step_given_namespace_creation_exists(context): # code to create the namespace "creation" @when("i create a namespace 'creation'") def step_when_i_create_a_namespace_creation(context): # code to create the namespace "creation" @then("an objectalreadyexistsexception is raised") def step_then_an_object_already_exists_exception_is_raised(context): try: # code to create the namespace "creation" assert false, "an objectalreadyexistsexception should have been raised" except exception as e: assert isinstance(e, objectalreadyexistsexception) ```



```python from behave import given, when, then from exceptions import ObjectAlreadyExistsException @given("namespace 'creation' exists") def step_given_namespace_creation_exists(context): # code to create the namespace "creation" @when("i create a namespace 'creation'") def step_when_i_create_a_namespace_creation(context): # code to create the namespace "creation" @then("an objectalreadyexistsexception is raised") def step_then_an_object_already_exists_exception_is_raised(context): try: # code to create the namespace "creation" assert False, "an objectalreadyexistsexception should have been raised" except ObjectAlreadyExistsException: pass ```

Task: Write a program to find the sum of the digits of a given number.
