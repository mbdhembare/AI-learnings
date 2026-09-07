import numpy as np

cpu_readings=np.array([87, 60, 90, 70, 75])
print(f"cpu readings: {cpu_readings}")

print(f"after adding 10: {cpu_readings+10}")
print(f"after multiplying by 2: {cpu_readings*2}")
print(f"average cpu: {cpu_readings.mean()}")
print(f"maximum cpu: {cpu_readings.max()}")
print(f"minimum cpu: {cpu_readings.min()}")
print(f"total cpu: {cpu_readings.sum()}")