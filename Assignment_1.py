# Python Assignment 1
### 1. Write a Python program to print "Hello Python"?
print("Hello Python")

### 2. Write a Python program to do arithmetical operations addition and division.?
def addition(a, b):
    return a + b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Test the functions
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", addition(num1, num2))
print("Division:", division(num1, num2))

### 3. Write a Python program to find the area of a triangle?
base = float(input("Enter the length of the base of triangle: "))
height = float(input("Enter the height of triangle: "))

area = 0.5 * base * height

print("The area of the triangle is:", area)

### 4. Write a Python program to swap two variables?
# Input the values of the variables
c = input("Enter the value of c: ")
d = input("Enter the value of d: ")

# Print the original values
print("Before swapping:")
print("c =", c)
print("d =", d)

# Swap the values using a temporary variable
temp = c
c = d
d = temp

# Print the swapped values
print("After swapping:")
print("c =", c)
print("d =", d)

### 5. Write a Python program to generate a random number?
import random

# Generate a random number between 1 and 50
random_number = random.randint(1,50)

print("Random number:", random_number)



