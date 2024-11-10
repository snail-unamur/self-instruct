# MQFS245
## Scenario
```gherkin
scenario: testing the web server 
   given a web server 
   when i send a get request to / 
   then i should get a 200 ok response 
   when i send a post request to / with data {"key": "value"} 
   then i should get a 201 created response 
   when i send a put request to /1 with data {"key": "value"} 
   then i should get a 200 ok response 
   when i send a delete request to /1 
   then i should get a 204 no content response 
   when i send a get request to /notfound 
   then i should get a 404 not found response
```


## Python Implementation
```python
from behave import given("a web server", lambda: pass)
when("i send a get request to /", lambda: pass)
then("i should get a 200 ok response", lambda: pass)
when("i send a post request to / with data {key: value}", lambda: pass)
then("i should get a 201 created response", lambda: pass)
when("i send a put request to /1 with data {key: value}", lambda: pass)
then("i should get a 200 ok response", lambda: pass)
when("i send a delete request to /1", lambda: pass)
then("i should get a 204 no content response", lambda: pass)
when("i send a get request to /notfound", lambda: pass)
then("i should get a 404 not found response", lambda: pass)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: testing the web server given a web server when i send a get request to / then i should get a 200 ok response when i send a post request to / with data {"key": "value"} then i should get a 201 created response when i send a put request to /1 with data {"key": "value"} then i should get a 200 ok response when i send a delete request to /1 then i should get a 204 no content response when i send a get request to /notfound then i should get a 404 not found response ```



```python from behave import given("a web server", lambda: pass)
when("i send a get request to /", lambda: pass)
then("i should get a 200 ok response", lambda: pass)
when("i send a post request to / with data {key: value}", lambda: pass)
then("i should get a 201 created response", lambda: pass)
when("i send a put request to /1 with data {key: value}", lambda: pass)
then("i should get a 200 ok response", lambda: pass)
when("i send a delete request to /1", lambda: pass)
then("i should get a 204 no content response", lambda: pass)
when("i send a get request to /notfound", lambda: pass)
then("i should get a 404 not found response", lambda: pass)
```

Task: Write a program to find the sum of the digits of a given number.
