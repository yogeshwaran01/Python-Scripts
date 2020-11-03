"""Return the system boot time since the epoch."""
from datetime import timedelta

from psutil import boot_time

if __name__ == "__main__":
    print(f"BOOT TIME: {timedelta(seconds=boot_time())}")
