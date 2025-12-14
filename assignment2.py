class Device:
    def __init__(self):
        print("=== Device Initialization ===")

        self.device_id = input("Enter device ID: ")
        self.device_type = input("Enter device type (phone / tablet / computer): ")
        self.location = input("Enter device location: ")
        self.os = input("Enter operating system: ")
        self.manufacturer = input("Enter manufacturer: ")

        self.connected = False
        self.base_station_id = None

        print("Device created successfully.\n")

    def info(self):
        return {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "location": self.location,
            "os": self.os,
            "manufacturer": self.manufacturer,
            "connected": self.connected,
            "base_station_id": self.base_station_id
        }

    def display(self):
        print("=== Device Info ===")
        for k, v in self.info().items():
            print(f"{k}: {v}")

device = Device()
device.display()
