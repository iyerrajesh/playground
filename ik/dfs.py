from collections import defaultdict


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
                else:
                    if rec_stack[c] == 1:
                        return True
            rec_stack[e] = 0
            return False

        n = numCourses
        visited = [0 for i in range(n)]
        rec_stack = [0 for i in range(n)]
        g = build(prerequisites)
        #print (g)
        for i in range(n):
            if dfs_cycle(g, i, visited, rec_stack):
                return False
        return True

n = 4
#inp = [(0,1), (1,3),  (1,2), (2,3)]
inp = [(1,0), (3,1), (2,1), (3,2)]

s = Solution()
print (s.canFinish(4, inp))



