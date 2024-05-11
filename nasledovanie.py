class Car:
    price = 1000000

    def horse_power(self):
        print(150)


class Nissan(Car):
    price = 500000

    def horse_power(self):
        print(140)


class Kia(Car):
    price = 150000

    def horse_power(self):
        print(130)


car = Car()
car.horse_power()
