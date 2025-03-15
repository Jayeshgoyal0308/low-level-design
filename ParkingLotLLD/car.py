from vehicle import Vehicle
from vehicle_type import VehicleType

class Car(Vehicle):
    
    def __init__(self, licence_number: str):
        super().__init__(licence_number, VehicleType.CAR)
