# MQFS10
## Scenario
```gherkin
scenario: checking the validity of a credit card number 
   given i have a credit card number "4532015112830366" 
   when i check the validity of the credit card number 
   then the credit card number is valid
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: checking the validity of a credit card number given i have a credit card number "4532015112830366" when i check the validity of the credit card number then the credit card number is valid ```



from behave import given, when, then
import re

@given("i have a credit card number {card_number}")
def step(context, card_number):
    context.card_number = card_number

@when("i check the validity of the credit card number")
def step(context):
    context.valid = validate_credit_card(context.card_number)

@then("the credit card number is valid")
def step(context):
    assert context.valid, "The card number is not valid"

def validate_credit_card(number):
    if not number or not re.match(r"^\d{13,16}$", number):
        return False
    odd_sum, even_sum = 0, 0
    for i, digit in enumerate(number[::-1]):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            doubled = int(digit) * 2
            odd_sum += doubled // 10 + doubled % 10
    return odd_sum + even_sum % 10 == 0

Task: Write a program to find the sum of the digits of a given number.
