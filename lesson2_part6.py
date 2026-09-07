import numpy as np

telemetry= np.array([
    [90, 50, 40],
    [30, 50, 10],
    [75, 80, 20],
    [85, 95, 35]
])

cpu=telemetry[:, 0]
error_rate=telemetry[:, 2]
problematic=(cpu>80) | (error_rate>30)
problematic_service=telemetry[problematic]
print(problematic_service)