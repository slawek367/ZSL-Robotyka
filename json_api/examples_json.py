import json
import sys

# Example 1
# Save class object to json file
# and load it to other list

class Car(object):
    def __init__(self, id = None, name = None, prod_year = None, power = None, json_data = None):
        self.id = id
        self.name = name
        self.prod_year = prod_year
        self.power = power

        if json_data is not None:
            self.__dict__ = json_data
    
    def get_json_format(self):
        return self.__dict__

#create list of cars
cars = []
cars.append(Car(1, "Audi TT", 2000, 198))
cars.append(Car(2, "BMW Z3", 2008, 302))
cars.append(Car(3, "Opel Astra", 1996, 102))

#save list to file as json
with open('cars.json', 'w') as outfile:
    json_to_save = {}
    for car in cars:
        json_to_save[car.id] = car.get_json_format()
    outfile.write(json.dumps(json_to_save, indent=4))

new_cars = []
#load objects from json file
with open('cars.json', 'r') as outfile:
    loaded_json = json.load(outfile)
    for id, car_json in loaded_json.items():
        print("Loaded car: " + str(car_json))
        new_cars.append(Car(json_data = car_json))

print("New loaded object list contains:")
for car in new_cars:
    print(car.name)