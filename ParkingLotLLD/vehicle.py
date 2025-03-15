from vehicle_type import VehicleType

class Vehicle:

    def __init__(self, licence_number: str, vehicle_type: VehicleType):
        self.licence_number = licence_number
        self.vehicle_type = vehicle_type
    
    def get_type(self) -> VehicleType:
        return self.vehicle_type

    def get_licence_number(self) -> str:
        return self.licence_number
