class Building:
    def __init__(self):
        self.numberOfFloors = 15
        self.buildingType = 'дом'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


b1 = Building()
b2 = Building()
if Building.__eq__(self=b1, other=b2):
    print('О два дома')
