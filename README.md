
# Cars Manager 01

The program downloads data from a json file with information about cars and performs operations on them

## Features
- All the data in the cars.json file is validated and the wrong data is processed accordingly
- Sorting in descending or ascending order by appropriately selected fields specified via Enum
- Get cars that have a mileage greater than the entered value
- Separate the cars by colour
- Get the most expensive car of all cars of the same model
- Get statistics for cars
- Get a car with an alphabetically sorted list of components
- Get information on all cars that have the component
- Get cars in a given price range

## Prerequisites
Make sure you have the following installed on your computer:
- Python 3.10

## Tests
1. To run tests, set up in the main application folder and call with discover
```bash
$ python -m unittest discover
```
