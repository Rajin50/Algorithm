# -*- coding: utf-8 -*-
"""CSE221_Task-06_Lab-03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mxj1_213HOU6hwiLG4bqnvRJVjXAHTss
"""

#Task- 06
file = open("input6.txt", "r")

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]

  return i + 1

def Kth_smallest_value(arr, low, high, k):
  if low <= high:
    pivot = partition(arr, low, high)

  if pivot == k:
    return arr[pivot]

  elif pivot > k:
    return Kth_smallest_value(arr, low, pivot - 1, k)

  else:
    return Kth_smallest_value(arr, pivot + 1, high, k)

N = int(file.readline())
arr = list(map(int, file.readline().split()))
Q = int(file.readline())

output_file = open("output6.txt", "a")
for i in range(Q):
  value = int(file.readline())
  kth_smallest = Kth_smallest_value(arr, 0, N - 1, value - 1)
  output_file.write(f"{kth_smallest} \n")

file.close()
output_file.close()