import psutil
import logging
from datetime import datetime
import time

# Configure logging
LOG_FILE = "system_health.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Threshold values
CPU_THRESHOLD = 80  # Percentage
MEMORY_THRESHOLD = 80  # Percentage
DISK_THRESHOLD = 80  # Percentage
PROCESS_THRESHOLD = 300  # Number of processes

def check_system_health():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")

    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High Memory usage detected: {memory_usage}%")

    # Get disk usage
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        alert(f"High Disk usage detected: {disk_usage.percent}%")

    # Get number of running processes
    processes = len(psutil.pids())
    if processes > PROCESS_THRESHOLD:
        alert(f"High number of running processes: {processes}")

def alert(message):
    # Log to file and print to console
    logging.warning(message)
    print(f"[ALERT] {datetime.now()} - {message}")

def main():
    print("Starting system health monitoring...")
    while True:
        check_system_health()
        time.sleep(10)  # Interval between checks in seconds

if __name__ == "__main__":
    main()
