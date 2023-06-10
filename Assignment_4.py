## Python Assignment 4

### 1. Write a Python Program to Find the Factorial of a Number?
number = int(input("Enter a number: "))

factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is", factorial)

### 2. Write a Python Program to Display the multiplication Table?
number = int(input("Enter a number: "))

print("Multiplication Table for", number)

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

### 3. Write a Python Program to Print the Fibonacci sequence?
terms = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci sequence
first_term = 0
second_term = 1

# Print the first two terms
print("Fibonacci sequence:")
print(first_term)
print(second_term)

# Generate the remaining terms
for i in range(2, terms):
    next_term = first_term + second_term
    print(next_term)
    # Update the values of the previous two terms
    first_term = second_term
    second_term = next_term

### 4. Write a Python Program to Check Armstrong Number?
number = int(input("Enter a number: "))

# Convert the number to a string to calculate the number of digits
num_str = str(number)

# Calculate the number of digits
num_digits = len(num_str)

# Initialize the sum
armstrong_sum = 0

# Calculate the sum of the cubes of each digit
for digit in num_str:
    armstrong_sum += int(digit) ** num_digits

# Check if the number is an Armstrong number
if number == armstrong_sum:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

### 5. Write a Python Program to Find Armstrong Number in an Interval?
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for number in range(lower, upper + 1):
    # Convert the number to a string to calculate the number of digits
    num_str = str(number)

    # Calculate the number of digits
    num_digits = len(num_str)

    # Initialize the sum
    armstrong_sum = 0

    # Calculate the sum of the cubes of each digit
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits

    # Check if the number is an Armstrong number
    if number == armstrong_sum:
        print(number)

### 6. Write a Python Program to Find the Sum of Natural Numbers?
n = int(input("Enter a positive integer: "))

# Check if n is a positive integer
if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_numbers = (n * (n + 1)) // 2
    print("The sum of natural numbers up to", n, "is", sum_of_numbers)
