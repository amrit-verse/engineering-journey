# Engineering Journey 🚀

This repository documents my journey toward becoming a skilled engineer through daily hands-on projects, problem solving, and system exploration.

Each day focuses on building something practical while learning new tools and concepts.

---

## Day 0 – Environment Setup

Today I set up the core development environment.

### What I learned

* Setting up **Git**
* Connecting **Git with GitHub using SSH**
* Writing my **first Python program**
* Debugging and fixing a **Linux WiFi driver issue**
* Creating my **first Git commit**

### Key Takeaway

Understanding development tools and solving system-level issues is an essential part of engineering.

---

## Day 1 – Photo Organizer 📷

Today I organized a large photo collection and automated the process.

### Tasks Completed

* Removed duplicate photos using **jdupes**
* Organized **5000+ iPhone photos and videos** by date using **ExifTool**
* Built a **Python script** to automatically organize photos using **EXIF metadata**

### What I Learned

* Working with **metadata**
* Automating repetitive tasks
* Using command-line tools with Python

---

## Day 2 – System Monitor CLI Tool 💻

Today I built a **command-line system monitoring tool** using Python.

### Features

* Monitor **CPU usage**
* Monitor **RAM usage**
* Monitor **disk usage**
* Display **system uptime**
* Show **CPU temperature**
* Display **network statistics**
* List **top processes by CPU usage**

### Improvements

* Added arrows **(↑ ↓ →)** to indicate resource usage trends
* Reduced terminal flickering by updating values instead of clearing the screen

### Technologies Used

* Python
* `psutil` library
* Linux system metrics

### Goal

Learn how system information can be collected programmatically from the operating system.

---

## Day 3 – Disk Usage Analyzer 📊

### Overview

Today I built a **Python CLI tool** that analyzes disk usage and identifies the largest directories inside a given path.

This helps understand where storage space is being consumed on a Linux system.

### Technologies

* Python
* `os` module
* `argparse`

### Features

* Recursively calculates **folder sizes**
* Displays **top directories by size**
* Outputs sizes in **human-readable format (KB, MB, GB)**

### Example Usage

```bash
python3 disk_analyzer.py /home/amrit
```

### Example Output

```
Scanning: /home/amrit

Top directories by size

2.4 GB  Downloads
1.8 GB  .cache
950 MB  Videos
```
