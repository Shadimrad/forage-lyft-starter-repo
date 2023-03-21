from abc import ABC, abstractmethod
import datetime

class Servicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Engine(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def needs_service(self):
        pass

class SternmanEngine(Engine):

    def __init__(self, last_service_date, warning_light_is_on):
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

class WilloughbyEngine(Engine):
    
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
    

class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000


class Battery(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def needs_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


class Car(Servicable):
    def __init__(self, engine, battery):
        self.battery = Battery
        self.engine = Engine

    def needs_service(self):
        pass

class CarFactory():
    def __init__(self):
        pass
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, CapuletEngine, SpindlerBattery)
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, WilloughbyEngine, SpindlerBattery)
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Car(last_service_date, SternmanEngine, SpindlerBattery)
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, WilloughbyEngine, NubbinBattery)
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(last_service_date, CapuletEngine, NubbinBattery)
