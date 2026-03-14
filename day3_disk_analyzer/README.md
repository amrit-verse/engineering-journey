# Disk Usage Analyzer 📊

## Overview

A Python CLI tool that analyzes disk usage and identifies the largest directories inside a given path.

Useful for understanding where storage space is being consumed on a Linux system.

## Features

* Recursively calculates folder sizes
* Displays largest directories
* Human-readable size output (KB, MB, GB)

## Technologies

* Python
* os module
* argparse

## Example Usage

python3 disk_analyzer.py /home/amrit

## Example Output

Scanning: /home/amrit

Top directories by size

2.4 GB Downloads
1.8 GB .cache
950 MB Videos
