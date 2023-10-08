from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, model, color, body_type, num_wheels, fuel_type, transmission_type, engine_volume):
        self.brand = brand
        self.model = model
        self.color = color
        self.body_type = body_type
        self.num_wheels = num_wheels
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type
        self.engine_volume = engine_volume

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def service(self):
        pass

    @abstractmethod
    def shift_gear(self):
        pass

    @abstractmethod
    def turn_on_lights(self):
        pass

    @abstractmethod
    def turn_on_wipers(self):
        pass


class ConcreteCar(Car):
    def move(self):
        print(f"The {self.brand} {self.model} is moving.")

    def service(self):
        print(f"The {self.brand} {self.model} is being serviced.")

    def shift_gear(self):
        print(f"The {self.brand} {self.model} is shifting gears.")

    def turn_on_lights(self):
        print(f"The lights of the {self.brand} {self.model} are turned on.")

    def turn_on_wipers(self):
        print(f"The wipers of the {self.brand} {self.model} are turned on.")


class StreetSweeper(Car):
    def move(self):
        print(f"The street sweeper is cleaning the street.")

    def service(self):
        print(f"The street sweeper is being serviced.")

    def shift_gear(self):
        pass

    def turn_on_lights(self):
        pass

    def turn_on_wipers(self):
        pass


class CarWithAdditionalFeatures(Car):
    def turn_on_fog_lights(self):
        print(f"The fog lights of the {self.brand} {self.model} are turned on.")

    def transport_cargo(self):
        print(f"The {self.brand} {self.model} is transporting cargo.")


class ThreeWheeler(Car):
    def __init__(self, brand, model, color, body_type, fuel_type, transmission_type, engine_volume):
        super().__init__(brand, model, color, body_type, 3, fuel_type, transmission_type, engine_volume)

    def move(self):
        print(f"The {self.brand} {self.model} is moving on three wheels.")

    def service(self):
        print(f"The {self.brand} {self.model} is being serviced.")

    def shift_gear(self):
        print(f"The {self.brand} {self.model} is shifting gears.")

    def turn_on_lights(self):
        print(f"The lights of the {self.brand} {self.model} are turned on.")

    def turn_on_wipers(self):
        print(f"The wipers of the {self.brand} {self.model} are turned on.")


class FlyingCar(Car):
    def move(self):
        print(f"The {self.brand} {self.model} is flying.")

    def service(self):
        print(f"The {self.brand} {self.model} is being serviced.")

    def shift_gear(self):
        pass

    def turn_on_lights(self):
        pass

    def turn_on_wipers(self):
        pass


class GasStation:
    def refuel(self, car):
        print(f"The {car.brand} {car.model} is being refueled.")


if __name__ == '__maine':
    car1 = ConcreteCar("Toyota", "Camry", "Red", "Sedan", 4, "Gasoline", "Automatic", 2.5)
    car1.move()
    car1.service()
    car1.shift_gear()
    car1.turn_on_lights()
    car1.turn_on_wipers()

    sweeper = StreetSweeper("Street Sweeper", "Model X", "Yellow", "Truck", 4, "Diesel", "Automatic", 6.0)
    sweeper.move()
    sweeper.service()

    car2 = CarWithAdditionalFeatures("BMW", "X5", "Black", "SUV", 4, "Gasoline", "Automatic", 3.0)
    car2.move()
    car2.service()
    car2.shift_gear()
    car2.turn_on_lights()
    car2.turn_on_wipers()
    car2.turn_on_fog_lights()
    car2.transport_cargo()

    car3 = ThreeWheeler("Piaggio", "Ape", "Blue", "Van", "Gasoline", "Manual", 0.5)
    car3.move()
    car3.service()
    car3.shift_gear()
    car3.turn_on_lights()
    car3.turn_on_wipers()

    car4 = FlyingCar("Terrafugia", "Transition", "Silver", "Sedan", 4, "Gasoline", "Automatic", 1.6)
    car4.move()
    car4.service()

    gas_station = GasStation()
    gas_station.refuel(car1)
