incidents={
    "service_name":"api-gateway",
    "cpu_usage":[70, 93, 89, 50],
    "error_rate": 35
}

high_cpu=[cpu for cpu in incidents["cpu_usage"] if cpu>70]
print(f"high_cpu: {high_cpu}")

memory_leakage=incidents.get("memory_leakage", "not_leakage")

print(f"memory_leakage:  {memory_leakage}")