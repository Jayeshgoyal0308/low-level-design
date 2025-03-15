from threading import Lock
from level import Level
from vehicle import Vehicle

class ParkingLot:
    _instance = None
    _lock = Lock()

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton and cannot be instantiated directly.")
        
        self.levels: list[Level] = []
    
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:  # Use lock for thread-safety
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()  # Create the single instance
        return ParkingLot._instance
    
    def add_level(self, level: Level):
        self.levels.append(level)
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    
    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()
        print()
