
from datetime import timedelta, datetime


def add(moment):

    if not isinstance(moment, datetime):
        raise TypeError("Valid input is datetime")

    gigasecond = 1000000000

    return moment + timedelta(seconds=gigasecond)
    #timedelta - used to add integers to datetime

print(add(["2024, 03, 11"]))

