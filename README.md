# 🕸️ Network Scanner — Ping Sweeper (Python + Scapy)

A simple Python-based **ping sweep tool** that scans a network and identifies live hosts using ICMP echo requests.  
Built using **Scapy** and **netaddr**, following the tutorial series:

📺 **YouTube Tutorial:**  
https://www.youtube.com/watch?v=wzltvLSsDkE&list=PLB7R26sRn2aLhKbDDRtd7wluaX91pqAQD&index=4

---

## 🚀 Features

- Scan all hosts in a subnet (e.g., `/24`)
- Detect online hosts using ICMP packets
- Progress counter during scanning
- Clean output (no Scapy warnings)
- Works on Windows when Npcap is installed

---

## 📦 Requirements

### 1️⃣ Python Version  
Use **Python 3.11** (best compatibility with Scapy).

### 2️⃣ Install Required Packages  
Install Scapy + netaddr into Python 3.11:

```bash
py -3.11 -m pip install scapy netaddr
```
### 3️⃣ Install Npcap (Windows)

Required for raw packet sending.

Download here:
https://nmap.org/npcap/

During installation, enable:

✔ Install Npcap in WinPcap API-compatible Mode

## ▶️ Usage
Run the script:
```bash
py -3.11 pingsweeper.py <network> <netmask>
```

## 📋 Example Output
```bash
Scanning host: 8/254
Host 192.168.1.1 is online.
Host 192.168.1.8 is online.
Completed scan.
Live hosts: ['192.168.1.1', '192.168.1.8']
```

## 🧩 Code Overview
- netaddr.IPNetwork() generates each host IP

- Scapy sends ICMP Echo Requests (ping)

- Hosts that respond are added to a live_hosts list

- Output is displayed as scan progresses

## 📁 Project Structure
network-scanner/
│
├── pingsweeper.py
└── README.md

## 🧹 Troubleshooting
### Scapy or netaddr not found
You installed packages in the wrong Python version.

Use:
```bash
py -3.11 -m pip install scapy netaddr
```

### Raw socket error on Windows
You need Npcap installed.

### VS Code shows “No name 'ICMP' in module 'scapy.all'”
This is a Pylint false warning. 

## 📜 Disclaimer
This project is for ethical and educational use only.
Only scan networks you own or have permission to test.