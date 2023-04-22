from datetime import datetime

# day / month / year / hours / minutes
time_format = "%d/%m/%Y/%H:%M"


def getDifference(last_spin_time, actual_time):
    last_spin_time = datetime.strptime(str(last_spin_time), time_format)
    actual_time = datetime.strptime(str(actual_time), time_format)
    difference = actual_time - last_spin_time
    difference_min = difference.total_seconds() // 60
    return difference_min
