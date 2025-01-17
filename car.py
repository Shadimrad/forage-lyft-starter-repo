from abc import ABC, abstractmethod
from datetime import datetime

class Servicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass
class OctoprimeTires(tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        """Octoprime tires should be serviced only when the sum of all
        values in the tire wear array is greater than or equal to 3."""
        return sum(self.tire_wear) >= 3
        
class CarriganTires(tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    def needs_service(self):
        """Carrigan tires should be serviced only when one or more of
        the values in the tire wear array is greater than or equal to 0.9."""
        return any([wear >= 0.9 for wear in self.tire_wear])

class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class SternmanEngine(Engine):

    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

class WilloughbyEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
    

class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000


class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False


class Car(Servicable):
    def __init__(self, engine, battery ,tire_wear):
        self.battery = battery
        self.engine = engine
        self.tire_wear = tire_wear

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire_wear.needs_service()

class CarFactory:
 
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage , tire_wear_arr):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_wear = OctoprimeTires(tire_wear_arr)
        car = Car(engine, battery, tire_wear)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_arr):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_wear = OctoprimeTires(tire_wear_arr)
        car = Car(engine, battery, tire_wear)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear_arr):
        engine = SternmanEngine(current_date, warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire_wear = OctoprimeTires(tire_wear_arr)
        car = Car(engine, battery, tire_wear)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_arr):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire_wear = OctoprimeTires(tire_wear_arr)
        car = Car(engine, battery, tire_wear)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_arr):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire_wear = CarriganTires(tire_wear_arr)
        car = Car(engine, battery, tire_wear)
        return car
