# Assignment 1: Design Your Own Class! 
class Smartphone:
    def __init__(self, model, brand, imei, battery_capacity_mah):
        self.model = model
        self.brand = brand
        self.imei = imei
        self.battery_capacity_mah = battery_capacity_mah
        self.battery_level = 100
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            print(f"{self.brand} {self.model} is powering on...")
            self.is_on = True
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        if self.is_on:
            print(f"{self.brand} {self.model} is powering off...")
            self.is_on = False
        else:
            print(f"{self.brand} {self.model} is already off.")

    def display_battery(self):
        print(f"{self.brand} {self.model} battery level: {self.battery_level}%")

    def charge(self, duration_minutes):
        if self.is_on:
            print("Please power off the phone to charge efficiently.")
            return
        charge_amount = (duration_minutes / 60) * 10  # Example: 10% charge per hour
        self.battery_level = min(100, self.battery_level + charge_amount)
        print(f"Charged {self.brand} {self.model} for {duration_minutes} minutes. Battery level is now {self.battery_level}%.")

class iPhone(Smartphone):
    def __init__(self, model, imei, battery_capacity_mah, ios_version):
        super().__init__(model, "Apple", imei, battery_capacity_mah)
        self.ios_version = ios_version
        self.is_face_id_enabled = False

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"IMEI: {self.imei}")
        print(f"Battery Capacity: {self.battery_capacity_mah} mAh")
        print(f"iOS Version: {self.ios_version}")
        print(f"Face ID Enabled: {'Yes' if self.is_face_id_enabled else 'No'}")
        print(f"Power Status: {'On' if self.is_on else 'Off'}")
        print(f"Battery Level: {self.battery_level}%")

    def enable_face_id(self):
        if not self.is_face_id_enabled:
            print("Face ID has been enabled.")
            self.is_face_id_enabled = True
        else:
            print("Face ID is already enabled.")

    def disable_face_id(self):
        if self.is_face_id_enabled:
            print("Face ID has been disabled.")
            self.is_face_id_enabled = False
        else:
            print("Face ID is already disabled.")

# Creating instances of the classes
phone1 = Smartphone("Galaxy S21", "Samsung", "358901234567890", 4000)
iphone1 = iPhone("iPhone 13 Pro", "351234567890123", 3095, "iOS 15")

# Interacting with the objects
phone1.power_on()
phone1.display_battery()
phone1.charge(30)
phone1.power_off()
print("\n")

iphone1.display_info()
iphone1.enable_face_id()
iphone1.disable_face_id()
iphone1.charge(60)
iphone1.power_on()
iphone1.display_battery()

# Activity 2: Polymorphism Challenge!
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving in a generic way.")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving 🚗.")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ✈️.")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing ⛵.")

def vehicle_actions(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Creating instances of different vehicles
my_car = Car("My Sedan")
my_plane = Plane("Boeing 747")
my_boat = Boat("Sailboat X")
generic_vehicle = Vehicle("Generic Transport")

# Creating a list of vehicles
all_vehicles = [my_car, my_plane, my_boat, generic_vehicle]

# Calling the move() method on each vehicle in the list
vehicle_actions(all_vehicles)