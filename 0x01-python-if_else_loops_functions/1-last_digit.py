#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10
print(f"Last digit of {number:d} is {last_digit:d} and is", end=" ")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
