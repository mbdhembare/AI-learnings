name="monali"
salary= 3000.2
role="developer"
ai_learning=True

cpu_readings=[90, 87, 20, 59, 80]

incidents={
    "service_name":"api-gateway",
    "cup_usage":85,
    "error_rate":35
}

def get_status(cpu_usage):
    if(cpu_usage>90):
        return "critical"
    elif(cpu_usage>70):
        return "High"
    else:
        return "Normal"

for cpu in cpu_readings:
    status=get_status(cpu)
    print(f"cpu_reading: {cpu} | status: {status}")



print("\n Incident Details:")
print(f"cpu_usage: {incidents['cup_usage']}%")
print(f"error_rate: {incidents['error_rate']}%")