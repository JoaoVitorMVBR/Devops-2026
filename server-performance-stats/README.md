# System Monitor Shell Script 📊

A lightweight and efficient Bash script to monitor vital system resources
in Linux. Provides a real-time snapshot of CPU usage, RAM availability,
Disk space, and the most demanding processes.

---

## 🚀 Features

- **Total CPU Usage** — real-time percentage calculated via `/proc/stat`
- **Memory Metrics** — used vs. free (KB) with percentages
- **Disk Status** — total, used, and free space on root (`/`)
- **Process Analysis** — top 5 by CPU and top 5 by memory

---

## 📋 Prerequisites

| Tool | Purpose |
|---|---|
| `bash` | Script interpreter |
| `bc` | Floating-point math |
| `awk` `grep` `ps` `df` | Standard Linux utilities |

> Missing `bc`? Install it with:
> `sudo apt install bc`

---

## 🛠️ How to Run

**1. Clone the repo**
```bash
git clone https://github.com/seu-usuario/system-monitor.git
cd system-monitor
```

**2. Give execution permission**
```bash
chmod +x server-stats.sh
```

**3. Run**
```bash
./server-stats.sh
```

---

## 📊 Example Output

Uso total da CPU: .62%
Uso total da memória : 15.90% / Memória livre : 6637248 kb / Memória usada : 1273732 kb
Memória livre: 82.86%
Uso total do disco: 2% / Total: 1007G / Usado: 18G / Livre: 938G
Top 5 processos por uso de CPU:
    PID COMMAND         %CPU
   1922 node             3.5
   1648 node             1.0
   6404 node             0.6
    196 containerd       0.1
      1 systemd          0.0
Top 5 processos por uso de memória:
    PID COMMAND         %MEM
   1922 node             7.4
   1648 node             1.8
    280 dockerd          1.0
   6404 node             0.7
   1724 node             0.7

---

## 🔗 Project Reference

This project is part of the
[roadmap.sh — Server Stats challenge](https://roadmap.sh/projects/server-stats).