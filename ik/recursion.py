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


def has_conflict(board, i, j, n):

	if board[i] != -1:
		return True
	if j in board:
		return True

	x = i-1
	ic = 1
	while x >= 0 and j-ic >= 0:
		if board[x] == j-ic:
			return True
		x -= 1
		ic += 1

	x = i-1
	ic = 1
	while x >= 0 and j+ic < n:
		if board[x] == j+ic:
			return True
		x -= 1
		ic += 1

	return False


def n_queens(n, b):

	def helper(nn, board, i):
		if i == nn:
			print board
			return

		for j in range(nn):
			if not has_conflict(board, i, j, nn):
				b1 = board[:]
				b1[i] = j
				helper(nn, b1, i+1)

	helper(n, b, 0)


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

b = [-1, -1, -1,-1]
n_queens(4, b)
# print has_conflict(b, 2, 0, 4)


def calc(s):
	num = 0
	pre_op = '+'
	s += '+'
	stack = []
	for c in s:
		if c.isdigit():
			num = num * 10 + int(c)
		elif c == ' ':
			pass
		else:
			if pre_op == '+':
				stack.append(num)
			elif pre_op == '*':
				operant = stack.pop()
				stack.append((operant * num))
			num = 0
			pre_op = c
	return sum(stack)


def generate_all_expressions(s, target):

	def eval_helper (slate, i, o):

		res = calc(slate)
		if i == len(s):
			if target == res:
				o.append(slate)
			return o

		# if res > target:
		# 	return o

		eval_helper(slate+s[i], i+1, o)
		eval_helper(slate+'+'+s[i], i+1, o)
		eval_helper(slate+'*'+s[i], i+1, o)
		return o

	out = []
	return eval_helper(s[0], 1, out)


# g =  generate_all_expressions("050505", 5)
# print len(g)
# print g
