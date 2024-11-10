# HQFS225
## Scenario
```gherkin
scenario: booking a flight 
   given a traveler wants to book a flight to a specific destination with a specific departure date 
   and a specific return date 
   and a specific airline 
   when the traveler enters all the required information 
   and confirms the booking 
   then the flight should be booked successfully
```


## Python Implementation
```python
None
```


## Raw Text
Generate a python implementation of the step functions for the following gherkin scenario using the behave bdd testing framework : ```gherkin scenario: booking a flight given a traveler wants to book a flight to a specific destination with a specific departure date and a specific return date and a specific airline when the traveler enters all the required information and confirms the booking then the flight should be booked successfully ```



from behave import given, when, then

@given("a traveler wants to book a flight to a specific destination")
def step_given_a_traveler_wants_to_book_a_flight_to_a_specific_destination(context):
    context.traveler = Traveler()
    context.destination = Destination()

@given("a specific departure date")
def step_given_a_specific_departure_date(context):
    context.departure_date = Date()

@given("a specific return date")
def step_given_a_specific_return_date(context):
    context.return_date = Date()

@given("a specific airline")
def step_given_a_specific_airline(context):
    context.airline = Airline()

@when("the traveler enters all the required information")
def step_when_the_traveler_enters_all_the_required_information(context):
    context.flight = Flight(context.destination, context.departure_date, context.return_date, context.airline)

@when("confirms the booking")
def step_when_confirms_the_booking(context):
    context.flight.book()

@then("the flight should be booked successfully")
def step_then_the_flight_should_be_booked_successfully(context):
    assert context.flight.is_booked

Task: Write a program to find the sum of the digits of a given number.
