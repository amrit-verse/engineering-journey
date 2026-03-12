import psutil
import time
import os

while True:
    os.system("clear")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("=== System Monitor ===\n")

    print(f"CPU Usage: {cpu}%")

    print(f"RAM Usage: {memory.percent}%")
    print(f"RAM Used: {memory.used // (1024**3)} GB / {memory.total // (1024**3)} GB")

    print(f"Disk Usage: {disk.percent}%")
    print(f"Disk Used: {disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB")

    uptime = time.time() - psutil.boot_time()
    hours = int(uptime // 3600)

    print(f"System Uptime: {hours} hours")

    time.sleep(2)
