from iot_client.iot_client import IotCLient
from time import time


iot_client = IotCLient("IOsfX9A3Aj9apoGT")

# Telemetry upload, only values.
telemetry_1 = {
    "ph": 6,
    "conductivity": 20.23,
    "tank_level": 75,
    "current": 0.01,
}


iot_client.upload_telemetry(telemetry_1)


# Telemetry upload, values and timestamp.
telemetry_2 = {
    "timestamp": int(time()),
    "values": {
        "ph": 8,
        "conductivity": 16.6,
        "tank_level": 20,
        "current": 0.5,
    },
}

iot_client.upload_telemetry(telemetry_2)
