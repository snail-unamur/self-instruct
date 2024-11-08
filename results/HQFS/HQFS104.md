# HQFS104
## Scenario
```gherkin
scenario: addition 
   given i take the calculator 
   when i add 5 
   and 3 
   then the result should be 8
```


## Python Implementation
```python
from behave import given, when, then @given("i take the calculator") def step_given_i_take_the_calculator(context): # initialize calculator pass @when("i potentiate {base} and {potence}") def step_when_i_potentiate(context, base, potence): # perform potentiation context.result = base ** potence @then("the result should be {result}") def step_then_the_result_should_be(context, result): # check result assert context.result == int(result)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: addition given i take the calculator when i add 5 and 3 then the result should be 8 ``` for all of the above tasks, you can use the following template for the step functions: ```python from behave import given, when, then @given("i take the calculator") def step_given_i_take_the_calculator(context): # initialize calculator pass @when("i potentiate {base} and {potence}") def step_when_i_potentiate(context, base, potence): # perform potentiation context.result = base ** potence @then("the result should be {result}") def step_then_the_result_should_be(context, result): # check result assert context.result == int(result) ``` you can modify the step functions according to the scenario and the actions that need to be performed.



```python from behave import given, when, then @given("i take the calculator") def step_given_i_take_the_calculator(context): # initialize calculator pass @when("i add {num1} and {num2}") def step_when_i_add(context, num1, num2): # perform addition context.result = int(num1) + int(num2) @then("the result should be {result}") def step_then_the_result_should_be(context, result): # check result assert context.result == int(result) ```
