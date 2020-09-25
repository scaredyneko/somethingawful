import math

print("Please enter the first side of a triangle:")
a = float(input())
print("Please enter the second side of a triangle:")
b = float(input())
print("What is the avalue of the angle between them (in radians)?")
theta = float(input())
print ("And the answer is:", math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(theta)))