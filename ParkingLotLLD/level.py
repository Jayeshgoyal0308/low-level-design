from parking_spot import ParkingSpot
from vehicle_type import VehicleType
from vehicle import Vehicle
from typing import List


class Level:
    def __init__(self, floor: int, spots_config: dict[int, VehicleType]):
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = []
        for spot_number, vehicle_type in spots_config.items():
            self.parking_spots.append(ParkingSpot(spot_number, vehicle_type))

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False

    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.parking_spots:
            if spot.is_available():
                print(f"Spot {spot.get_spot_number()}: Available for {spot.get_vehicle_type().value}")
            else:
                parked_vehicle = spot.get_parked_vehicle()
                print(f"Spot {spot.get_spot_number()}: occupied by {parked_vehicle.get_type().value} {parked_vehicle.get_licence_number()}")
