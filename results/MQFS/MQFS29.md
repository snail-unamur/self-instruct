# MQFS29
## Scenario
```gherkin
scenario: testing the function to get the number of occurrences of a character in a string 
   given a string "hello world" 
   and a character "l" 
   when i call the function to get the number of occurrences of a character in a string 
   then i should get 3 as the result
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the function to get the number of occurrences of a character in a string given a string "hello world" and a character "l" when i call the function to get the number of occurrences of a character in a string then i should get 3 as the result ```



from behave import given, when, then

@given("a string {string} and a character {character}")
def step_impl(context, string, character):
    context.string = string
    context.character = character

@when("i call the function to get the number of occurrences of a character in a string")
def step_impl(context):
    context.result = get_occurrences(context.string, context.character)

@then("i should get {int} as the result")
def step_impl(context, int):
    assert int == context.result

def get_occurrences(string, character):
    return string.count(character)
