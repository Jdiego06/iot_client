import requests


class IotCLient:
    _SERVER_URL = "https://iot-app.herokuapp.com/api"
    _client_token: str = None

    def __init__(self, token: str) -> None:
        self._client_token = token

    def upload_telemetry(self, telemetry: dict):
        """
        Upload telemetry data to the server.

        Args:
            telemetry (dict): The telemetry data as dict.

            E.g.
            {
                "value_str": "on",
                "value_int": 25,
                "value_float": 12.3,
                "value_bool": True
            }

            The telemetry timestamp could be explicitly specified if the telemetry is
            passed as follows:

            E.g.
            {
                "ts": 1672796836,
                "values": {
                    "value_str": "on",
                    "value_int": 25,
                    "value_float": 12.3,
                    "value_bool": True
                }
            }

        Raises:
            Exception: An exception if some error occurs.

        Return: None
        """
        telemetry_endpoint = (
            f"{self._SERVER_URL}/devices/{self._client_token}/telemetry"
        )
        response = requests.post(url=telemetry_endpoint, json=telemetry)

        if not response.ok:
            raise Exception("The telemetry data couldn't be loaded", response.json())
