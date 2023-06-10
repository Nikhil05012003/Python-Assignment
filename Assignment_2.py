#Python Assignment 2
# 1. Write a Python program to convert kilometers to miles?

kilometers = float(input("Enter the distance in kilometers: "))

# Conversion factor for kilometers to miles
conversion_factor = 0.621371

# Calculate the equivalent miles
miles = kilometers * conversion_factor

print("The distance in miles is:", miles)

### 2.Write a Python program to convert Celsius to Fahrenheit?

Celsius = float(input("Enter the temperature in Celsius: "))

# Conversion formula from Celsius to Fahrenheit
Fahrenheit = (Celsius * 9/5) + 32

print("The temperature in Fahrenheit is:", Fahrenheit)

# 3. Write a Python program to display calendar?

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Display the calendar
print(calendar.month(year, month))

### 4. Write a Python program to solve quadratic equation?

import math

# Prompt the user to enter the coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of the roots
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print("The root is:", root)
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("Root 1 =", real_part, "+", imaginary_part, "i")
    print("Root 2 =", real_part, "-", imaginary_part, "i")

# 5. Write a Python program to swap two variables without temp variable?

x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

# Print the original values
print("Before swapping:")
print("x =", x)
print("y =", y)

# Swap the values without a temporary variable
x, y = y, x

# Print the swapped values
print("After swapping:")
print("x =", x)
print("y =", y)
