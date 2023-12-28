# -*- coding: utf-8 -*-
"""CSE221_Lab-04_Task-04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19QDd1Q4M091gAcFIFPc2_LNYIQe3IGId
"""

#Task- 04
file = open("input4_5.txt", "r")
output_file = open("output4_5.txt", "a")
N, M = map(int, file.readline().split())
Adj_list = {}
for j in range(1, N+1):
  Adj_list[j] = []

for k in range(M):
  u, v = map(int, file.readline().split())
  Adj_list[u].append(v)

def find_cycle(graph, visited, stack, V):
  visited[V] = True
  stack[V] = True

  for i in graph[V]:
    if not visited[i]:
      recursive_call = find_cycle(graph, visited, stack, i)
      if recursive_call == True:
        return True
    elif stack[i]:
      return True

  stack[V] = False

  return False

def is_cyclic(graph, n):
  visited = [False] * (n + 1)
  stack = [False] * (n + 1)

  for r in range(1, n + 1):
    if not visited[r]:
      cycle = find_cycle(graph, visited, stack, r)
      if cycle == True:
        return True

  return False

R = is_cyclic(Adj_list, N)
if R == True:
  output_file.write("YES")
else:
  output_file.write("NO")

file.close()
output_file.close()