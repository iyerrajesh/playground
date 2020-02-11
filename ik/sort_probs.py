
import random

def intersection (n1, n2):

	l1 = len(n1)
	l2 = len(n2)

	out = []

	i = 0
	j = 0

	while i < l1 and j < l2:

		if n1[i] == n2[j]:
			out.append(n1[i])
			i += 1
			j += 1
		elif n1[i] < n2[j]:
			i += 1
		else:
			j += 1

	return out


def union(n1, n2):
	'''
	use merge sort template for union and intersection
	problems
	for union
	'''
	l1 = len(n1)
	l2 = len(n2)

	i=0
	j=0
	out = []

	while i < l1 and j < l2:
		if n1[i] == n2[j]:
			out.append(n1[i])
			i += 1
			j += 1
		elif n1[i] < n2[j]:
			out.append(n1[i])
			i += 1
		else:
			out.append(n2[j])
			j += 1

	while i < l1:
		out.append(n1[i])
		i += 1

	while j < l2:
		out.append(n2[j])
		j += 1

	return out


def quickselect(nums, k):
	"""

	:type nums: object
	"""
	def helper(nums, start, end):

		if start >= end:
			return nums[end]

		p_i = random.randrange(start,end+1)
		nums[start], nums[p_i] = nums[p_i], nums[start]

		i = start
		j = start+1
		pivot = nums[start]
		while j <= end:
			if nums[j] < pivot:
				i += 1
				nums[i], nums[j] = nums[j], nums[i]
			j += 1

		nums[start], nums[i] = nums[i], nums[start]

		if i == len(nums)-k:
			return nums[i]
		elif i < len(nums)-k:
			return helper(nums, i + 1, end)
		else:
			return helper(nums, start, i-1)

	return helper(nums, 0, len(nums)-1)


#
# Complete the mergeArrays function below.
#
def mergeArrays(arr):
	#
	# Write your code here.
	#
	def comp(n1, n2, order):
		if order == 'asc':
			if n1 < n2:
				return -1
			elif n1 == n2:
				return 0
			else:
				return 1

		if order == 'dsc':
			if n1 > n2:
				return -1
			elif n1 == n2:
				return 0
			else:
				return 1

	def merge(n1, n2, order='asc'):
		out = []
		i = 0
		j = 0
		l1 = len(n1)
		l2 = len(n2)

		while i < l1 and j < l2:
			res = comp(n1[i], n2[j], order)
			if res == 0:
				out.append(n1[i])
				out.append(n2[j])
				i += 1
				j += 1
			elif res == -1:
				out.append(n1[i])
				i += 1
			else:
				out.append(n2[j])
				j += 1

		while i < l1:
			out.append(n1[i])
			i += 1

		while j < l2:
			out.append(n2[j])
			j += 1

		return out

	k = len(arr)
	if k <= 0:
		return []

	if k == 1:
		return arr[0]

	# 10-15-10:25 = break
	# 10:38 - 11
	inp = arr
	l = k
	order = ''

	for i in range(l):
		if order:
			break
		for j in range(len(inp[i])-1):
			if inp[i][j] < inp[i][j + 1]:
				order = 'asc'
				break
			elif inp[i][j] > inp[i][j+1]:
				order = 'dsc'
				break
		while l > 1:
			out = []
			i = 0
			while i < l:
				if i == l - 1:
					out.append(inp[l - 1])
				else:
					o = merge(inp[i], inp[i + 1], order)
					out.append(o)
				i += 2
			inp = out
			l = len(inp)

	return out[0]

n1 = [1,3,5,7]
n2 = [2,4,6,7,8]
# print intersection(n1, n2)
# print union(n1,n2)

n =[3,5,2,1,5,6,4,6]
#print sorted(n)
print quickselect(n,3)
print quickselect(n,5)
# done = False
# k = 7
# i = 1
# prev = None
# out = []
#
# while not done:
# 	if i > len(n):
# 		break
# 	x = quickselect(n, i)
# 	if x != prev:
# 		out.append(x)
# 	i += 1
# 	prev = x
# 	done = (len(out) == k)
#
# print out


i = [
[1,6],
[3, 5, 7],
[2, 4],
[0, 9,10],
[10, 11],
[12,13]
]

inp = [
[34,26, 20, 13, 11, 7, 4, 4],
[41, 34, 27, 23, 19, 10, 8, 0],
[26, 25, 19, 12, 7, 7, 7, 5],
[46, 39, 35, 33, 27, 19, 12, 9],
[33, 24, 22, 18, 18, 10, 3, 0],
[42, 35, 35, 30, 21, 20, 12, 9],
[42, 33, 24, 21, 12, 12, 8, 7],
[29, 23, 21, 18, 18, 11, 8, 7],
[35, 30, 30, 23, 15, 14, 8, 7],
[20, 18, 17, 16, 12, 11, 5, 4]
]
#print mergeArrays(inp)


def func():
	l1 = len(arr1)
	l2 = len(arr2)

	out = arr2
	i = l1 - 1
	j = l1 - 1
	k = l2 - 1

	while i >= 0 and j >= 0:
		if arr1[i] == arr2[j]:
			out[k] = arr2[j]
			j -= 1
			k -= 1
			out[k] = arr1[i]
			i -= 1
		elif arr1[i] > arr2[j]:
			out[k] = arr1[i]
			i -= 1
		else:
			out[k] = arr2[j]
			j -= 1
		k -= 1

	return out


def dutch_flag_sort(balls):
	b_dict = {'R':1, 'G':2, 'B':3}
	pivot = 'G'

	ln = len(balls)
	curr = lo = 0
	hi = ln - 1

	while curr <= hi:
		c = b_dict[balls[curr]]
		p = b_dict[pivot]
		if c < p:
			balls[lo], balls[curr] = balls[curr], balls[lo]
			lo += 1
			curr += 1
		elif c > p:
			balls[hi], balls[curr] = balls[curr], balls[hi]
			hi -= 1
		else:
			curr += 1


# b = ['G','B','R','B','G']
# # print b
# # dutch_flag_sort(b)
# # print b

def solve(arr):
	lex_dict = {}

	for a in arr:
		k, v = a.split()

		if k in lex_dict:
			count, lex = lex_dict[k]
			count += 1
			if v > lex:
				lex = v
			lex_dict[k] = (count, lex)
		else:
			lex_dict[k] = (1, v)

	return [kk+':'+str(v[0])+','+v[1] for kk, v in lex_dict.items()]
