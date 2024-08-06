from Interface.IVehicleFactory import IVehicleFactory
from Interface.IVehicle import IVehicle
from ConcreteClasses.Maruti import Maruti
from ConcreteClasses.Swift import Swift

class OrdinaryFactory(IVehicleFactory):
    def getVehicle(self, model) -> IVehicle:
        if model == "Swift":
            return Swift()
        elif model == "Maruti":
            return Maruti()