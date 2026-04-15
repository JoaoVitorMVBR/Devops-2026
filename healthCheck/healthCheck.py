#!/usr/bin/env python3
"""Simple health-check script using Linux tools and Python.

This script demonstrates how to perform basic service and host health checks
with `ping`, `curl`/`wget`, `ssh`, and `netstat`. It also shows a Python-only
fallback for disk usage and port reachability.
"""

import argparse
import shutil
import socket
import subprocess
import sys
import urllib.request
from typing import Optional


def command_available(command: str) -> bool:
    """Return True if the given command is available in PATH."""
    return shutil.which(command) is not None


def run_command(cmd: list[str], capture_output: bool = True, timeout: int = 10) -> tuple[int, str, str]:
    """Run a shell command and return (exit_code, stdout, stderr)."""
    result = subprocess.run(
        cmd,
        capture_output=capture_output,
        text=True,
        timeout=timeout,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def check_ping(host: str, count: int = 3) -> bool:
    """Check if a host responds to ICMP ping."""
    if not command_available("ping"):
        print("ping command not found; skipping ping check.")
        return False

    cmd = ["ping", "-c", str(count), "-W", "2", host]
    returncode, stdout, stderr = run_command(cmd)
    print(stdout or stderr)
    return returncode == 0


def check_http(url: str) -> bool:
    """Verify HTTP response using curl, wget, or urllib fallback."""
    if command_available("curl"):
        cmd = ["curl", "-I", "--max-time", "5", url]
        returncode, stdout, stderr = run_command(cmd)
        print(stdout or stderr)
        return returncode == 0

    if command_available("wget"):
        cmd = ["wget", "--spider", "--timeout=5", url]
        returncode, stdout, stderr = run_command(cmd)
        print(stdout or stderr)
        return returncode == 0

    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            print(f"HTTP status: {response.status}")
            return 200 <= response.status < 400
    except Exception as exc:
        print(f"urllib failed: {exc}")
        return False


def check_ssh(host: str, port: int = 22, user: Optional[str] = None) -> bool:
    """Check SSH reachability using ssh in batch mode."""
    if not command_available("ssh"):
        print("ssh command not found; skipping SSH check.")
        return False

    ssh_target = f"{user}@{host}" if user else host
    cmd = [
        "ssh",
        "-o",
        "BatchMode=yes",
        "-o",
        "ConnectTimeout=5",
        "-p",
        str(port),
        ssh_target,
        "echo ok",
    ]
    returncode, stdout, stderr = run_command(cmd)
    print(stdout or stderr)
    return returncode == 0 and stdout.strip() == "ok"


def check_netstat() -> bool:
    """Show active TCP/UDP listeners with netstat or ss."""
    if command_available("netstat"):
        cmd = ["netstat", "-tuln"]
    elif command_available("ss"):
        cmd = ["ss", "-tuln"]
    else:
        print("neither netstat nor ss is available; skipping listener check.")
        return False

    returncode, stdout, stderr = run_command(cmd)
    print(stdout or stderr)
    return returncode == 0


def check_port(host: str, port: int, timeout: int = 3) -> bool:
    """Try a TCP socket connection to a specific host and port."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError as exc:
        print(f"Port check failed: {exc}")
        return False


def check_disk(threshold_percent: int = 90) -> bool:
    """Check local disk usage and alert if threshold is exceeded."""
    usage = shutil.disk_usage("/")
    percent_used = int((usage.used / usage.total) * 100)
    print(f"Disk usage: {percent_used}% (used {usage.used // (1024**3)}GiB of {usage.total // (1024**3)}GiB)")
    return percent_used < threshold_percent


def print_section(title: str) -> None:
    """Format output sections for readability."""
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Health-check script for host, HTTP, SSH, netstat, and disk usage."
    )
    parser.add_argument("--host", default="localhost", help="Host to ping and test ports")
    parser.add_argument("--url", default="http://localhost", help="URL to test via HTTP")
    parser.add_argument("--port", type=int, default=80, help="TCP port to test with socket")
    parser.add_argument("--ssh-user", help="SSH user for the SSH health check")
    args = parser.parse_args()

    print_section("PING CHECK")
    ping_ok = check_ping(args.host)
    print("PING OK" if ping_ok else "PING FAILED")

    print_section("HTTP CHECK")
    http_ok = check_http(args.url)
    print("HTTP OK" if http_ok else "HTTP FAILED")

    print_section("SSH CHECK")
    ssh_ok = check_ssh(args.host, user=args.ssh_user)
    print("SSH OK" if ssh_ok else "SSH FAILED")

    print_section("PORT CHECK")
    port_ok = check_port(args.host, args.port)
    print(f"PORT {args.port} OK" if port_ok else f"PORT {args.port} FAILED")

    print_section("LISTENER CHECK")
    netstat_ok = check_netstat()
    print("NETSTAT/SS OK" if netstat_ok else "NETSTAT/SS FAILED")

    print_section("DISK CHECK")
    disk_ok = check_disk()
    print("DISK OK" if disk_ok else "DISK USAGE HIGH")

    all_ok = ping_ok and http_ok and ssh_ok and port_ok and netstat_ok and disk_ok
    print_section("SUMMARY")
    print("ALL CHECKS PASSED" if all_ok else "SOME CHECKS FAILED")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
