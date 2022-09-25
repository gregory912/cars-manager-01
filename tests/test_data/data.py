from car.model import Car

CAR_TEST_MODEL = Car.get_model({"model": "BMW", "price": 160, "mileage": 2500, "color": "SILVER",
                                "components": ["BLUETOOTH", "ABS", "RADIO", "CRUISE CONTROL"]})

MAZDA = Car.get_model({"model": "MAZDA", "price": 160, "mileage": 5000,
                       "color": "WHITE", "components": ['ABS']})

MAZDA_1 = Car.get_model({"model": "MAZDA", "price": 300, "mileage": 5000,
                         "color": "WHITE", "components": ['ABS']})

BMW = Car.get_model({"model": "BMW", "price": 160, "mileage": 3000,
                     "color": "SILVER", "components": ['ABS']})

BMW_1 = Car.get_model({"model": "BMW", "price": 400, "mileage": 3000,
                       "color": "SILVER", "components": ['RADIO']})

AUDI = Car.get_model({"model": "AUDI", "price": 160, "mileage": 1000,
                      "color": "BLACK", "components": ['RADIO']})

AUDI_1 = Car.get_model({"model": "AUDI", "price": 250, "mileage": 1000,
                        "color": "BLACK", "components": ['RADIO']})

PEUGEOT = Car.get_model({"model": "PEUGEOT", "price": 300, "mileage": 1200,
                         "color": "WHITE", "components": ['RADIO', 'ABS']})

RENAULT = Car.get_model({"model": "RENAULT", "price": 450, "mileage": 2000,
                         "color": "SILVER", "components": ["ABS"]})

SEAT = Car.get_model({"model": 'SEAT', "price": 2000, "mileage": 5000, "color": "WHITE",
                      "components": ['ROOF RACK', 'AIR CONDITIONING', 'PANORAMIC ROOF']})

FORD = Car.get_model({"model": 'FORD', "price": 1800, "mileage": 3000, "color": "SILVER",
                      "components": ['AIR CONDITIONING', 'CRUISE CONTROL', 'ABS', 'RADIO']})

SEAT_1 = Car.get_model({"model": 'SEAT', "price": 2000, "mileage": 5000, "color": "WHITE",
                        "components": ['AIR CONDITIONING', 'PANORAMIC ROOF', 'ROOF RACK']})

FORD_1 = Car.get_model({"model": 'FORD', "price": 1800, "mileage": 3000, "color": "SILVER",
                        "components": ['ABS', 'AIR CONDITIONING', 'CRUISE CONTROL', 'RADIO']})
