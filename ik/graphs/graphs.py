from collections import deque

# tab change

class Graph(object):

	def __init__(self, n):
		self.g = [[] for _ in range(n)]
		self.visited =[0]*n
		self.parents = [-1]*n
		self.distance = [0]*n  # distance from start node

	def add_edge(self, u, v):
		self.g[u].append(v)

	def build(self, arr):
		for u,v in arr:
			self.add_edge(u,v)
			self.add_edge(v,u) # needed for undirected graph

	def bfs(self, source):
		q = deque()
		q.append(source)
		self.visited[source] = 1

		while q:
			c = q.popleft()
			for e in self.g[c]:
				if not self.visited[e]:
					self.parents[e] = c
					self.visited[e] = 1
					q.append(e)

	def dfs(self, node):
		self.visited[node] = 1
		for e in self.g[node]:
			if not self.visited[e]:
				self.parents[e] = node
				self.dfs(e)

	def connected_components(self):
		components = 0
		n = len(self.g)
		for i in range(n):
			if not self.visited[i]:
				#self.bfs(i)
				self.dfs(i)
				components += 1

		return components


edge_list = [[0,1], [1,2], [3,2]]
g = Graph(5)
g.build(edge_list)
print g.g
print g.connected_components()
print g.parents

#print g.visited


4
cat
hat
bad
had
bat
had

3
cccw
accc
accw
cccc
cccc

001
000
000
