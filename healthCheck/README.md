# Health Check Script

This repository contains a Python-based health-check script: `healthCheck.py`.

## What the script does

The script performs the following checks:

- **Ping check**: uses the system `ping` command to verify the host is reachable.
- **HTTP check**: uses `curl` or `wget` if available, otherwise falls back to Python's `urllib` to verify that a URL responds successfully.
- **SSH check**: uses the `ssh` command in batch mode to detect whether the host accepts SSH connections.
- **Port check**: uses a Python socket connection to test whether a specific TCP port is open and reachable.
- **Listener check**: uses `netstat` or `ss` to list active TCP/UDP listeners on the local machine.
- **Disk usage check**: uses Python's `shutil.disk_usage` to verify root filesystem usage stays below a threshold.

## How it works

The script is written as a reusable health-check utility:

- `command_available()` checks whether an external command exists in `PATH`.
- `run_command()` runs a command with a timeout and captures output.
- `check_ping()`, `check_http()`, `check_ssh()`, `check_netstat()`, `check_port()`, and `check_disk()` are separate functions, each returning `True` or `False`.
- The main script prints a section for each check and summarizes whether all checks passed.

## Run example

```bash
python3 healthCheck.py --host localhost --url http://localhost --port 80
```

## Notes on permissions

If you want to make the script executable, run:

```bash
chmod +x healthCheck.py
```

If you want to change ownership, use:

```bash
chown youruser:yourgroup healthCheck.py
```
