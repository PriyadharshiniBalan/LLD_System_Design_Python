from abc import ABC, abstractmethod
from Interface.IVehicle import IVehicle

class IVehicleFactory(ABC):
    #@abstractmethod
    def getVehicle(self, model) -> IVehicle:
        pass
