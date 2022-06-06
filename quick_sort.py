# an array of random integers
import random

arr = [random.randint(0, 100) for i in range(10)]

# print the array
print(arr)

# sort the array
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


narr = quick_sort(arr)

print(narr)
