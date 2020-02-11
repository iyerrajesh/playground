def build(inp, n):
	g = dict()
	for i in range(n):
		g[i] = []

	for u,v in inp:
		g[u].append(v)
	return g


def dfs(g, n, e, path):
	
	if not visited[e]:
		visited[e] = 1
		path = path + [e]
		for c in g[e]:
			dfs(g,n,c,path)
	else:
		if e in path:
			print ('cycle')
	#print (path)


def walk(inp, n):
	g = build(inp, n)

	p = []
	st = 0
	dfs(g, n, st, p)

	#print (g)
	#print (p)


n = 4

visited = [0 for i in range(n)]
parents = [0 for i in range(n)]
inp = [(0,1), (1,0), (0,2), (2,3)]
walk(inp, n)

