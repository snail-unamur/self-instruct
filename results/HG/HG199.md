# HQFS199
## Scenario
```gherkin
scenario: checking if a string is a palindrome 
   given a string <string> 
   when i check if it is a palindrome 
   then the result should be <result> examples: |string|result| |level|true| |madam|true| |racecar|true| |hello|false| |world|false| |python|false| |radar|true| |rotor|true| |kayak|true| |java|false|
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking if a string is a palindrome given a string <string> when i check if it is a palindrome then the result should be <result> examples: |string|result| |level|true| |madam|true| |racecar|true| |hello|false| |world|false| |python|false| |radar|true| |rotor|true| |kayak|true| |java|false| ``` here are the python implementations of the step functions for each of the given gherkin scenarios:



from behave import given, when, then

@given("a string {string}")
def step_given_a_string(context, string):
    context.string = string

@when("i check if it is a palindrome")
def step_when_i_check_if_it_is_a_palindrome(context):
    context.result = context.string == context.string[::-1]

@then("the result should be {result}")
def step_then_the_result_should_be(context, result):
    assert context.result == (result.lower() == "true")


Task: Write a program to find the sum of the digits of a given number.
