# HQFS113
## Scenario
```gherkin
scenario: i can find the number of occurrences of a word in a list 
   given a list of words: ["apple", "banana", "apple", "orange", "banana", "banana"] 
   when i search for the word "banana" 
   then i should get the number of occurrences of "banana" which is 3
```


## Python Implementation
```python
from collections import Counter

@given("i have a list of words: {words}")
def step(context, words):
    context.words = words

@when("i search for the word: {word}")
def step(context, word):
    context.word = word
    context.occurrences = Counter(context.words)[context.word]

@then("i should get the number of occurrences of {word} which is {occurrences}")
def step(context, word, occurrences):
    assert context.occurrences == int(occurrences)
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: i can find the number of occurrences of a word in a list given a list of words: ["apple", "banana", "apple", "orange", "banana", "banana"] when i search for the word "banana" then i should get the number of occurrences of "banana" which is 3 ```



```python from collections import Counter

@given("i have a list of words: {words}")
def step(context, words):
    context.words = words

@when("i search for the word: {word}")
def step(context, word):
    context.word = word
    context.occurrences = Counter(context.words)[context.word]

@then("i should get the number of occurrences of {word} which is {occurrences}")
def step(context, word, occurrences):
    assert context.occurrences == int(occurrences)
```

Task: Write a program to find the number of occurrences of a word in a string.
