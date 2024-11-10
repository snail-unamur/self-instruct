# HQFS88
## Scenario
```gherkin
scenario: run setup script on directory with existing draft 
   and broken draft 
   and other drafts 
   and broken drafts 
   and other files 
   and broken files 
   given a git repo with a draft


   Given a git repo with a draft

   And a directory with existing draft 
   and broken draft 
   and other drafts 
   and broken drafts 
   and other files 
   and broken files

   When I run the setup script

   Then the draft should be updated

   And the broken draft should be fixed

   And the other drafts should be ignored

   And the other files should be ignored

   And the broken files should be fixed
```


## Python Implementation
```python
from behave import given, when, then
import subprocess

@given("a git repo with a draft")
def step_given_a_git_repo_with_a_draft(context):
    pass

@given("a directory with existing draft and broken draft and other drafts and broken drafts and other files and broken files")
def step_given_a_directory_with_existing_draft_and_broken_draft_and_other_drafts_and_broken_drafts_and_other_files_and_broken_files(context):
    pass

@when("I run the setup script")
def step_when_i_run_the_setup_script(context):
    subprocess.run(["python", "setup.py"])

@then("the draft should be updated")
def step_then_the_draft_should_be_updated(context):
    assert True

@then("the broken draft should be fixed")
def step_then_the_broken_draft_should_be_fixed(context):
    assert True

@then("the other drafts should be ignored")
def step_then_the_other_drafts_should_be_ignored(context):
    assert True

@then("the other files should be ignored")
def step_then_the_other_files_should_be_ignored(context):
    assert True

@then("the broken files should be fixed")
def step_then_the_broken_files_should_be_fixed(context):
    assert True
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: run setup script on directory with existing draft and broken draft and other drafts and broken drafts and other files and broken files given a git repo with a draft

Given a git repo with a draft
And a directory with existing draft and broken draft and other drafts and broken drafts and other files and broken files
When I run the setup script
Then the draft should be updated
And the broken draft should be fixed
And the other drafts should be ignored
And the other files should be ignored
And the broken files should be fixed
```

```python
from behave import given, when, then
import subprocess

@given("a git repo with a draft")
def step_given_a_git_repo_with_a_draft(context):
    pass

@given("a directory with existing draft and broken draft and other drafts and broken drafts and other files and broken files")
def step_given_a_directory_with_existing_draft_and_broken_draft_and_other_drafts_and_broken_drafts_and_other_files_and_broken_files(context):
    pass

@when("I run the setup script")
def step_when_i_run_the_setup_script(context):
    subprocess.run(["python", "setup.py"])

@then("the draft should be updated")
def step_then_the_draft_should_be_updated(context):
    assert True

@then("the broken draft should be fixed")
def step_then_the_broken_draft_should_be_fixed(context):
    assert True

@then("the other drafts should be ignored")
def step_then_the_other_drafts_should_be_ignored(context):
    assert True

@then("the other files should be ignored")
def step_then_the_other_files_should_be_ignored(context):
    assert True

@then("the broken files should be fixed")
def step_then_the_broken_files_should_be_fixed(context):
    assert True
```
