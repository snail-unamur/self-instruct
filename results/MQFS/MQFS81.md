# MQFS81
## Scenario
```gherkin
scenario: user can register 
   given i am on the registration page 
   when i fill out the form with my name, email, 
   and password 
   and i click the "register" button 
   then i should be registered 
   and i should be taken to the login page
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario : ```gherkin scenario: user can register given i am on the registration page when i fill out the form with my name, email, and password and i click the "register" button then i should be registered and i should be taken to the login page ```



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected\_conditions as EC

def user\_can\_register():
    driver = webdriver.Firefox()
    driver.get("http://www.example.com/register")

    name\_field = driver.find\_element\_by\_name("name")
    email\_field = driver.find\_element\_by\_name("email")
    password\_field = driver.find\_element\_by\_name("password")

    name\_field.send\_keys("John Doe")
    email\_field.send\_keys("johndoe@example.com")
    password\_field.send\_keys("password123")

    register\_button = driver.find\_element\_by\_id("register\_button")
    register\_button.click()

    WebDriverWait(driver, 10).until(EC.url\_changes("http://www.example.com/login"))

    assert driver.current\_url == "http://www.example.com/login"

    driver.quit()

user\_can\_register()
