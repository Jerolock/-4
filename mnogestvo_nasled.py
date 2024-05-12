class Vehicle:
    vehicle_type = None


class Car:
    price = 10000000

    def horse_powers(self):
        print(150)


class Nissan(Vehicle, Car):
    price = 15000000
    vehicle_type = "car"

    def horse_powers(self):
        print(140)


car = Nissan()
print(car.price, car.vehicle_type)
