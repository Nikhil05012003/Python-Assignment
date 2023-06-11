# Python Assignment 8
### 1. Write a Python Program to Add Two Matrices?
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    columns = len(matrix1[0])

    # Initialize a result matrix with zeros
    result = [[0 for _ in range(columns)] for _ in range(rows)]

    # Add corresponding elements from the two matrices
    for i in range(rows):
        for j in range(columns):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# Test the function
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = add_matrices(matrix1, matrix2)
print("Resultant matrix:")
for row in result:
    print(row)

### 2. Write a Python Program to Multiply Two Matrices?
def multiply_matrices(matrixa, matrixb):
    rows1 = len(matrixa)
    columns1 = len(matrixa[0])
    rows2 = len(matrixb)
    columns2 = len(matrixb[0])

    if columns1 != rows2:
        print("Error: The number of columns in the first matrix should be equal to the number of rows in the second matrix.")
        return None

    # Initialize a result matrix with zeros
    result = [[0 for _ in range(columns2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(columns2):
            for k in range(columns1):
                result[i][j] += matrixa[i][k] * matrixb[k][j]

    return result

# Test the function
matrixa = [[1, 2],
           [3, 4]]

matrixb = [[5, 6],
           [7, 8]]

result = multiply_matrices(matrixa, matrixb)
print("Resultant matrix:")
for row in result:
    print(row)

### 3. Write a Python Program to Transpose a Matrix?
def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    # Initialize a new matrix with transposed dimensions
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

    # Perform matrix transposition
    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Test the function
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in result:
    print(row)


### 4. Write a Python Program to Sort Words in Alphabetic Order?
def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words

# Test the function
word_list = ["banana", "apple", "cherry", "date", "blueberry"]
sorted_words = sort_words(word_list)

print("Original words:", word_list)
print("Words in alphabetical order:", sorted_words)

### 5. Write a Python Program to Remove Punctuation From a String?
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(translator)
    return text_without_punctuation

# Test the function
text = "Hello, world! How are you?"
text_without_punctuation = remove_punctuation(text)

print("Original text:", text)
print("Text without punctuation:", text_without_punctuation)
