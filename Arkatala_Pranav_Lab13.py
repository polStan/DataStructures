def sequential_search(arr, target):
    for i in range(len(arr)): # checking if the values are in the range of the length of the array
        if arr[i] == target: # If the element is equal to the target element, the element at that index is returned
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        i = (left + right) // 2 # Will check at the middle of the arr

        if arr[i] == target: # If the middle element is equal to the target value , then the middle element is returned
            return i
        elif arr[i] < target: # If the middle element is less than the target value that is being search, the left element is moved to the right by 1 position 
            left = i + 1
        else:
            right = i - 1
    return -1

def bubble_sort(arr):
    n = len(arr)
    # Traversing through all the array elements
    for i in range(n):
        # Last i elements are sorted
        for j in range(0, n - i - 1):
            # Swaps if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):  # will check for each element if it is in the range of 1 and length of the array
        key = arr[i] # element at index i becomes key
        j = i - 1 
        while j >= 0 and key < arr[j]: #  Comparing the elements at the sorted and unsorted part and putting it in the right position.
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n): # Checking for each element i in the array 
        min_index = i 
        for j in range(i + 1, n): # checking for each element j that is in the range from minimum index to the right of one to the whole length of the array
            if arr[j] < arr[min_index]: # Checking if the element stored at j us less that the element stored at 
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) <= 1: # checking if the kength of the array does not exceed 1
        return arr # 

    mid = len(arr) // 2 # Finds the middle element in the array
    leftHalf = arr[:mid] # left half of the elements will be stored 
    rightHalf = arr[mid:] # right half of the elements will be stored 

    sortedLeft = merge_sort(leftHalf) # recursively calling the left half so that it is sorted
    sortedRight = merge_sort(rightHalf) # Recursively calling the right half so that it is sorted

    return merge(sortedLeft, sortedRight) # Will return the elements that are merged

def merge(left, right):
    result = [] # The merged elements are appended to the array 
    i = j = 0 # Initially zero

    while i < len(left) and j < len(right): # while the element at i is less than the len of the left half and the element at j is less than the len of the right haf
        if left[i] < right[j]: #If loop to compare if the element at i and is less than the element at j 
            result.append(left[i]) 
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # will extend all the elements at the left half of i
    result.extend(right[j:]) # Will extend all the element at the right half of j 

    return result # All the elements from the left half and right half will be returned

def quick_sort(arr):
    if len(arr) < 2: # when the array length is 1 , it just returns the array
        return arr
    else:
        pivot = arr[0] # Making 1st element in the array as the pivot
        less = [i for i in arr[1:] if i <= pivot] # If the number is less than or equal to the pivot, then we will move the pointer to that location
        greater = [i for i in arr[1:] if i > pivot] # If the number is greater than the pivot, then we will move the pointer to that location
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
arr = [3, 7, 2, 9, 5]
target = 2
result = sequential_search(arr, target)
print("Sequential search:")
if result != -1:
    print("Value", target, "Found at index", result, "in the array ", arr )

else:
    print("Value", target, "not found in", arr)
print("\n")

myarray = [1, 3, 5, 6, 7, 8, 9, 10]
mytarget = 8
result = binary_search(myarray, mytarget)
print("Binary search:")
if result != -1:
    print("Value", mytarget, "found at index", result, "in the array", myarray)
else:
    print("Target not found in ", myarray)
print("\n")

arr = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print("Before bubble Sort:", arr)
result = bubble_sort(arr)
print("After bubble Sort:", result)
print("\n")

B = [-5, 3, 2, 1, -10, -1, 7, 2, 2]
print("Before insertion sort:", B)
insertion_sort(B)
print("After insertion sort:", B)
print("\n")

C = [-5, 3, 2, 1, -10, -1, 7, 2, 2]
print("Before selection sort:", C)
result = selection_sort(C)
print("After selection sort:", result)
print("\n")

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
print("Before merge sort:", unsortedArr)
sortedArr = merge_sort(unsortedArr)
print("Sorted array after merge sort: ", sortedArr)
print("\n")

myarray = [-5, 3, 2, 1, -10, -1, 7, 2, 2]
print("Before quick sort:", myarray)
result = quick_sort(myarray)
print("Sorted array after quick sort:", result)


