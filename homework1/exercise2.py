"""
Exercise 2
Import the math module in whatever way you prefer. Call its sqrt function on the number 13689 and print that value to the console.
"""

from math import sqrt
from os import system


def clear():
    system('cls')


defaultNumber = 13689
answer = input(
    "Enter 'yes' if you want to continue with the default value '13689'.\n"
    "If you want to enter your own value, enter 'no'.\nAnswer : ").lower()


def read(value):
    if value == "yes":
        result = sqrt(defaultNumber)
    elif value == "no":
        clear()
        myNumber = input("Please enter your number ?\nAnsver : ")
        result = sqrt(int(myNumber))
    else:
        return "We encountered an unexpected error"
    return result


print(read(answer))
