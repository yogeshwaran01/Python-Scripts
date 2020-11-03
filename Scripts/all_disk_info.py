from psutil import disk_partitions, disk_usage
from tabulate import tabulate

"""
Script return DataFrame of the information about all disk in your pc
"""


def convert_bytes_gb(bytes_: int) -> int:
    """
    Function convert bytes to gb
    """
    return round(float(bytes_) / (1024 ** 3))


class DiskInfo:
    """
    Class collects information about Disk
    """

    def __init__(self):
        self.data = disk_partitions(all=True)

    def details(self, device_name: str) -> tuple:
        for i in self.data:
            if i.device == device_name:
                return i

    @property
    def get_device_names(self) -> list:

        return [i.device for i in self.data]

    def disk_info(self, device_name: str) -> str:
        disk_info = {}
        try:
            usage = disk_usage(device_name)
            disk_info["Device"] = device_name
            disk_info["Size"] = f"{convert_bytes_gb(usage.used + usage.free)} GB"
            disk_info["Used"] = f"{convert_bytes_gb(usage.used)} GB"
            disk_info["Free"] = f"{convert_bytes_gb(usage.free)} GB"
            disk_info["Usage"] = f"{usage.percent} %"
        except PermissionError:
            pass
        info = self.details(device_name)
        disk_info.update({"Device": info.device})
        disk_info["Mount Point"] = info.mountpoint
        disk_info["FS-Type"] = info.fstype
        disk_info["Opts"] = info.opts
        return disk_info

    @property
    def all_disk_info(self) -> list:
        return_ = []
        for i in self.get_device_names:
            return_.append(self.disk_info(i))
        return return_


if __name__ == "__main__":
    info = DiskInfo().all_disk_info
    _list = [i.values() for i in info]
    print(tabulate(_list, headers=info[0].keys(), tablefmt="grid", missingval="-"))
