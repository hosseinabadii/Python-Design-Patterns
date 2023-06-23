from vehicle import VehicleRegistry

def register_vehicle(brand: str) -> None:
     
    registry = VehicleRegistry()
    return registry.create_vehicle(brand)


if __name__ == "__main__":
    
    vehicle = register_vehicle("new")
    vehicle.print()
