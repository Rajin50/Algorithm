# -*- coding: utf-8 -*-
"""CSE221_Lab-01_Task-01(a).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PwwyrVW1BTkPN-7xE2wb_0G7Il9vvopr
"""

#Task- 01 a
file = open("input1a.txt", "r")
T = int(file.readline())
nums = file.readlines()

output_file = open("output1a.txt", "a")

for i in range(T):
  if int(nums[i]) % 2 == 0:
    output_file.write(f"{int(nums[i])} is an even number.\n")
  else:
    output_file.write(f"{int(nums[i])} is an odd number.\n")

file.close()
output_file.close()