import psutil
import time
import sys

prev_cpu = None
prev_ram = None

def trend(curr, prev):
    if prev is None:
        return " "
    if curr > prev:
        return "↑"
    if curr < prev:
        return "↓"
    return "→"

while True:
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    ram = mem.percent

    cpu_tr = trend(cpu, prev_cpu)
    ram_tr = trend(ram, prev_ram)

    prev_cpu = cpu
    prev_ram = ram

    # Move cursor to top instead of clearing screen
    sys.stdout.write("\033[H")
    sys.stdout.flush()

    print("=== System Monitor ===\n")

    print(f"CPU Usage: {cpu}% {cpu_tr}")
    print(f"RAM Usage: {ram}% {ram_tr}")

    print(f"\nDisk Usage: {disk.percent}%")
    print(f"Disk Used: {disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB")

    uptime = time.time() - psutil.boot_time()
    hours = int(uptime // 3600)
    print(f"\nSystem Uptime: {hours} hours")

    time.sleep(2)
