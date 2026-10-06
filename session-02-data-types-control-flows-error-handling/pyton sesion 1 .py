def clean_and_average(raw_data):
    valid_temps = []
    for elem in raw_data:
        try:
            valid_temps.append(float(elem))
        except(TypeError, ValueError):
            pass
    avg=0
    totalsum=0
    for elem in valid_temps:
        totalsum= totalsum + elem 
        avg = totalsum/len(valid_temps)
    return avg

sensor_readings = [22.5, "23.1", "error", None, 21, "22.0C", 19.8]
print(f"Average: {clean_and_average(sensor_readings)}")