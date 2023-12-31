# -*- coding: utf-8 -*-
"""CSE221_Task-01_Lab-03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14U163JYkAonq8oKaZ0pKNbFMJmuc-hRo
"""

#Task- 01
file = open("input1.txt", "r")
N = int(file.readline())
elem = file.readline()
arr = list(map(int, elem.split()))

def merge(a, b):
  i = j = k = 0
  new_arr = []
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      new_arr.append(a[i])
      i += 1

    else:
      new_arr.append(b[j])
      j += 1

    k += 1

  while i < len(a):
    new_arr.append(a[i])
    i += 1
    k += 1

  while j < len(a):
    new_arr.append(b[j])
    j += 1
    k += 1

  return new_arr

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    a = merge_sort(left_half)
    b = merge_sort(right_half)

    return merge(a, b)

R = merge_sort(arr)
output_file = open("output1.txt", "a")
for r in R:
  output_file.write(str(r) + " ")

file.close()
output_file.close()