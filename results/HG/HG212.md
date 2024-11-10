# HQFS212
## Scenario
```gherkin
scenario: check if the button is disabled 
   given i open the site "/" 
   and the button "#testbutton" is enabled 
   when i press "a" 
   then i expect that element "#testkeyresponse" contains the text "65" 
   and the button "#testbutton" is disabled 
   and 
   when i press "a" 
   then i expect that element "#testkeyresponse" contains the text "65" 
   and the button "#testbutton" is enabled 
   and 
   when i press "a" 
   then i expect that element "#testkeyresponse" contains the text "65" 
   and the button "#testbutton" is disabled
```


## Python Implementation
```python
from behave import given, when, then @given("i open the site \"/\" and the button #{button_id} is enabled") def step_impl(context, button_id): # code to open the site and check if the button is enabled pass @when("i press \"a\"") def step_impl(context): # code to press the "a" key pass @then("i expect that element #{element_id} contains the text \"65\"") def step_impl(context, element_id): # code to check if the element contains the text "65" pass @then("the button #{button_id} is disabled") def step_impl(context, button_id): # code to check if the button is disabled pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: check if the button is disabled given i open the site "/" and the button "#testbutton" is enabled when i press "a" then i expect that element "#testkeyresponse" contains the text "65" and the button "#testbutton" is disabled and when i press "a" then i expect that element "#testkeyresponse" contains the text "65" and the button "#testbutton" is enabled and when i press "a" then i expect that element "#testkeyresponse" contains the text "65" and the button "#testbutton" is disabled ``` ```python from behave import given, when, then @given("i open the site \"/\" and the button #{button_id} is enabled") def step_impl(context, button_id): # code to open the site and check if the button is enabled pass @when("i press \"a\"") def step_impl(context): # code to press the "a" key pass @then("i expect that element #{element_id} contains the text \"65\"") def step_impl(context, element_id): # code to check if the element contains the text "65" pass @then("the button #{button_id} is disabled") def step_impl(context, button_id): # code to check if the button is disabled pass ```

Task: Write a program to find the sum of the digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number using recursion.
