array = [42, 10, 78, 54, 23, 7, 85, 92, 31, 67]

# Bubble sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Bogo sort
import random
def is_sorted(array):
    return all(array[i] <= array[i+1] for i in range(len(array)-1))

def bogo_sort(array):
    while not is_sorted(array):
        random.shuffle(array)
    return array

# Selection sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

# Insertion sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print("Základní pole:", array)
print("Bubble sort:", bubble_sort(array.copy()))
print("Bogo sort:", bogo_sort(array.copy()))
print("Selection sort:", selection_sort(array.copy()))
print("Insertion sort:", insertion_sort(array.copy()))