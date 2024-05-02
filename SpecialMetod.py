class House:
    def __init__(self):

        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors


house = House()
print(house.numberOfFloors)
house.setNewNumberOfFloors(15)
print(house.numberOfFloors)
