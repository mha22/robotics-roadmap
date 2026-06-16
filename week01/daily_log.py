sensor_readings = [23, 45, 21, 29, 30]

def analyze_temperatures(numbers):
    average = sum(numbers) / len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)

    return f"max:{max_value}\nmin:{min_value}\naverage:{average}"

print(analyze_temperatures(sensor_readings))