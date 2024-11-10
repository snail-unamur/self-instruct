# HQFS92
## Scenario
```gherkin
scenario: the player with the highest score wins 
   given multiple players have played 
   when the game ends 
   then the player with the highest score wins
```


## Python Implementation
```python
from behave import given, when, then

@given("multiple players have played")
def step_impl(context):
    context.players = [
        {"name": "player1", "score": 10},
        {"name": "player2", "score": 20},
        {"name": "player3", "score": 30},
    ]

@when("the game ends")
def step_impl(context):
    context.winner = max(context.players, key=lambda x: x["score"])

@then("the player with the highest score wins")
def step_impl(context):
    assert context.winner == {"name": "player3", "score": 30}
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: the player with the highest score wins given multiple players have played when the game ends then the player with the highest score wins ```



```python from behave import given, when, then

@given("multiple players have played")
def step_impl(context):
    context.players = [
        {"name": "player1", "score": 10},
        {"name": "player2", "score": 20},
        {"name": "player3", "score": 30},
    ]

@when("the game ends")
def step_impl(context):
    context.winner = max(context.players, key=lambda x: x["score"])

@then("the player with the highest score wins")
def step_impl(context):
    assert context.winner == {"name": "player3", "score": 30}
```

Task: Write a program to find the second largest number in a list.
