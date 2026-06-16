sensor_readings = [10, 25, 30, 45, 12]
print("first value:", sensor_readings[0])
print("last valude:", sensor_readings[-1])
sensor_readings.append(50)
print("after appending new item", sensor_readings)

robot = {"name":"R2D2", "speed": 1.5, "battery": 80}
print(f"Robot Name is: {robot["name"]}")
robot["battery"] = 75
print(robot)


for value in sensor_readings:
    if value > 30:
        print(value, "----> HIGH")
    else:
        print(value, "----> LOW")


def average(numbers):
    return sum(numbers) / len(numbers)

print('averge value is:', average(sensor_readings))


class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def info(self):
        return f"{self.name} with speed {self.speed} m/s"

r = Robot("Rover", 2)
print(r.info())