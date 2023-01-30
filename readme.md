# IoT Client - Aeroponic crop monitoring system

This python client allows to connect the IoT devices with the monitoring server, in order to perform the following actions:

- Upload telemetry data to the server

In order to use this client a _device token_ is required, this token is obtained when creating a new device in the monitoring server.

## Examples.

### Import and initialize the client

```python
from iot_client.iot_client import IotCLient

device_token = 'The_Device_Token'
iot_client = IotCLient(device_token)
```

### Load telemetry data without timestamp

```python
telemetry_without_timestamp = {
    "ph": 6,
    "conductivity": 20.23,
    "tank_level": 75,
    "current": 0.01,
}


try:
    iot_client.upload_telemetry(telemetry_without_timestamp)
except Exception as e:
    print(e)
```

### Load telemetry data with timestamp

```python
from time import time

telemetry_with_timestamp = {
    "timestamp": int(time()),
    "values": {
        "ph": 8,
        "conductivity": 16.6,
        "tank_level": 20,
        "current": 0.5,
    },
}

try:
    iot_client.upload_telemetry(telemetry_with_timestamp)
except Exception as e:
    print(e)
```
