class Building:
    total = 0

    def __init__(self):
        Building.total += 1


house = Building()
while house.total < 40:
    house.total += 1
print(house.total)