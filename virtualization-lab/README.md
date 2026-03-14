# Virtualization Lab – Kali + Windows + Metasploitable

## Overview

This lab demonstrates how to build a local cybersecurity and networking lab using **KVM virtualization** on Debian.

The goal is to safely practice networking concepts, system administration, and security tools using isolated virtual machines.

## Host System

* OS: Debian 13 (Trixie)
* Virtualization: KVM + Virt-Manager
* Hardware: Ryzen CPU with hardware virtualization

## Lab Architecture

```
Debian Host
│
├── Kali Linux VM (Security testing environment)
├── Windows VM (Practice target system)
└── Metasploitable VM (Intentionally vulnerable machine)
```

## Tools Used

* Kali Linux
* Metasploitable
* Windows VM
* Virt-Manager
* KVM

## Network Setup

All virtual machines are connected to an isolated virtual network.

Example subnet:

```
192.168.100.0/24
```

Example structure:

```
Kali Linux        192.168.100.10
Windows VM        192.168.100.20
Metasploitable    192.168.100.30
```

## Learning Goals

This lab helps practice:

* Virtual machine management
* Linux system administration
* Network discovery
* Port scanning
* Packet analysis
* Basic security concepts
* Windows system configuration

## Example Commands

Network discovery:

```
nmap -sn 192.168.100.0/24
```

Service detection:

```
nmap -sV 192.168.100.30
```

## Future Improvements

* Add router VM
* Simulate enterprise network
* Automate lab setup scripts
* Add packet capture experiments
* Add documentation for each experiment

## Author

Amrit – Computer Science Engineering Student
