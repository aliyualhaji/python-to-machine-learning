#!/usr/bin/python
"""A module that explain Match statement"""

day = "Sunday"

match day:
    case "Monday":
        print("First day of the Week")
    case "Tuesday":
        print("Second day of the week")
    case "Wednesday":
        print("Third day of the week")
    case "Thursday":
        print("Fourth day of the week")
    case "Friday":
        print("Fifth day of the week")
    case _:
        print("week ends")