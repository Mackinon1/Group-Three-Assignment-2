## Device Class

The `Device` class represents a user device in a networked system. It is responsible for collecting and storing basic device information at initialization and providing methods to access and display that data in a structured format.

### Overview

When a `Device` object is created, the class interactively prompts the user to enter key device details such as ID, type, location, operating system, and manufacturer. The device also tracks its network connection status and associated base station.

### Features

* Interactive device initialization via user input
* Stores essential device metadata
* Tracks connection status and base station association
* Provides formatted output for device information

### Attributes

* **device_id**: Unique identifier for the device
* **device_type**: Type of device (e.g., phone, tablet, computer)
* **location**: Physical or logical location of the device
* **os**: Operating system running on the device
* **manufacturer**: Device manufacturer
* **connected**: Boolean indicating network connection status
* **base_station_id**: Identifier of the connected base station (if any)

### Methods

* **`__init__()`**
  Initializes the device and prompts the user for required information.

* **`info()`**
  Returns a dictionary containing all device attributes.

* **`display()`**
  Prints the device information in a readable format.

### Example Usage

```python
device = Device()
device.display()
```

This class serves as a foundational component for simulations or applications involving device management and network connectivity.
