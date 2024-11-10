# MQFS215
## Scenario
```gherkin
None
```


## Python Implementation
```python
from behave import given, when, then @given('i am a client') def step_given_i_am_a_client(): # implement the step function for the given 'i am a client' @given('order an item for ".25" dollar') def step_given_order_an_item_for_25_dollar(): # implement

the step function for the given 'order an item for ".25" dollar' @when('i pay with a ".50" dollar bill') def step_when_i_pay_with_a_50_dollar_bill(): # implement the step function for the when 'i pay with a ".50" dollar bill' @then('i should receive ".25" dollars in change') def step_then_i_should_receive_25_dollars_in_change(): # implement the step function for the then 'i should receive ".25" dollars in change'
```


## Raw Text
To implement the step functions for the given gherkin scenario, you can use the behave bdd testing framework and python. here is an example of how you can do this: ```python from behave import given, when, then @given('i am a client') def step_given_i_am_a_client(): # implement the step function for the given 'i am a client' @given('order an item for ".25" dollar') def step_given_order_an_item_for_25_dollar(): # implement

the step function for the given 'order an item for ".25" dollar' @when('i pay with a ".50" dollar bill') def step_when_i_pay_with_a_50_dollar_bill(): # implement the step function for the when 'i pay with a ".50" dollar bill' @then('i should receive ".25" dollars in change') def step_then_i_should_receive_25_dollars_in_change(): # implement the step function for the then 'i should receive ".25" dollars in change' ```

```python
from behave import given, when, then

@given('i am a client')
def step_given_i_am_a_client():
    # implement the step function for the given 'i am a client'

@given('order an item for ".25" dollar')
def step_given_order_an_item_for_25_dollar():
    # implement the step function for the given 'order an item for ".25" dollar'

@when('i pay with a ".50" dollar bill')
def step_when_i_pay_with_a_50_dollar_bill():
    # implement the step function for the when 'i pay with a ".50" dollar bill'

@then('i should receive ".25" dollars in change')
def step_then_i_should_receive_25_dollars_in_change():
    # implement the step function for the then 'i should receive ".25" dollars in change'
```
