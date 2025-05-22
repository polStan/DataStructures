import timeit
import random 
import sys



arr = []
while True:

    np = input("\nPlease enter the size of array: ")
    if np == "quit":
        break
    n = int(np)
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 100))
    start_time = timeit.default_timer()
    result = sum(arr)
    end_time = timeit.default_timer()

    array_size = sys.getsizeof(arr)
    print(f"Array size: {n}")
    print(f"Sum of array elements: {result}")
    print(f"Execution time: {end_time - start_time:.20f} seconds")
    print(f"Memory used by Array: {array_size} bytes")


def generating_the_matrix(n):
    arr1 = []

    for i in range(n):
        arr2 = []
        for j in range(n):
            arr2.append(random.randint(1, 10))
        arr1.append(arr2)
    return arr1
            
def matrix_sum(A, B, n):
    result = []
    for i in range(n):
        arr2 = []
        for j in range(n):
            arr2.append(0)
        result.append(arr2)
    
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

def get_memory_size(matrix):
    return sys.getsizeof(matrix) + sum(sys.getsizeof(row) for row in matrix)


arr = []
while True:
    np = input("\nPlease enter the size of the matrix: ")
    if np == "quit":
        break
    n = int(np)
    A = generating_the_matrix(n)
    B = generating_the_matrix(n)
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 100))
    start_time = timeit.default_timer()
    result = matrix_sum(A, B, n)
    end_time = timeit.default_timer()
    matrix_size_A = get_memory_size(A)
    matrix_size_B = get_memory_size(B)
    matrix_size_result = get_memory_size(result)


    print(f"Matrix size is : {n} x {n}")
    print(f"Execution time is : {end_time - start_time:.20f} seconds")
    print(f"Memory used by Matrix A is: {matrix_size_A} bytes")
    print(f"Memory used by Matrix B is : {matrix_size_B} bytes")
    print(f"Memory used by Result Matrix is : {matrix_size_result} bytes")
