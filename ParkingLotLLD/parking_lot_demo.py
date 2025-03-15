from parking_lot import ParkingLot
from vehicle_type import VehicleType
from level import Level
from car import Car
from bike import Bike
from truck import Truck

level1_spots_config = {
    1: VehicleType.CAR,
    2: VehicleType.TRUCK,
    3: VehicleType.TRUCK
}

level2_spots_config = {
    1: VehicleType.CAR,
    2: VehicleType.BIKE,
    3: VehicleType.CAR
}

level3_spots_config = {
    1: VehicleType.CAR,
    2: VehicleType.BIKE,
    3: VehicleType.BIKE
}    

class ParkingLotDemo:

    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, level1_spots_config))
        parking_lot.add_level(Level(2, level2_spots_config))

        car = Car("ABC123")
        truck = Truck("XYZ789")
        bike = Bike("M1234")

        # Display availability
        parking_lot.display_availability()        

        # Park vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(bike)

        # Display availability
        parking_lot.display_availability()

        # Unpark vehicle
        parking_lot.unpark_vehicle(bike)

        # Display updated availability
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()