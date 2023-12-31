# -*- coding: utf-8 -*-
"""CSE221_Lab-06_Task-04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nfL1qC5tV3y0vWgPOJCctVxhJ8x6XXCD
"""

#Task- 04
file = open("input4_1.txt", "r")
output_file = open('output4_1.txt','w')
N, M = map(int, file.readline().split())
G = []
for i in range(M):
  u, v, w = map(int, file.readline().split())
  G.append((u, v, w))

def minimum_cost(N, M, G):
  def set_finding(x):
    if parent[x] != x:
      parent[x] = set_finding(parent[x])
    return parent[x]

  def set_of_U(x, y):
    rx = set_finding(x)
    ry = set_finding(y)
    if rx != ry:
      parent[rx] = ry

  def kruskal():
    edges.sort(key=lambda x: x[2])
    cost = 0
    for j in edges:
      u, v, w = j
      if set_finding(u) != set_finding(v):
        set_of_U(u, v)
        cost += w
    return cost

  parent = list(range(N + 1))
  edges = G

  return kruskal()

R = minimum_cost(N, M, G)
output_file.write(str(R))

file.close()
output_file.close()