# -*- coding: utf-8 -*-
"""CSE221_Task-02_Lab-03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q5svn_J3auPqHWZQ3FwrOudy4WCKp3KJ
"""

#Task- 02
file = open("input2.txt", "r")

def max_finder(arr, low, high):
  if low == high:
    return arr[low]

  mid = (low + high) // 2

  left_max = max_finder(arr, low, mid)
  right_max = max_finder(arr, mid + 1, high)

  return max(left_max, right_max)

N = int(file.readline())
arr = list(map(int, file.readline().split()))
max_value = max_finder(arr, 0, N - 1)

output_file = open("output2.txt", "a")
output_file.write(str(max_value))

file.close()
output_file.close()