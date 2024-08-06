from abc import ABC, abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def getVehicleName(self):
        pass
