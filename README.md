# Engineering Journey

This repository documents my journey to becoming a great engineer.

---

## Day 0

Today I learned:

- Setting up Git
- Connecting Git with GitHub using SSH
- Writing my first Python program
- Debugging and fixing a Linux WiFi driver issue
- Creating my first Git commit

## Day 1 – Photo Organizer

- Removed duplicate photos using jdupes
- Organized 5000+ iPhone photos and videos by date using Exif Tool
- Built a Python script to automatically organize photos using EXIF metadata

## Day 2 – System Monitor CLI Tool

Today I built a simple system monitoring tool using Python.

Features implemented:

- Monitor CPU usage
- Monitor RAM usage
- Monitor disk usage
- Display system uptime
- Show CPU temperature
- Display network statistics
- List top processes using CPU
- Added arrows (↑ ↓ →) to indicate increasing or decreasing resource usage
- Reduced terminal flickering by updating values instead of clearing the screen

Tools and technologies used:

- Python
- psutil library
- Linux system metrics

Goal: Learn how system information can be collected programmatically from the operating system.

## Day 3 – Disk Usage Analyzer

### Overview
Today I built a Python CLI tool that analyzes disk usage and identifies the largest directories inside a given path.

This is useful for understanding where storage space is being consumed on a Linux system.

### Technologies
- Python
- os module
- argparse

### Features
- Recursively calculates folder sizes
- Displays top directories by size
- Human-readable output (KB, MB, GB)

### Example Usage

python3 disk_analyzer.py /home/amrit

### Example Output

Scanning: /home/amrit

Top directories by size

1. 2.4 GB   Downloads
2. 1.8 GB   .cache
3. 950 MB   Videos
