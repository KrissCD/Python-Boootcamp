import math
import statistics

print("Mean, Median and Standard Deviation")
print("Enter numbers separated by spaces:")
numbers = list(map(int, input().split()))
mean = sum(numbers) / len(numbers)
median = sorted(numbers)[len(numbers) // 2]
stdev = statistics.stdev(numbers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {stdev}")