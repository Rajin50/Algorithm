# -*- coding: utf-8 -*-
"""CSE221_Lab-06_Task-01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zHQTmFDp7hdiLYP0A4aNdD-ZUEI4ikm5
"""

#Task- 01
file = open("input1_2.txt", "r")
output_file = open('output1_2.txt','w')
N, M = map(int, file.readline().split())
graph = {i: [] for i in range(1, N + 1)}

for i in range(M):
    u, v, w = map(int, file.readline().split())
    graph[u].append((v, w))

s = int(file.readline())

def dijkstra(graph, s):
  distances = {node: float('inf') for node in graph}
  distances[s] = 0

  visit = [(0, s)]
  while visit:
    D, vtx = min(visit)
    visit.remove((D, vtx))

    for adj, weight in graph[vtx]:
      distance = D + weight
      if distance < distances[adj]:
        distances[adj] = distance
        visit.append((distance, adj))

  return distances

Dist = dijkstra(graph, s)

for i in range(1, N+1):
  if Dist[i] == float('inf'):
    output_file.write(str(-1) + " ")
  elif Dist[i] != 0:
    output_file.write(str(Dist[i]) + " ")

file.close()
output_file.close()