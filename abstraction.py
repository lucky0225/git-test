class SortingAlgorithm():

    def sort(self):
        pass


class InsertionSort(SortingAlgorithm):

    # function override
    def sort(self):
        print("Here is: InsertionSort(SortingAlgorithm)")


class SelectionSort(SortingAlgorithm):
    
    # function override
    def sort(self):
        print("Here is: SelectionSort(SortingAlgorithm)")


class QuickSort(SortingAlgorithm):
    
    # function override
    def sort(self):
        print("Here is: QuickSort(SortingAlgorithm)")


num = input("Please select a sorting algorithm!\n 0: insertion sort\n 1: selection sort\n 2: quick sort\n")
num = int(num)

# NULL object
sorting_algorithm = None

if num == 0:
    sorting_algorithm = InsertionSort()
elif num == 1:
    sorting_algorithm = SelectionSort()
else:
    sorting_algorithm = QuickSort()

    print(sorting_algorithm.sort())


# practice
class Vehicle():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def fuel_consumption(self):
        print("average fuel consumption of a vehicle")

class Bus(Vehicle):
    def __innit__(self, brand, year):
        super().__init__(brand. year)

    def fuel_consumption(self):
        print("Fuel consumption for \"Bus\" is: 25l/100km")

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand,year)

    def fuel_consumption(self):
        print("Fuel consumption for \"Car\" is: 12l/100km")

bus = Bus(brand="Ford", year=1960)
print(bus.fuel_consumption())

car = Car(brand="BMW", year= 2018)
print(car.fuel_consumption())