import random
import heapq

class Graph:
  def __init__(self, n):
    self.E = [[] for i in range(n)]
  
  def populateGraph(self, E):
    for edge in E:
      self.E[edge[0]].append(edge[1])
      self.E[edge[1]].append(edge[0])

class Graph2:
  def __init__(self, n):
    self.E = []
    self.V = [[] for i in range(n)]
  
  def populateGraph(self, E):
    self.E = E
    for edge in E:
      self.V[edge[0]].append(edge[1])
      self.V[edge[1]].append(edge[0])

def DFS(g, visited, v=None):
  if v == None:
    v = 0
    visited[0] = True
  print(v)
  for e in g.E[v]:
    if not visited[e]:
      visited[e] = True
      DFS(g, visited, e)

def BFS():
  pass

def createEdgeList(n, ct):
  tempEdgeList = set()
  while len(tempEdgeList) < ct:
    v1 = random.randrange(0, n)
    v1eqv2 = True
    while v1eqv2:
      v2 = random.randrange(0, n)
      if v1 != v2:
        v1eqv2 = False
    tempEdgeList.add((v1, v2))
  return list(tempEdgeList)

def kruskal(g):
  vertices = g.V
  Q = []
  for i in range(len(g.V)):
    pass
  for e in g.E:
    heapq.heappush(Q, e)

def main():
  sz = 8
  G = Graph(sz)
  edgeList = createEdgeList(sz, sz*(sz-1))
  G.populateGraph(edgeList)
  visited = [False]*sz
  DFS(G, visited)

if __name__ == '__main__':
  main()