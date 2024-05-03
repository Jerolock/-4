class Building:
    total = 0

    def __init__(self):
        Building.total += 1


while Building.total < 40:
    Building.total += 1
print(Building.total)