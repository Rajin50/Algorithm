# -*- coding: utf-8 -*-
"""CSE221_Lab-05_Task_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-tV0pD5bMKwKfMNcKQdLCHbWTy-qaXQs
"""

#Task- 02
file = open('input2_3.txt', 'r')
output_file = open('output2_3.txt','w')

N, M = map(int, file.readline().split())
course =[]
for i in range(M):
  course.append(tuple(map(int, file.readline().split())))

def lexicographically_smallest_sequence(N, prerequisites):
  graph = {i: [] for i in range(1, N + 1)}
  in_degree = {i: 0 for i in range(1, N + 1)}

  for a, b in prerequisites:
    graph[a].append(b)
    in_degree[b] += 1

  stack = []
  for v, deg in in_degree.items():
    if deg == 0:
      stack.append(v)

  sort = []
  while stack:
    stack.sort()
    vtx = stack.pop(0)
    sort.append(vtx)

    for adj in graph[vtx]:
      in_degree[adj] -= 1
      if in_degree[adj] == 0:
        stack.append(adj)

  if len(sort) != N:
    return "IMPOSSIBLE"

  return sort

course_order = lexicographically_smallest_sequence(N, course)

if course_order == "IMPOSSIBLE":
  output_file.write("IMPOSSIBLE")
else:
  for r in course_order:
    output_file.write(str(r) + " ")

file.close()
output_file.close()