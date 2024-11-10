# HQFS194
## Scenario
```gherkin
scenario: a player can see their hand 
   given a player 
   when they choose to look at their hand 
   then they can see their hand
```


## Python Implementation
```python
from behave import given, when, then

@given("a player")
def step_given_a_player(context):
    context.player = Player()

@when("they choose to look at their hand")
def step_when_they_choose_to_look_at_their_hand(context):
    context.player.look_at_hand()

@then("they can see their hand")
def step_then_they_can_see_their_hand(context):
    assert context.player.can_see_hand
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a player can see their hand given a player when they choose to look at their hand then they can see their hand ```



```python from behave import given, when, then

@given("a player")
def step_given_a_player(context):
    context.player = Player()

@when("they choose to look at their hand")
def step_when_they_choose_to_look_at_their_hand(context):
    context.player.look_at_hand()

@then("they can see their hand")
def step_then_they_can_see_their_hand(context):
    assert context.player.can_see_hand
```

Task: Write a program to find the sum of the digits of a number.
