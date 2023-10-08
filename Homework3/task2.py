from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def service(self):
        pass


class Car(Vehicle):
    def shift_gear(self):
        pass

    def turn_on_lights(self):
        pass

    def turn_on_wipers(self):
        pass


class StreetSweeper(Vehicle):
    def move(self):
        pass

    def service(self):
        pass


class CarWithAdditionalFeatures(Car):
    def turn_on_fog_lights(self):
        pass

    def transport_cargo(self):
        pass


class ThreeWheeler(Vehicle):
    def move(self):
        pass

    def service(self):
        pass


class FlyingCar(Vehicle):
    def move(self):
        pass

    def service(self):
        pass


class GasStation:
    def refuel(self, vehicle):
        pass
