from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, make, model, spec):
    self.make = make
    self.model = model
    self.spec = spec

  @abstractmethod
  def start_engine(self):
    pass

class Car(Vehicle):
  def start_engine(self):
    print(f'{self.make} {self.model} ({self.spec}): engine started')

class Motorcycle(Vehicle):
  def start_engine(self):
    print(f'{self.make} {self.model} ({self.spec}): engine started')

class VehicleFactory(ABC):
  @abstractmethod
  def create_car(self, make, model, spec):
    pass

  @abstractmethod
  def create_motorcycle(self, make, model, spec):
    pass

class USVehicleFactory(VehicleFactory):
  def create_car(self, make, model):
    return Car(make, model, 'US Spec')

  def create_motorcycle(self, make, model):
    return Motorcycle(make, model, 'US Spec')

class EUVehicleFactory(VehicleFactory):
  def create_car(self, make, model):
    return Car(make, model, 'EU Spec')

  def create_motorcycle(self, make, model):
    return Motorcycle(make, model, 'EU Spec')

if __name__ == '__main__':
  us_factory = USVehicleFactory()
  vehicle1 = us_factory.create_car('Ford', 'Mustang')
  vehicle1.start_engine()

  eu_factory = EUVehicleFactory()
  vehicle2 = eu_factory.create_motorcycle('Harley-Davidson', 'Sportster')
  vehicle2.start_engine()