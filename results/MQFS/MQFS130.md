# MQFS130
## Scenario
```gherkin
scenario: i can find house prices by date 
   given a house price search engine with july 2016 data 
   and i am on the search page 
   when i enter the start date of 14 july 
   and i enter an end date of 21 july 
   and i click the search button 
   then all house prices should be for sales between 14 july 
   and 21 july
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can find house prices by date given a house price search engine with july 2016 data and i am on the search page when i enter the start date of 14 july and i enter an end date of 21 july and i click the search button then all house prices should be for sales between 14 july and 21 july ``` here is the python implementation of the step functions for the given gherkin scenario using the behave bdd testing framework: from behave import given, when, then @given("a house price search engine with july 2016 data") def step\_given\_a\_house\_price\_search\_engine\_with\_july\_2016\_data(context): pass @given("i am on the search page") def step\_given\_i\_am\_on\_the\_search\_page(context): pass @when("i enter the start date of 14 july") def step\_when\_i\_enter\_the\_start\_date\_of\_14\_july(context): pass @when("i enter an end date of 21 july") def step\_when\_i\_enter\_an\_end\_date\_of\_21\_july(context): pass @when("i click the search button") def step\_when\_i\_click\_the\_search\_button(context): pass @then("all house prices should be for sales between 14 july and 21 july") def step\_then\_all\_house\_prices\_should\_be\_for\_sales\_between\_14\_july\_and\_21\_july(context): pass

Task: Write a program to find the sum of the digits of a number.

def sum\_of\_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

Task: Write a program to find the sum of the digits of a number using recursion.
