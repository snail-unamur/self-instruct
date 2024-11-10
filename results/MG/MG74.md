# MQFS74
## Scenario
```gherkin
scenario: 
   given a distgit repository at version 1.2.3-4 
   and release 1.2.3-4 
   when i execute the rdopkg command "koji" 
   then the koji process should be triggered 
   and the rpm package should be built 
   and the rpm package should be placed in the koji build



from behave import 
   given, 
   when, 
   then

@
   given("a distgit repository at version {version} 
   and release {release}")
def step_impl(context, version, release):
    context.repository = Repository("distgit", version, release)

@
   when("i execute the rdopkg command 'koji'")
def step_impl(context):
    context.koji = Koji(context.repository)
    context.koji.execute()

@
   then("the koji process should be triggered 
   and the rpm package should be built 
   and the rpm package should be placed in the koji build")
def step_impl(context):
    assert context.koji.triggered
    assert context.koji.built
    assert context.koji.koji_build

class Repository:
    def __init__(self, name, version, release):
        self.name = name
        self.version = version
        self.release = release

class Koji:
    triggered = False
    built = False
    koji_build = None

    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        self.triggered = True
        self.built = True
        self.koji_build = KojiBuild(self.repository)

class KojiBuild:
    def __init__(self, repository):
        self.repository = repository

    def place(self):
        self.repository.built = True
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a distgit repository at version 1.2.3-4 and release 1.2.3-4 when i execute the rdopkg command "koji" then the koji process should be triggered and the rpm package should be built and the rpm package should be placed in the koji build



from behave import given, when, then

@given("a distgit repository at version {version} and release {release}")
def step_impl(context, version, release):
    context.repository = Repository("distgit", version, release)

@when("i execute the rdopkg command 'koji'")
def step_impl(context):
    context.koji = Koji(context.repository)
    context.koji.execute()

@then("the koji process should be triggered and the rpm package should be built and the rpm package should be placed in the koji build")
def step_impl(context):
    assert context.koji.triggered
    assert context.koji.built
    assert context.koji.koji_build

class Repository:
    def __init__(self, name, version, release):
        self.name = name
        self.version = version
        self.release = release

class Koji:
    triggered = False
    built = False
    koji_build = None

    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        self.triggered = True
        self.built = True
        self.koji_build = KojiBuild(self.repository)

class KojiBuild:
    def __init__(self, repository):
        self.repository = repository

    def place(self):
        self.repository.built = True

```

Task: Write a program to find the sum of the digits of a number.
