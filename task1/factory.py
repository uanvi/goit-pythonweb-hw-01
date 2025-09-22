from abc import ABC, abstractmethod
from utils.logger import logger

# 1. Abstract Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


# 2.  Car and Motorcycle from Vehicle
class Car(Vehicle):
    def __init__(self, make: str, model: str, spec: str):
        super().__init__(make, model)
        self.spec = spec

    def start_engine(self) -> None:
        logger.info("%s %s (%s): Двигун запущено", self.make, self.model, self.spec)


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, spec: str):
        super().__init__(make, model)
        self.spec = spec

    def start_engine(self) -> None:
        logger.info("%s %s (%s): Мотор заведено", self.make, self.model, self.spec)


# 3. Abstract VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


# 4. Fabric impl
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# 5. run
def main():
    # Створення
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # US фабрики
    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    # EU фабрики
    vehicle3 = eu_factory.create_car("BMW", "3 Series")
    vehicle3.start_engine()

    vehicle4 = eu_factory.create_motorcycle("Ducati", "Monster")
    vehicle4.start_engine()


if __name__ == "__main__":
    main()