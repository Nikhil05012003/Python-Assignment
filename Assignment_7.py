## Python Assignment 7
### 1. Write a Python Program to find sum of array?
def array_sum(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

# Test the function
array = [1, 2, 3, 4, 5]
result = array_sum(array)
print("Sum of the array:", result)

### 2. Write a Python Program to find largest element in an array?
def find_largest_element(arr):
    if len(arr) == 0:
        return None

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Test the function
array = [5, 2, 8, 10, 3]
result = find_largest_element(array)
print("Largest element in the array:", result)

### 3. Write a Python Program for array rotation?
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Normalize rotation amount to handle larger values of k

    rotated_arr = arr[k:] + arr[:k]
    return rotated_arr

# Test the function
array = [1, 2, 3, 4, 5]
rotation_amount = 2
result = rotate_array(array, rotation_amount)
print("Original array:", array)
print("Rotated array:", result)

### 4. Write a Python Program to Split the array and add the first part to the end?
def split_and_add(arr, k):
    n = len(arr)
    k = k % n  # Normalize split position to handle larger values of k

    split_arr = arr[k:] + arr[:k]
    return split_arr

# Test the function
array = [1, 2, 3, 4, 5]
split_position = 2
result = split_and_add(array, split_position)
print("Original array:", array)
print("Split and added array:", result)

### 5. Write a Python Program to check if given array is Monotonic?
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            increasing = False
        if arr[i] > arr[i-1]:
            decreasing = False

    return increasing or decreasing

# Test the function
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 2, 2, 3, 4, 5]
array4 = [1, 1, 1, 1, 1]

print("Array1 is monotonic:", is_monotonic(array1))
print("Array2 is monotonic:", is_monotonic(array2))
print("Array3 is monotonic:", is_monotonic(array3))
print("Array4 is monotonic:", is_monotonic(array4))
