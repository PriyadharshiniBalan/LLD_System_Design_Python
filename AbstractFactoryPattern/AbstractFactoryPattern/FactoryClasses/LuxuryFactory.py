from Interface.IVehicleFactory import IVehicleFactory
from Interface.IVehicle import IVehicle
from ConcreteClasses.BMW import BMW
from ConcreteClasses.Mercedes import Mercedes

class LuxuryFactory(IVehicleFactory):
    def getVehicle(self,model) -> IVehicle:
        if model == "BMW":
            return BMW()
        elif model == "Mercedes":
            return Mercedes()
        else:
            raise ValueError("Unknown model")