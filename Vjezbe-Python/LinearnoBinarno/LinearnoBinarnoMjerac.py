import random
import time
import bisect


data = [random.randint(0, 100000) for _ in range(10000)]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def binary_insertion_sort(arr):
    sorted_list = []
    for item in arr:
        pos = bisect.bisect_left(sorted_list, item)
        sorted_list.insert(pos, item)
    return sorted_list

data_linear = data.copy()
start = time.time()
selection_sort(data_linear)
end = time.time()
print(f"Selection sort {end - start:.4f} sekundi")

data_binary = data.copy()
start = time.time()
sorted_binary = binary_insertion_sort(data_binary)
end = time.time()
print(f"Binary insertion sort {end - start:.4f} sekundi")