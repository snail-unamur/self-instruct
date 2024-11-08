# HQFS238
## Scenario
```gherkin
None
```


## Python Implementation
```python
@given("we have an initialized game with two teams") def step_given_initialized_game(context): # implementation to initialize the game pass @given("team 1 has a score of {score1} points") def step_given_team1_score(context, score1): context.team1_score = int(score1) @given("team 2 has a score of {score2} points") def step_given_team2_score(context, score2): context.team2_score = int(score2) @when("team 1 scores a goal") def step_when_team1_scores(context): context.team1_score += 1 @then("the game is over") def step_then_game_over(context): # implementation to check if the game is over pass @then("winner team is team 1") def step_then_winner_team1(context): # implementation to check if team 1 is the winner pass @then("team 1 is mopper") def step_then_team1_mopper(context): # implementation to check if team 1 is mopper pass @then("team 2 is mopped") def step_then_team2_mopped(context): # implementation to check if team 2 is mopped pass @then("the game is a mopa") def step_then_game_mopa(context): # implementation to check if the game is a mopa pass
```


## Raw Text
For scenario 6, you can use the following step definition: ```python @given("we have an initialized game with two teams") def step_given_initialized_game(context): # implementation to initialize the game pass @given("team 1 has a score of {score1} points") def step_given_team1_score(context, score1): context.team1_score = int(score1) @given("team 2 has a score of {score2} points") def step_given_team2_score(context, score2): context.team2_score = int(score2) @when("team 1 scores a goal") def step_when_team1_scores(context): context.team1_score += 1 @then("the game is over") def step_then_game_over(context): # implementation to check if the game is over pass @then("winner team is team 1") def step_then_winner_team1(context): # implementation to check if team 1 is the winner pass @then("team 1 is mopper") def step_then_team1_mopper(context): # implementation to check if team 1 is mopper pass @then("team 2 is mopped") def step_then_team2_mopped(context): # implementation to check if team 2 is mopped pass @then("the game is a mopa") def step_then_game_mopa(context): # implementation to check if the game is a mopa pass ```



```python @given("we have an initialized game with two teams") def step_given_initialized_game(context): # implementation to initialize the game pass @given("team 1 has a score of {score1} points") def step_given_team1_score(context, score1): context.team1_score = int(score1) @given("team 2 has a score of {score2} points") def step_given_team2_score(context, score2): context.team2_score = int(score2) @when("team 1 scores a goal") def step_when_team1_scores(context): context.team1_score += 1 @then("the game is over") def step_then_game_over(context): assert context.team1_score + context.team2_score >= 100 @then("winner team is team 1") def step_then_winner_team1(context): assert context.team1_score > context.team2_score @then("team 1 is mopper") def step_then_team1_mopper(context): assert context.team1_score >= 80 @then("team 2 is mopped") def step_then_team2_mopped(context): assert context.team2_score < 20 @then("the game is a mopa") def step_then_game_mopa(context): assert context.team1_score >= 80 and context.team2_score < 20 ```
