import string
import random

class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))
    
    def generate_vehicle_license(self, id):
        return f"{id[:5]}-{''.join(random.choices(string.digits, k=3))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:

    def register_vehicle(self, brand: str):
        # create a registry instance
        registry = VehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # generate a license plate for vehicle
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla":
            catalogue_price = 60_000
        elif brand == "Volkswagon":
            catalogue_price = 35_000
        elif brand == "BMW":
            catalogue_price = 45_000

        # compute the tax percentage
        # default is 5% of the catalogue price, except for electric cars where is 2%
        tax_percentage = 0.05
        if brand == "Tesla" or brand == "Volkswagon":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Resigtration complete. Vehicle information:")
        print(f"{'Brand':15} : {brand}")
        print(f"{'Id':15} : {vehicle_id}")
        print(f"{'License plate':15} : {license_plate}")
        print(f"{'Payable tax':15} : ${payable_tax}")



if __name__ == "__main__":

    app = Application()
    app.register_vehicle("Tesla")
