# MQFS15
## Scenario
```gherkin
None
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: test rdopkg pkgenv with valid patches_base given a distgit at version 0 and release 0 given a patches branch with 2 patches when i set .spec file patches_base=patches then i run rdopkg pkgenv then command return code is 0 then .spec file tag release is 3%{?dist} then .spec file has 2 patches defined then .spec file contains patches_base then .spec file doesn't contain patches_base_ref then .spec

file contains patches_base_version then .spec file doesn't contain patches_base_version_ref

from behave import given, when, then

@given("a distgit at version 0 and release 0")
def step_given_distgit_at_version_0_and_release_0(context):
    context.distgit_version = "0"
    context.distgit_release = "0"

@given("a patches branch with 2 patches")
def step_given_patches_branch_with_2_patches(context):
    context.patches_count = 2

@when("i set .spec file patches_base=patches")
def step_when_i_set_spec_file_patches_base_patches(context):
    context.patches_base = "patches"

@when("i run rdopkg pkgenv")
def step_when_i_run_rdopkg_pkgenv(context):
    context.run_result = context.run("rdopkg pkgenv")

@then("command return code is 0")
def step_then_command_return_code_is_0(context):
    assert context.run_result.returncode == 0

@then(".spec file tag release is 3%{?dist}")
def step_then_spec_file_tag_release_is_3_dist(context):
    assert "Release: 3%{?dist}" in context.spec_file

@then(".spec file has 2 patches defined")
def step_then_spec_file_has_2_patches_defined(context):
    assert "Patch" in context.spec_file
    assert context.spec_file.count("Patch") == context.patches_count

@then(".spec file contains patches_base")
def step_then_spec_file_contains_patches_base(context):
    assert "patches_base" in context.spec_file

@then(".spec file doesn't contain patches_base_ref")
def step_then_spec_file_doesnt_contain_patches_base_ref(context
