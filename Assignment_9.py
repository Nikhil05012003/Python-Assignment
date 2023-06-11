## Python Assignment 9
### 1. Write a Python program to check if the given number is a Disarium Number?
def disarium_number(number):
    str_number = str(number)
    length = len(str_number)
    disarium_sum = 0

    for i in range(length):
        disarium_sum += int(str_number[i]) ** (i + 1)

    return disarium_sum == number

# Test the function
number = int(input("Enter a number: "))
if disarium_number(number):
    print(number, "is a Disarium number.")
else:
    print(number, "is not a Disarium number.")
    
### 2. Write a Python program to print all disarium numbers between 1 to 100?
def is_disarium_number(number):
    str_number = str(number)
    length = len(str_number)
    disarium_sum = 0

    for i in range(length):
        disarium_sum += int(str_number[i]) ** (i + 1)

    return disarium_sum == number


print("Disarium numbers between 1 and 100:")

for i in range(1, 101):
    if is_disarium_number(i):
        print(i)
        
### 3. Write a Python program to check if the given number is Happy Number?
def happy_number(number):
    seen_numbers = set()
    while True:
        if number == 1:
            return True
        elif number in seen_numbers:
            return False
        seen_numbers.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))

# Test the function
number = int(input("Enter a number: "))
if happy_number(number):
    print(number, "is a Happy number.")
else:
    print(number, "is not a Happy number.")
    
### 4. Write a Python program to print all happy numbers between 1 and 100?
def is_happy_number(number):
    seen_numbers = set()
    while True:
        if number == 1:
            return True
        elif number in seen_numbers:
            return False
        seen_numbers.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))

print("Happy numbers between 1 and 100:")

for i in range(1, 101):
    if is_happy_number(i):
        print(i)
        
### 5. Write a Python program to determine whether the given number is a Harshad Number?
def is_harshad_number(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return number % digit_sum == 0

# Test the function
number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(number, "is a Harshad number.")
else:
    print(number, "is not a Harshad number.")
    
### 6. Write a Python program to print all pronic numbers between 1 and 100?
def is_pronic_number(number):
    sqrt = int(number ** 0.5)
    return sqrt * (sqrt + 1) == number

print("Pronic numbers between 1 and 100:")

for i in range(1, 101):
    if is_pronic_number(i):
        print(i)





