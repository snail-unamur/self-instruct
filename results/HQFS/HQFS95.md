# HQFS95
## Scenario
```gherkin
scenario: testing the delete employee functionality 
   given i am on the employee list page 
   when i click on the delete button for an employee 
   then the employee should be deleted from the system
```


## Python Implementation
```python
from behave import given, when, then @given("the ninja has a third level black-belt") def step_given_ninja_has_black_belt(context): context.ninja = ninja() context.ninja.black_belt_level = 3 @when("attacked by chuck norris") def step_when_attacked_by_chuck_norris(context): context.opponent = chucknorris() context.ninja.fight(context.opponent) @then("the ninja should run for his life") def step_then_ninja_should_run(context): assert context.ninja.is_running() @given("a database containing critical data") def step_given_database_with_critical_data(context): context.database = database() context.database.populate_with_critical_data() @when("initiating a backup process") def step_when_initiating_backup_process(context): context.backup = backup() context.backup.backup_database(context.database) @then("the backup should be stored securely in an offsite location") def step_then_backup_should_be_stored_securely(context): assert context.backup.is_stored_securely() @given("you are starting a game of chess") def step_given_starting_chess_game(context): context.board = chessboard()

@when("you move your pawn to e4") def step_when_moving_pawn_to_e4(context): context.board.move_piece("pawn", "e2", "e4")
@then("your opponent should respond with e5") def step_then_opponent_responds_with_e5(context): assert context.board.get_piece("e5") == "pawn"
@given("i am on the employee list page") def step_given_on_employee_list_page(context): context.page = employee_list_page()
@when("i click on the delete button for an employee") def step_when_click_delete_button(context): context.page.click_delete_button()
@then("the employee should be deleted from the system") def step_then_employee_deleted(context): assert context.page.employee_not_found()
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the delete employee functionality given i am on the employee list page when i click on the delete button for an employee then the employee should be deleted from the system ``` ```python from behave import given, when, then @given("the ninja has a third level black-belt") def step_given_ninja_has_black_belt(context): context.ninja = ninja() context.ninja.black_belt_level = 3 @when("attacked by chuck norris") def step_when_attacked_by_chuck_norris(context): context.opponent = chucknorris() context.ninja.fight(context.opponent) @then("the ninja should run for his life") def step_then_ninja_should_run(context): assert context.ninja.is_running() @given("a database containing critical data") def step_given_database_with_critical_data(context): context.database = database() context.database.populate_with_critical_data() @when("initiating a backup process") def step_when_initiating_backup_process(context): context.backup = backup() context.backup.backup_database(context.database) @then("the backup should be stored securely in an offsite location") def step_then_backup_should_be_stored_securely(context): assert context.backup.is_stored_securely() @given("you are starting a game of chess") def step_given_starting_chess_game(context): context.board = chessboard()

@when("you move your pawn to e4") def step_when_moving_pawn_to_e4(context): context.board.move_piece("pawn", "e2", "e4")
@then("your opponent should respond with e5") def step_then_opponent_responds_with_e5(context): assert context.board.get_piece("e5") == "pawn"
@given("i am on the employee list page") def step_given_on_employee_list_page(context): context.page = employee_list_page()
@when("i click on the delete button for an employee") def step_when_click_delete_button(context): context.page.click_delete_button()
@then("the employee should be deleted from the system") def step_then_employee_deleted(context): assert context.page.employee_not_found()
```

```python from behave import given, when, then @given("i am on the employee list page") def step_given_on_employee_list_page(context): context.page = EmployeeListPage() @when("i click on the delete button for an employee") def step_when_click_delete_button(context): context.page.click_delete_button() @then("the employee should be deleted from the system") def step_then_employee_deleted(context): assert context.page.employee_not_found()
```

Task: Write a program to find the sum of the digits of a number.
