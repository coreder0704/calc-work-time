from datetime import timedelta
import sys

start_base = timedelta(hours=8, minutes=45)
end_base = timedelta(hours=17, minutes=30)


def translate_timeformat(time: str) -> timedelta:
    hours: int
    minutes: int
    try:
        hours, minutes = list(map(int, time.split(":")))
    except ValueError:
        sys.exit("Error: Non-numeric string for time.")
    return timedelta(hours=hours, minutes=minutes)


def calc_overtime(start: str, end: str) -> str:
    return "0:15"
