# MQFS154
## Scenario
```gherkin
scenario: a user can edit their account details 
   given i am logged in as a user 
   when i click on the edit account button 
   then i should be taken to the edit account page 
   and i should see a form to edit my details 
   and i should see a button to submit the form 
   when i fill in the form with valid details 
   and i click on the submit button 
   then i should be taken back to the login page 
   and i should see a message saying that my account details have been updated
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: a user can edit their account details given i am logged in as a user when i click on the edit account button then i should be taken to the edit account page and i should see a form to edit my details and i should see a button to submit the form when i fill in the form with valid details and i click on the submit button then i should be taken back to the login page and i should see a message saying that my account details have been updated ``` note: * the step functions should be implemented using the behave bdd testing framework * the step functions should use the selenium webdriver library to interact with the web application * the step functions should use the requests library to interact with the web application * the step functions should use the json library to interact with json data * the step functions should use the time library to add delays between actions * the step functions should use the random library to generate random values * the step functions should use the re library to perform regular expression matching * the step functions should use the unittest library to perform assertions * the step functions should use the urllib library to encode url parameters * the step functions should use the os library to interact with the operating system * the step functions should use the sys library to interact with the system * the step functions should use the datetime library to interact with dates and times * the step functions should use the math library to perform mathematical operations * the step functions should use the collections library to interact with collections * the step functions should use the string library to manipulate strings * the step functions should use the platform library to interact with the platform * the step functions should use the logging library to log



from behave import given, when, then
import time
import random
import re
import unittest
import urllib
import os
import sys
import datetime
import math
import collections
import string
import platform
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('i am logged in as a user')
def step_given_i_am_logged_in_as_a_user(context):
    context.driver = webdriver.Firefox()
    context.driver.get('https://www.example.com/login')
    time.sleep(random.uniform(1, 2))
    username_field = context.driver.find_element_by_name('username')
    password_field = context.driver.find_element_by_name('password')
    username_field.send_keys('testuser')
    password_field.send_keys('testpassword')
    password_field.send_keys(Keys.RETURN)
    time.sleep(random.uniform(1, 2))

@when('i click on the edit account button')
def step_when_i_click_on_the_edit_account_button(context):
    context.driver.find_element_by_id('edit-account-button').click()
    time.sleep(random.uniform(1, 2))

@then('i should be taken to the edit account page')
def step_then_i_should_be_taken_to_the_edit_account_page(context):
    assert context.driver.current_url == 'https://www.example.com/edit-account'

@then('i should see a form to edit my details')
def step_then_i_should_see_a_form_to_edit_my_details(context):
    assert context.driver.find_element_by_id('edit-account-form')

@then('i should see a button to submit the
