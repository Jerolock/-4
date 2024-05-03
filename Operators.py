class Building:
    def __init__(self):
        self.numberOfFloors = 15
        self.buildingType = 'Небоскреб'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors

