# HQFS4
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a dealer can always play given a dealer when round starts then the dealer chooses a play and the player chooses a play then the dealer wins if the dealer's play is higher then the player wins if the player's play is higher then it is a tie if the dealer's and player's plays are equal and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer then the player wins and the player has a higher card than the dealer



from behave import given, when, then

@given("a dealer")
def step_given_a_dealer(context):
    context.dealer = Dealer()

@given("when round starts")
def step_given_when_round_starts(context):
    context.round = Round()

@when("the dealer chooses a play")
def step_when_the_dealer_chooses_a_play(context):
    context.dealer_play = context.dealer.choose_play()

@when("the player chooses a play")
def step_when_the_player_chooses_a_play(context):
    context.player_play = context.player.choose_play()

@then("the dealer wins if the dealer's play is higher")
def step_then_the_dealer_wins_if_the_dealers_play_is_higher(context):
    if context.dealer_play > context.player_play:
        context.winner = context.dealer

@then("the player wins if the player's play is higher")
def step_then_the_player_wins_if_the_players_play_is_higher(context):
    if context.player_play > context.dealer_play:
        context.winner = context.player

@then("it is a tie if the dealer's and player's plays are equal")
def step_then_it_is_a_tie_if_the_dealers_and_players_plays_are_equal(context):
    if context.dealer_play == context.player_play:
        context.winner = None

@then("the player wins if the player's play is higher and the player has a higher card than the dealer")
def step_then_the_player_wins_if_the_players_play_is_higher_and_the_player_has_a_higher_card_than_the_dealer(context):
    if context.player_play > context.dealer_play and context.player_card > context
