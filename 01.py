# Aim
# Create a program in Python that calculates the area of a circle, given its radius.

import random
import math

radius = random.randrange(0,99,5)
print(f"Radius of th circle is: {radius}")
area = math.pi * pow(radius,2)
print(f"Area of the circle is: {area}")