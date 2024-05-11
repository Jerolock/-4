class Building:
    total = 0

    def __init__(self):
        Building.total += 1


town = []
town_size = 40
while len(town) < town_size:
    new_house = Building()
    town.append(new_house)
print(Building.total)
