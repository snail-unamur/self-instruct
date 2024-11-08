# HQFS127
## Scenario
```gherkin
scenario: 
   given a list of numbers, return the second largest number 
   given a list of numbers: [1, 2, 3, 4, 5] 
   when i ask for the second largest number 
   then the answer should be 4 
   given a list of numbers: [1, 2, 2, 4, 5] 
   when i ask for the second largest number 
   then the answer should be 2 
   given a list of numbers: [1, 2, 1, 4, 5] 
   when i ask for the second largest number 
   then the answer should be 2 
   given a list of numbers: [1, 2] 
   when i ask for the second largest number 
   then the answer should be none 
   given a list of numbers: [1] 
   when i ask for the second largest number 
   then the answer should be none
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: given a list of numbers, return the second largest number given a list of numbers: [1, 2, 3, 4, 5] when i ask for the second largest number then the answer should be 4 given a list of numbers: [1, 2, 2, 4, 5] when i ask for the second largest number then the answer should be 2 given a list of numbers: [1, 2, 1, 4, 5] when i ask for the second largest number then the answer should be 2 given a list of numbers: [1, 2] when i ask for the second largest number then the answer should be none given a list of numbers: [1] when i ask for the second largest number then the answer should be none ```

[1, 2, 2, 4, 5]

2
