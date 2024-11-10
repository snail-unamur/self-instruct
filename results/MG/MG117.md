# MQFS117
## Scenario
```gherkin
scenario: a user can add a new repository to a project 
   given a user is logged in 
   and the user has access to a project 
   when the user navigates to the project details page 
   and clicks the "add repository" button 
   then the user should see a form to add a new repository including fields for the repository name, scm type, 
   and repository address 
   and 
   when the user fills in the form 
   and clicks the "add" button 
   then the new repository should be added to the project 
   and the user should be redirected to the project details page with the updated list of repositories
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can add a new repository to a project given a user is logged in and the user has access to a project when the user navigates to the project details page and clicks the "add repository" button then the user should see a form to add a new repository including fields for the repository name, scm type, and repository address and when the user fills in the form and clicks the "add" button then the new repository should be added to the project and the user should be redirected to the project details page with the updated list of repositories ```



```python from behave import given, when, then

@given("a user is logged in and the user has access to a project")
def step_impl(context):
    context.user = User()
    context.project = Project()
    context.project.repositories = []
    context.project.add_repository(Repository())
    context.project.add_repository(Repository())
    context.project.add_repository(Repository())
    context.project.save()
    context.response = context.app.get(f"/projects/{context.project.id}")
    context.login_page = LoginPage(context.response)
    context.login_page.login(context.user.username, context.user.password)

@when("the user navigates to the project details page and clicks the 'add repository' button")
def step_impl(context):
    context.project_page = ProjectPage(context.response)
    context.project_page.click_add_repository()

@then("the user should see a form to add a new repository including fields for the repository name, scm type, and repository address")
def step_impl(context):
    context.add_repository_page = AddRepositoryPage(context.response)
    assert context.add_repository_page.is_displayed()

@when("the user fills in the form and clicks the 'add' button")
def step_impl(context):
    context.repository = Repository()
    context.repository.name = "new_repository"
    context.repository.scm_type = "git"
    context.repository.address = "https://github.com/new_repository.git"
    context.add_repository_page.fill_form(context.repository)
    context.add_repository_page.click_add()

@then("the new repository should be added to the project and the user should be redirected to the project details page with the updated list of repositories")
def step_impl(context):
    context.project_page = ProjectPage(context.response)
    assert len(context.project_page.repositories) == 4
    assert context.project_page.repository_names[
