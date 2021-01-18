"""
Rewrite your pay computation program (previus chapter) with time-and-a-half for overtime
and create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

Hours = int(input("Hours : "))
Rate = int(input("Rate : "))


def computepay(hours, rate):
    if hours >= 40:
        return (hours * rate) + ((hours - 40) * (rate * 0.5))
    else:
        return hours * rate


print("Pay : ", computepay(Hours, Rate))
