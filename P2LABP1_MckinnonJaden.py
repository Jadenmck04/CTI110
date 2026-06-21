# Jaden McKinnon
# 06/21/2026
# P4LAB1_CircleCalculations
# This program calculates the diameter, circumference,
# and area of a circle based on a user-entered radius.

import math

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display results with required formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")