from collections import defaultdict, deque


class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		def build(inp):
			g = defaultdict(list)
			for u,v in inp:
				g[v].append(u)
			return g

		# Directed graph has cycle ?
		# use rec_stack to track visits in the current recursion
		# just relying on visited will not work.
		def dfs_cycle(g, e, visited, rec_stack):
			visited[e] = 1
			rec_stack[e] = 1
			for c in g[e]:
				if visited[c] == 0:
					if dfs_cycle(g,c, visited, rec_stack):
						return True
				if visited[c] == 1:
					if rec_stack[c] == 1:
						return True
			rec_stack[e] = 0
			visited[e] = 2
			return False

		n = numCourses
		visited = [0 for i in range(n)]
		rec_stack = [0 for i in range(n)]
		g = build(prerequisites)
		in_degree = [0 for i in range(n)]

		for v,e in g.items():
			for x in e:
				in_degree[x] += 1

		for i in range(n):
			if visited[i] == 0:
				if dfs_cycle(g, i, visited, rec_stack):
					return [-1]

		def topo_sort(in_d, g):
			path = []
			q = deque()
			for i in range(n):
				if in_d[i] == 0:
					q.appendleft(i)

			while q:
				e = q.pop()
				path.append(e)
				for c in g[e]:
					in_d[c] -= 1
					if in_d[c] == 0:
						q.appendleft(c)

			if len(path) != n:
				return [-1]
			return path

		return topo_sort(in_degree, g)


n = 4
# inp = [(0,1), (1,3),  (1,2), (2,3)]
inp = [(1,0), (2,0), (3,1), (3,2)]

s = Solution()
print (s.canFinish(4, inp))



