## Python Assignment 10
### 1. Write a Python program to find sum of elements in list?
def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print("Sum of elements:", result)

### 2. Write a Python program to  Multiply all numbers in the list?
def multiply_numbers(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Test the function
numbers1 = [1, 2, 3, 4, 5]
result1 = multiply_numbers(numbers1)
print("Multiplication of numbers:", result1)

### 3. Write a Python program to find smallest number in a list?
def find_smallest_number(lst):
    if len(lst) == 0:
        return None
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# Test the function
numbers3 = [5, 2, 9, 1, 7]
smallest_number = find_smallest_number(numbers3)
print("Smallest number:", smallest_number)

### 4. Write a Python program to find largest number in a list?
def find_largest_number(lst):
    if len(lst) == 0:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Test the function
numbers4 = [5, 2, 9, 1, 7]
largest_number = find_largest_number(numbers4)
print("Largest number:", largest_number)

### 5. Write a Python program to find second largest number in a list?
def find_second_largest_number(lst):
    if len(lst) < 2:
        return None
    largest = lst[0]
    second_largest = None
    for num in lst[1:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest

# Test the function
numbers5 = [5, 2, 9, 1, 7]
second_largest_number = find_second_largest_number(numbers5)
print("Second largest number:", second_largest_number)

### 6. Write a Python program to find N largest elements from a list?
def find_n_largest_elements(lst, n):
    if n > len(lst) or n <= 0:
        return None
    lst.sort(reverse=True)
    return lst[:n]

# Test the function
numbers6 = [5, 2, 9, 1, 7]
n = 3
n_largest_elements = find_n_largest_elements(numbers6, n)
print(f"{n} largest elements:", n_largest_elements)

### 7. Write a Python program to print even numbers in a list?
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

# Test the function
numbers7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
print_even_numbers(numbers7)

### 8. Write a Python program to print odd numbers in a List?
def print_odd_numbers(lst):
    for num in lst:
        if num % 2 != 0:
            print(num)

# Test the function
numbers8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Odd numbers:")
print_odd_numbers(numbers8)

### 9. Write a Python program to Remove empty List from List?
def remove_empty_lists(lst):
    return [sublist for sublist in lst if sublist]

# Test the function
my_list = [1, [], [2, 3], [], 4, [], [5, 6]]
updated_list = remove_empty_lists(my_list)
print("Updated list:", updated_list)

### 10. Write a Python program to Cloning or Copying a list?
def clone_list(lst):
    return lst.copy()

# Test the function
original_list = [1, 2, 3, 4, 5]
cloned_list = clone_list(original_list)
print("Original list:", original_list)
print("Cloned list:", cloned_list)

### 11. Write a Python program to Count occurrences of an element in a list?
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Test the function
my_list1 = [1, 2, 3, 2, 4, 2, 5, 2]
element_to_count = 2
occurrences = count_occurrences(my_list1, element_to_count)
print("Occurrences of", element_to_count, "in the list:", occurrences)
