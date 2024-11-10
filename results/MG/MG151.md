# MQFS151
## Scenario
```gherkin
scenario: testing the function of the button 
   given a button is pressed 
   when the button is released 
   and pressed again 
   and released 
   then the button should be in the released state 
   given a button 
   when the button is pressed 
   then the button should be in the pressed state 
   when the button is released 
   then the button should be in the released state 
   when the button is pressed 
   then the button should be in the pressed state 
   when the button is released 
   then the button should be in the released state
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the function of the button given a button is pressed when the button is released and pressed again and released then the button should be in the released state given a button when the button is pressed then the button should be in the pressed state when the button is released then the button should be in the released state when the button is pressed then the button should be in the pressed state when the button is released then the button should be in the released state ```



```python from behave import given, when, then

@given("a button is pressed")
def step_given_a_button_is_pressed(context):
    context.button.press()
    assert context.button.is_pressed

@when("the button is released")
def step_when_the_button_is_released(context):
    context.button.release()

@then("the button should be in the released state")
def step_then_the_button_should_be_in_the_released_state(context):
    assert not context.button.is_pressed

@given("a button when the button is pressed")
def step_given_a_button_when_the_button_is_pressed(context):
    context.button.press()
    assert context.button.is_pressed

@when("the button is released")
def step_when_the_button_is_released_1(context):
    context.button.release()

@then("the button should be in the pressed state")
def step_then_the_button_should_be_in_the_pressed_state(context):
    assert context.button.is_pressed

@given("a button when the button is released")
def step_given_a_button_when_the_button_is_released(context):
    context.button.release()
    assert not context.button.is_pressed

@when("the button is pressed")
def step_when_the_button_is_pressed_1(context):
    context.button.press()

@then("the button should be in the pressed state")
def step_then_the_button_should_be_in_the_pressed_state_1(context):
    assert context.button.is_pressed

@given("a button when the button is pressed")
def step_given_a_button_when_the_button_is_pressed_1(context):
    context.button.press()
    assert context.button.is_pressed

@when("the button is released")
def step_when_the_button_released(context):
    context.
