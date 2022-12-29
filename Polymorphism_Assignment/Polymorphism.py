
# Parent class
class Vehicle:
    make = 'Unknown'
    model = 'Unknow'
    year =  None
    size = 'Unknown'
    cylinders = None

    def about(self):
        info = "\nMake: {}\nModel: {}\nYear: {}\nBody Type: {}\nNumber of Engine Cylinders: {}".format(self.make,self.model,self.year,self.size,self.cylinders)
        return info

# Child class 
class Truck(Vehicle):
    make = 'Ford'
    model = 'F350'
    year =  2014
    size = 'Crew-Cab'
    cylinders = 8
    #Added attributes
    bed_size = '12\''
    lift_kit = True
    
    # The method is the same as the parent class but it also displays the added atttributes to this specific child class
    def about(self):
        info = "\nMake: {}\nModel: {}\nYear: {}\nBody Type: {}\nNumber of Engine Cylinders: {}\nSize of Bed: {}\nEquipped with lift kit: {}".format(self.make,self.model,self.year,self.size,self.cylinders,self.bed_size,self.lift_kit)
        return info

# Another child class 
class Car(Vehicle):
    make = 'Infiniti'
    model = 'G37s'
    year =  2012
    size = 'Coupe'
    cylinders = 6
    # Added attributes
    low_kit = True
    wheels = 'Aftermarket'

    # The method is the same as the parent class but it also displays the added atttributes p this specific child class
    def about(self):
        info = "\nMake: {}\nModel: {}\nYear: {}\nBody Type: {}\nNumber of Engine Cylinders: {}\nEquipped with lowering kit: {}\nType of wheels: {}".format(self.make,self.model,self.year,self.size,self.cylinders,self.low_kit,self.wheels)
        return info

# Invoking the methods inside each of the child classes
if __name__ == "__main__":
    truck = Truck()
    print(truck.about())

    car = Car()
    print(car.about())
