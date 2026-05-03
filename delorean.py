#!/usr/bin/env python3
import sys
import os

from datetime import datetime
import calendar


def subtract_months(dt, months):
    year = dt.year
    month = dt.month - months

    while month <= 0:
        month += 12
        year -= 1

    last_day = calendar.monthrange(year, month)[1]
    day = min(dt.day, last_day)

    return dt.replace(year=year, month=month, day=day)


def set_current_time():
    os.system('timedatectl set-ntp true')
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(formatted)


def set_months_backwards(nums_of_months_back):
    now = datetime.now()
    result = subtract_months(now, nums_of_months_back)
    formatted_timestamp = result.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(formatted_timestamp)
    os.system('timedatectl set-ntp false')
    os.system(f'timedatectl set-time "{formatted_timestamp}"')


def run(param):
    param = int(param)
    if param == 0:
        set_current_time()
    else:
        set_months_backwards(param)


def main():
    if len(sys.argv) == 1:
        print("no args")
    else:
        run(sys.argv[1])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")

