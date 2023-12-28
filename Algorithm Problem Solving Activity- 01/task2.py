# -*- coding: utf-8 -*-
"""CSE221_Lab-01_Task-02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Snq7U4xG3LaB6vWK0FtFXhl7rLB1NN0
"""

#Task- 02
def bubbleSort(arr):
    flag = False
    for idx in range(len(arr)-1):
        if arr[idx]>arr[idx+1]:
            flag = True
            break

    if flag == True:
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

file = open("input2.txt","r")
output_file = open("output2.txt","a")

num_of_elements = int(file.readline())
arr = list(map(int, file.readline().split()))
sorted_arr = bubbleSort(arr)

for i in range(0, num_of_elements):
  output_file.write(str(sorted_arr[i]) + " ")

file.close()
output_file.close()