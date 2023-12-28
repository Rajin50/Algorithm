# -*- coding: utf-8 -*-
"""CSE221_Lab-05_Task_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xN9h8zxgvTo-7u5I9BOsYFRoaaqztVtq
"""

#Task- 03
file = open("input3_1.txt", "r")
output_file = open("output3_1.txt", "w")

N, M = map(int, file.readline().split())

graph = {i: [] for i in range(1, N + 1)}
for i in range(M):
    u, v = map(int, file.readline().split())
    graph[u].append(v)

def DFS_visiting(vtx, G, visited, stack):
  visited[vtx] = True
  for adj in G[vtx]:
    if not visited[adj]:
      DFS_visiting(adj, G, visited, stack)
  stack.append(vtx)

def Reverse_graph(G):
  reverse = {n: [] for n in G}
  for vtx in G:
    for adj in graph[vtx]:
      reverse[adj].append(vtx)
  return reverse

def SCC_DFS(vtx, G, visited, C):
  visited[vtx] = True
  C.append(vtx)
  for adj in G[vtx]:
    if not visited[adj]:
      SCC_DFS(adj, G, visited, C)

def Strongly_Connected(G):
  vertex = len(G)
  visited = [False] * (vertex + 1)
  stack = []
  for vtx in range(1, vertex + 1):
    if not visited[vtx]:
      DFS_visiting(vtx, G, visited, stack)

  rev_graph = Reverse_graph(G)
  visited = [False] * (vertex + 1)
  Components = []

  while stack:
    vtx = stack.pop()
    if not visited[vtx]:
      temp = []
      SCC_DFS(vtx, rev_graph, visited, temp)
      Components.append(temp)

  return Components

SCC = Strongly_Connected(graph)

for i in SCC:
  output_file.write(" ".join(str(vtx) for vtx in i) + "\n")

file.close()
output_file.close()