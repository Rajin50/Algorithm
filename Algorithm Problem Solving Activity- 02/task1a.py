# -*- coding: utf-8 -*-
"""CSE221_Lab-02_Task-01(a).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hei0p6C3U8FzDqhPvuQx2vMlgbULRUTA
"""

#Task- 01 a
file = open("input1a.txt", "r")
T = file.readline()
L = file.readline()

TL = T.split()
N = int(TL[0])
S = int(TL[1])
int_list = list(map(int, L.split()))

output_file = open("output1a.txt", "a")
for i in range(N):
  flag = False
  for j in range(1, N):
    if int_list[i] + int_list[j] == S:
      output_file.write(f"{i+1} {j+1}")
      flag = True
      break
  if flag == True:
    break
if flag == False:
  output_file.write("Impossible")

file.close()
output_file.close()