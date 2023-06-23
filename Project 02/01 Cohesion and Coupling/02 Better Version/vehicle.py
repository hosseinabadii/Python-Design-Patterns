import string
import random

class VehicleInfo:

    def __init__(self, brand: str, catalogue_price: int, electric: bool) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self) -> float:
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.2
        return tax_percentage * self.catalogue_price
    
    def print(self):
        print(f"{'Brand':15} : {self.brand}")
        print(f"{'Payable tax':15} : ${self.compute_tax()}")


class Vehicle:

    def __init__(self, vehicle_id: str, vehicle_license: str, info: VehicleInfo) -> None:
        self.vehicle_id = vehicle_id
        self.vehicle_license = vehicle_license
        self.info = info

    def print(self):
        print("Resigtration complete. Vehicle information:")  
        print(f"{'ID':15} : {self.vehicle_id}")
        print(f"{'License plate':15} : {self.vehicle_license}")
        self.info.print()


class VehicleRegistry:

    vehicle_info = {}

    def add_vehicle_info(self, brand, catalogue_price, electric):
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def __init__(self) -> None:
        self.add_vehicle_info('Tesla', 60000, True)
        self.add_vehicle_info('BMW', 45000, False)
        self.add_vehicle_info('Volkswagon', 35000, True)
        self.add_vehicle_info('new', 50000, True)
    
    def generate_vehicle_id(self, length: int):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_vehicle_license(self, id):
        return f"{id[:5]}-{''.join(random.choices(string.digits, k=3))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand) -> Vehicle:
        vehicle_id = self.generate_vehicle_id(12)
        vehicle_license = self.generate_vehicle_license(vehicle_id)
        vehicle = Vehicle(vehicle_id, vehicle_license, self.vehicle_info[brand])
        return vehicle

