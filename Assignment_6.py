# Python Assignment 6
### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

# Test the function
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence:")
print(fib_sequence)

### 2. Write a Python Program to Find Factorial of Number Using Recursion?
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial:", result)

### 3. Write a Python Program to calculate your Body Mass Index?
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Test the function
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your Body Mass Index (BMI) is:", bmi)

### 4. Write a Python Program to calculate the natural logarithm of any number?
import math

# Take user input
number = float(input("Enter a number: "))

# Calculate natural logarithm
ln = math.log(number)

# Print the result
print("Natural logarithm of", number, "is:", ln)


### 5. Write a Python Program for cube sum of first n natural numbers?
def cube_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum

# Test the function
num = int(input("Enter a number: "))
result = cube_sum(num)
print("Cube sum of the first", num, "natural numbers:", result)
