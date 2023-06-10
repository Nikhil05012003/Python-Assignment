## Python Assignment  5
### 1. Write a Python Program to Find LCM?
def gcd(a, b):
    # Calculate the Greatest Common Divisor (GCD) using Euclid's algorithm
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Calculate the Least Common Multiple (LCM)
    return (a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm_result = lcm(num1, num2)

print("The LCM of", num1, "and", num2, "is", lcm_result)

### 2. Write a Python Program to Find HCF?
def hcf(x, y):
    # Calculate the Highest Common Factor (HCF) using Euclid's algorithm
    while y != 0:
        x, y = y, x % y
    return x

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf_result = hcf(num1, num2)

print("The HCF of", num1, "and", num2, "is", hcf_result)

### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
decimal = int(input("Enter a decimal number: "))

print("Binary:", bin(decimal))
print("Octal:", oct(decimal))
print("Hexadecimal:", hex(decimal))

### 4. Write a Python Program To Find ASCII value of a character?
character = input("Enter a character: ")

ascii_value = ord(character)

print("The ASCII value of", character, "is", ascii_value)

### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 1:
    result = add(num1, num2)
    operation = "+"
elif choice == 2:
    result = subtract(num1, num2)
    operation = "-"
elif choice == 3:
    result = multiply(num1, num2)
    operation = "*"
elif choice == 4:
    result = divide(num1, num2)
    operation = "/"
else:
    print("Invalid choice.")
    exit()

print(num1, operation, num2, "=", result)






