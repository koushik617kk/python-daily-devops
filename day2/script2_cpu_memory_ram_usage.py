#So get me the cpu, memory, disk utilization 

import psutil
import time

def get_system_metrics():

    #CPU Metrics
    # interval=1 means last 1 second percentage of cpu utilization

    cpu_usage = psutil.cpu_percent(interval=1)

    memory= psutil.virtual_memory()
    memory_usage = memory.percent
    memory_free_gb = round(memory.available / (1024**3),2)

    if psutil.disk_usage('/'):
        disk_usage = psutil.disk_usage('/').percent

    else:
        disk_usahe = psutil.disk_usage('C:/').percent

    print("\n--- System Health Check")
    print(f"Time of check: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"CPU Usage: {cpu_usage}%\n")
    print(f"Memory Used: {memory_usage}% (free: {memory_free_gb}GB)")
    print(f"Disk Used: {disk_usage}%")


for i in range(3):
    get_system_metrics()
    time.sleep(3)


    
