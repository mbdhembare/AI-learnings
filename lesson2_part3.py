import numpy as np

cpu_readings=np.array([67, 40, 90, 60, 80])
print(f"cpu_readings: {cpu_readings}")
print(f"cpu_readingd dimention: {cpu_readings.ndim}")
print(f"cpu_readings shape: {cpu_readings.shape}")

telemetry=np.array([
    [50, 47, 89],
    [34, 60, 90],
    [80, 30, 50]])

print(f"2d array: {telemetry}")

print(f"dimention: {telemetry.ndim}")
print(f"shape: {telemetry.shape}")

print(f"telementry val for row 1: {telemetry[0,:]}")
print(f"sclicing: {telemetry[1:3]}")
print(f"get data of first service: {telemetry[0,:]}")
print(cpu_readings>80)