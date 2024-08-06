from FactoryClasses.LuxuryFactory import LuxuryFactory
from FactoryClasses.OrdinaryFactory import OrdinaryFactory

def main():
    #Create a factory
    factory = LuxuryFactory()

    # Get an BMW Vehicle
    vehicle = factory.getVehicle("BMW")
    print(vehicle.getVehicleName())

    # Get an Mercedes Vehicle
    vehicle = factory.getVehicle("Mercedes")
    print(vehicle.getVehicleName())
        
    factory = OrdinaryFactory()
    
    # Get an Maruti Vehicle
    vehicle = factory.getVehicle("Maruti")
    print(vehicle.getVehicleName())

    # Get an Swift Vehicle
    vehicle = factory.getVehicle("Swift")
    print(vehicle.getVehicleName())

if __name__ == "__main__":
    main()