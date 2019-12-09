def permhelper(slate, array, perms):
	if not array:
		perms.append(slate)
	else:
		for i in range(len(array)):
			permhelper(slate+array[i], array[:i]+array[i+1:],perms)
	return perms


def perms(c):
	p = []
	print permhelper("", c, p)


perms('abc')


def subset_tgt (array, tgt):

	def helper (inp_sum, j, tgt):

		if inp_sum == tgt:
			return 1
		elif j == len(array):
			return 0
		elif inp_sum > tgt:
			return 0

		return helper (inp_sum+array[j], j+1, tgt) + helper(inp_sum, j+1, tgt)

	return helper (0,0,3)


a = [1,2,3]
print subset_tgt(a, 3)


def climbing_stairs(n, a):

	def helper(n, a):

		if n == 0:
			return 1

		if n < 0:
			return 0

		s = 0
		for i in a:
			s += helper(n-i, a)

		return s

	return helper(n, a)


a = [1,2]
print climbing_stairs(5, a)


def n_queens(n, board):

	def helper(n, board, i):
		if n == 0:
			print board
			return

		for j in range(n):
			if j not in board and board[i] == 0:
				board[i] = j
				helper (n-1, board, i+1)
			else:
				return

	helper (n, board, 0)


def subsets(s):

	def subset_helper(slate, i, p):
		if i == len(s):
			p.append(slate)
		else:
			subset_helper(slate, i+1,p)
			subset_helper(slate+s[i], i+1, p)
		return p

	s_sets = []
	return subset_helper("",0,s_sets)


s = "xy"
print subsets(s)