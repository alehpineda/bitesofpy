"""
Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names 
(should work for other grep too)
Sort the models (values) alphabetically
See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is 
better to pass the cars dict into each function to make its 
scope local.
"""

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ", ".join(cars["Jeep"])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [cars[key][0] for key in cars]


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    return sorted(
        [
            e
            for _, val in cars.items()
            for e in val
            if grep.lower() in e.lower()
        ]
    )


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return {key: sorted(val) for key, val in cars.items()}
