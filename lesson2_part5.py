import numpy as np
# cpu_readings=np.array([60, 90, 70, 80, 86])
# Boolean indexing/filtering.
# high_readings=cpu_readings[cpu_readings>80]
# print(high_readings)

telemetry=np.array([
    [30, 50, 90],
    [98, 10, 60],
    [84, 48, 32],
    [55, 20, 100]
])

cpu_readings=telemetry[:,0]
print(f"all cpu readings: {cpu_readings}")

high_readings=cpu_readings[cpu_readings>80]
print(f"high cpu readings > 80:  {high_readings}")
print(f"number of high cpu readings: {len(high_readings)}")