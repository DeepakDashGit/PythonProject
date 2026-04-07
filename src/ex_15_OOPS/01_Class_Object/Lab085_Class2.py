# 1. This is the 'Cabinet'
class SmartDevice:
    # 2. This is how we 'set up' the device when we buy it
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    # 3. This is an 'Action' the device can take
    def check_battery(self):
        print(f"The {self.brand} has {self.battery}% power left.")

    def charge(self):
        self.battery = self.battery + 10
        print(f"Charging... Battery is now {self.battery}%")

# 4. We 'build' a real phone from the blueprint
my_phone = SmartDevice("Real Me", 64)

# 5. We trigger the action
my_phone.check_battery()
my_phone.charge()

