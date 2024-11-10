# HQFS111
## Scenario
```gherkin
None
```


## Python Implementation
```python
@given("br-init is run with existent") def step_given_br_init_run_existent(context): context.br_init_run_existent = true @when("the application executes") def step_when_application_executes(context): # implementation to run the application pass @then("an exception is raised") def step_then_exception_raised(context): assert context.br_init_run_existent == true
```


## Raw Text
For scenario 5, you can use the following step definition: ```python @given("br-init is run with existent") def step_given_br_init_run_existent(context): context.br_init_run_existent = true @when("the application executes") def step_when_application_executes(context): # implementation to run the application pass @then("an exception is raised") def step_then_exception_raised(context): assert context.br_init_run_existent == true ```

Number: 100000

1 + 0 + 0 + 0 + 0 = 1

Task: Write a program to find the sum of the digits of a given number.
