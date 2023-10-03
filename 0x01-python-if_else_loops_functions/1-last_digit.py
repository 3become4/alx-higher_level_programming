#!/usr/bin/python3
import random
x = random.randint(-10000, 10000)
y = abs(x) % 10
if x < 0:
	y = -y
print("Last digit of {} is {} and is ".format(x, y), end="")
if y > 5:
	print("greater than 5")
elif y == 0:
	print("0")
else:
	print("less than 6 and not 0")
