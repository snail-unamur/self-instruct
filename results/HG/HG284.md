# HQFS284
## Scenario
```gherkin
scenario: user can follow 
   and unfollow another user 
   given the user is logged in 
   and another user exists 
   when the user follows the other user 
   then the user is following the other user 
   and the other user is followed by the user 
   when the user unfollows the other user 
   then the user is no longer following the other user 
   and the other user is no longer followed by the user
```


## Python Implementation
```python
from behave import given, when, then

@given("the user is logged in and another user exists")
def step_impl(context):
    context.user = User("test_user")
    context.other_user = User("other_user")

@when("the user follows the other user")
def step_impl(context):
    context.user.follow(context.other_user)

@then("the user is following the other user and the other user is followed by the user")
def step_impl(context):
    assert context.user.is_following(context.other_user)
    assert context.other_user.is_followed_by(context.user)

@when("the user unfollows the other user")
def step_impl(context):
    context.user.unfollow(context.other_user)

@then("the user is no longer following the other user and the other user is no longer followed by the user")
def step_impl(context):
    assert not context.user.is_following(context.other_user)
    assert not context.other_user.is_followed_by(context.user)

class User:
    def __init__(self, name):
        self.name = name
        self.following = set()
        self.followers = set()

    def follow(self, other):
        self.following.add(other)
        other.followers.add(self)

    def unfollow(self, other):
        self.following.remove(other)
        other.followers.remove(self)

    def is_following(self, other):
        return other in self.following

    def is_followed_by(self, other):
        return self in other.followers
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: user can follow and unfollow another user given the user is logged in and another user exists when the user follows the other user then the user is following the other user and the other user is followed by the user when the user unfollows the other user then the user is no longer following the other user and the other user is no longer followed by the user ```



```python from behave import given, when, then

@given("the user is logged in and another user exists")
def step_impl(context):
    context.user = User("test_user")
    context.other_user = User("other_user")

@when("the user follows the other user")
def step_impl(context):
    context.user.follow(context.other_user)

@then("the user is following the other user and the other user is followed by the user")
def step_impl(context):
    assert context.user.is_following(context.other_user)
    assert context.other_user.is_followed_by(context.user)

@when("the user unfollows the other user")
def step_impl(context):
    context.user.unfollow(context.other_user)

@then("the user is no longer following the other user and the other user is no longer followed by the user")
def step_impl(context):
    assert not context.user.is_following(context.other_user)
    assert not context.other_user.is_followed_by(context.user)

class User:
    def __init__(self, name):
        self.name = name
        self.following = set()
        self.followers = set()

    def follow(self, other):
        self.following.add(other)
        other.followers.add(self)

    def unfollow(self, other):
        self.following.remove(other)
        other.followers.remove(self)

    def is_following(self, other):
        return other in self.following

    def is_followed_by(self, other):
        return self in other.followers
```

Task: Write a program to find the sum of the digits of a number.
