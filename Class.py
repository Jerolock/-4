class House:
    def __init__(self):
        self.numberOfFloors = 10


House.numberOfFloors = 10
while House.numberOfFloors <= 10:
    print('Текущий Этаж Равен ', House.numberOfFloors)
    House.numberOfFloors -= 1
    if House.numberOfFloors == 1:
        print('Мы спустились на', House.numberOfFloors)
        break


