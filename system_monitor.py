import psutil
import time
import os


def bar(percent, length=30):
    filled = int(length * percent / 100)
    return "█" * filled + "-" * (length - filled)


def gb(value):
    return round(value / (1024**3), 2)


while True:
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()

    os.system("clear")

    print("=========== SYSTEM MONITOR ===========\n")

    print("CPU")
    print(f"[{bar(cpu)}] {cpu}%")

    print("\nRAM")
    print(f"[{bar(mem.percent)}] {mem.percent}%")
    print(f"{gb(mem.used)} GB / {gb(mem.total)} GB")

    print("\nDISK")
    print(f"[{bar(disk.percent)}] {disk.percent}%")
    print(f"{gb(disk.used)} GB / {gb(disk.total)} GB")

    print("\nNETWORK")
    print(f"Sent: {round(net.bytes_sent / (1024**2), 2)} MB")
    print(f"Recv: {round(net.bytes_recv / (1024**2), 2)} MB")

    uptime = int((time.time() - psutil.boot_time()) / 3600)
    print(f"\nUPTIME: {uptime} hours")

    print("\n======================================")

    time.sleep(2)
