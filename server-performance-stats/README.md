# System Monitor Shell Script 📊

A lightweight and efficient Bash script to monitor vital system resources in Linux. It provides a real-time snapshot of CPU usage, RAM availability, Disk space, and the most demanding processes.

---

## 🚀 Features

The script calculates and displays:
*   **Total CPU Usage:** Real-time percentage calculated via `/proc/stat`.
*   **Memory Metrics:** Total used vs. free memory (in KB) and their respective percentages.
*   **Disk Status:** Total, used, and free space on the root (`/`) partition.
*   **Process Analysis:** Top 5 processes ranked by CPU and Memory consumption.

---

## 📋 Prerequisites

Most tools used are native to Linux distributions. However, ensure you have:
*   **Bash:** The script's interpreter.
*   **bc:** An arbitrary precision calculator language (required for decimal/floating-point math).
*   **Standard Utilities:** `awk`, `grep`, `ps`, and `df`.

> **Note:** If `bc` is missing on Ubuntu/Debian, install it using:  
> `sudo apt install bc`

---

## 🛠️ How to Run

Follow these steps to set up and execute the monitor:

### 1. Create the File
Open your terminal and create a new file named `monitor.sh`:
```bash
nano monitor.sh

https://roadmap.sh/projects/server-stats