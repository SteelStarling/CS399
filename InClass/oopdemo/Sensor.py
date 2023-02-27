from random import randint


class Sensor:
    frequency = 10

    def __init__(self, location: str):
        self.location = location
        self.request_counter = 0

    def value(self) -> bool:
        self.request_counter += 1
        return self.request_counter % self.frequency == 0

    def __str__(self):
        return self.__class__.__name__


class HumiditySensor(Sensor):
    frequency = 5

    def value(self) -> str:
        if super().value():
            return f"Humidity in the {self.location} is {randint(10, 90)}%"


class TemperatureSensor(Sensor):
    inCelsius = False

    def __init__(self, location: str, unit: str):
        super().__init__(location)
        self.unit = unit

    def value(self) -> str:
        if super().value():
            return f"Temperature in the {self.location} is {randint(42, 105)} {self.unit}"


ts = TemperatureSensor("Kitchen", "F")
hs = HumiditySensor("Bathroom")
sl = [ts, hs]
for i in range(30):
    for s in sl:
        reading = s.value()
        if reading:
            print(f"{s.request_counter} .. {s} : {s.value()}")
