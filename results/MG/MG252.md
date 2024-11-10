# MQFS252
## Scenario
```gherkin
scenario: verify that the correct number of files are in the directory 
   given a directory containing 5 files 
   when i check the number of files in the directory 
   then the number of files in the directory is 5
```


## Python Implementation
```python
from behave import given, when, then @given("user is on the page containing incrorrect words and uder clicked an incorrect word option 'none of the above'") def step_given1(context): pass @when("user clicks on the option") def step_when1(context): pass @then("input field appears with greek aplhabet below") def step_then1(context): pass @then("user can type a word clicking on greek alphabet letters") def step_then2(context): pass @then("when lenght of the input >2 save button is enabled") def step_then3(context): pass @then("user clicks on save button") def step_then4(context): pass @then("and right pane is emptied") def step_then5(context): pass @given("a distgit at version 1.1.1") def step_given2(context): pass @then(".spec file doesn't contain patches_base") def step_then6(context): pass @then(".spec file doesn't contain patches_ignore") def step_then7(context): pass @when("i run rdopkg set-magic-comment patches_ignore ''") def step_when2(context): pass @then(".spec file doesn't contain patches_ignore") def step_then8(context): pass
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: verify that the correct number of files are in the directory given a directory containing 5 files when i check the number of files in the directory then the number of files in the directory is 5 ``` ```python from behave import given, when, then @given("user is on the page containing incrorrect words and uder clicked an incorrect word option 'none of the above'") def step_given1(context): pass @when("user clicks on the option") def step_when1(context): pass @then("input field appears with greek aplhabet below") def step_then1(context): pass @then("user can type a word clicking on greek alphabet letters") def step_then2(context): pass @then("when lenght of the input >2 save button is enabled") def step_then3(context): pass @then("user clicks on save button") def step_then4(context): pass @then("and right pane is emptied") def step_then5(context): pass @given("a distgit at version 1.1.1") def step_given2(context): pass @then(".spec file doesn't contain patches_base") def step_then6(context): pass @then(".spec file doesn't contain patches_ignore") def step_then7(context): pass @when("i run rdopkg set-magic-comment patches_ignore ''") def step_when2(context): pass @then(".spec file doesn't contain patches_ignore") def step_then8(context): pass

```

```python from behave import given, when, then @given("a directory containing 5 files") def step_given(context): pass @when("i check the number of files in the directory") def step_when(context): pass @then("the number of files in the directory is 5") def step_then(context): assert 5 == len(context.files) ```

Task: Write a program to find the sum of the digits of a number.
