from collections import deque


def neighbours(grid, i,j, keys):
	m = len(grid)
	n = len(grid[0])
	near = [(i+1, j), (i-1,j), (i,j-1), (i,j+1)]

	out = []
	for x,y in near:
		if 0 <= x < m and 0 <= y < n:
			item = grid[x][y]
			if item == '.':
				out.append((x,y))
			elif item in 'abcdefghij':
				keys.add(item)
				out.append((x,y))
			elif item in 'ABCDEFGHIJ':
				if item.lower() in keys:
					out.append((x,y))
			elif item == '+':
				out.append((x,y))

	return out


def find_shortest_path(grid):
	keys = set()
	m = len(grid)
	n = len(grid[0])
	path = []
	visited = [[0 for _ in range(n)] for _ in range(m)]

	q = deque()
	for i in range(m):
		ix = g[i].find('@')
		if ix != -1:
			si, sj = i,ix

	q.appendleft((si, sj))
	visited[si][sj] = 1

	while q:
		i,j = q.pop()
		if grid[i][j] == '+':
			path.append((i, j))
			break
		for n in neighbours(grid, i, j, keys):
			if not visited[i][j]:
				visited[i][j] = 1
				path.append(i,j)
				q.appendleft(n)

	return path