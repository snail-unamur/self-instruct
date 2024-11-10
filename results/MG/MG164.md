# MQFS164
## Scenario
```gherkin
scenario: testing the stopwatch 
   given a stopwatch 
   when the user starts the stopwatch 
   then the stopwatch should start counting 
   when the user stops the stopwatch 
   then the stopwatch should stop counting 
   when the user resets the stopwatch 
   then the stopwatch should reset to 0
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the stopwatch given a stopwatch when the user starts the stopwatch then the stopwatch should start counting when the user stops the stopwatch then the stopwatch should stop counting when the user resets the stopwatch then the stopwatch should reset to 0```



from behave import given, when, then
import time

stopwatch = {"start_time": None, "end_time": None, "elapsed_time": 0}

@given("a stopwatch")
def step_given_a_stopwatch(context):
    pass

@when("the user starts the stopwatch")
def step_when_the_user_starts_the_stopwatch(context):
    stopwatch["start_time"] = time.time()

@then("the stopwatch should start counting")
def step_then_the_stopwatch_should_start_counting(context):
    assert stopwatch["start_time"] is not None

@when("the user stops the stopwatch")
def step_when_the_user_stops_the_stopwatch(context):
    stopwatch["end_time"] = time.time()

@then("the stopwatch should stop counting")
def step_then_the_stopwatch_should_stop_counting(context):
    assert stopwatch["end_time"] is not None

@when("the user resets the stopwatch")
def step_when_the_user_resets_the_stopwatch(context):
    stopwatch["elapsed_time"] = 0
    stopwatch["start_time"] = None
    stopwatch["end_time"] = None

@then("the stopwatch should reset to 0")
def step_then_the_stopwatch_should_reset_to_0(context):
    assert stopwatch["elapsed_time"] == 0
    assert stopwatch["start_time"] is None
    assert stopwatch["end_time"] is None
