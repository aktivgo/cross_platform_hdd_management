import psutil

for disk in psutil.disk_partitions():
    print("Диск: ", disk.device)
    print("Тип: ", disk.opts)
    print("Файловая система: ", disk.fstype)
    p = psutil.disk_usage(disk.mountpoint)
    print("Всего: ", round(p.used / 1024 / 1024 / 1024 + p.free / 1024 / 1024 / 1024, 2), "Gb")
    print("Занято: ", round(p.used / 1024 / 1024 / 1024, 2), "Gb")
    print("Свободно: ", round(p.free / 1024 / 1024 / 1024, 2), "Gb", "\n")
