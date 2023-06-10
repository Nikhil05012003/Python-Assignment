## Python Assignment 3
### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

### 2. Write a Python Program to Check if a Number is Odd or Even?
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

### 3. Write a Python Program to Check Leap Year?
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

### 4. Write a Python Program to Check Prime Number?
number = int(input("Enter a number: "))

# Prime numbers are greater than 1
if number > 1:
    # Check for factors
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is not a prime number.")
    
### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for number in range(lower , upper + 1):
    # Prime numbers are greater than 1
    if number > 1:
        # Check for factors
        for i in range(2, int(number/2) + 1):
            if number % i == 0:
                break
        else:
            print(number)



