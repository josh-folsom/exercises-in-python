#2. Make your own class
#Create a class Vehicle. A Vehicle object will have 3 attributes:
# make
# model
# year


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print("Vehicle Details: {} - {} - {}".format(self.year, self.make, self.model))

audi = Vehicle('Audi', 'R8', '2019')
print(audi.make, audi.model, audi.year)
audi.print_info()
