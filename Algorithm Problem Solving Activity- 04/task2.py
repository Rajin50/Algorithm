# -*- coding: utf-8 -*-
"""CSE221_Lab-04_Task-02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13S2TZDQwUUOiCsY8g3kg8KQpwsiCs7Ui
"""

#Task- 02
file = open("input2_4.txt", "r")
output_file = open("output2_4.txt", "a")
N, M = map(int, file.readline().split())
Adj_list = {}
for j in range(1, N+1):
  Adj_list[j] = []

for k in range(M):
  u, v = map(int, file.readline().split())
  Adj_list[u].append(v)
  Adj_list[v].append(u)

def BFS(G, s):
  visited = []
  queue = [s]
  path = []

  while queue:
    city = queue.pop(0)
    if city not in visited:
      visited.append(city)
      path.append(city)

      for i in G[city]:
        if i not in visited:
          queue.append(i)

  return path

bfs_path = BFS(Adj_list, 1)

output_file.write(" ".join(map(str, bfs_path)))

file.close()
output_file.close()