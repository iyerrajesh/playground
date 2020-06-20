from collections import defaultdict
import sys

def numSubarraysWithSum(A,S):
	l = len(A)
	c_sum = 0
	count = 0
	s = e = 0
	while e < l:
		while c_sum <= S and e < l:
			c_sum += A[e]
			if c_sum > S:
				break
			if c_sum == S:
				count += 1
			e += 1

		c_sum -= A[s]
		c_sum -= A[e]
		s += 1
		# while s <= e:
		# 	if c_sum == S:
		# 		count += 1
		# 	c_sum -= A[s]
		# 	s += 1
		# s -= 1
	return count


def findSubarraySum(arr, Sum):
	# Dictionary to store number of subarrays
	# starting from index zero having
	# particular value of sum.
	prevSum = defaultdict(lambda: 0)

	res = 0

	# Sum of elements so far.
	currsum = 0

	for i in range(0, len(arr)):

		# Add current element to sum so far.
		currsum += arr[i]

		# If currsum is equal to desired sum,
		# then a new subarray is found. So
		# increase count of subarrays.
		if currsum == Sum:
			res += 1

		# currsum exceeds given sum by currsum  - sum.
		# Find number of subarrays having
		# this sum and exclude those subarrays
		# from currsum by increasing count by
		# same amount.
		if (currsum - Sum) in prevSum:
			res += prevSum[currsum - Sum]

		# Add currsum value to count of
		# different values of sum.
		prevSum[currsum] += 1

	print prevSum
	return res


def min_subarry_k_ints(A, k):
	'''

	A = [1, 1, 2, 2, 3, 3, 4, 5], k = 3
	out = 5,7

	A = [1, 2, 2, 3], k = 2
	out = 0,1
	'''

	n_hash = defaultdict(lambda: 0)
	l = len(A)
	i = j = 0
	min_len = sys.maxint
	m_s, m_e = 0,0

	while j < l:
		while j < l:
			if len(n_hash) < k:
				n_hash[A[j]] += 1
			if len(n_hash) == k:
				m_len = j-i + 1
				if m_len < min_len:
					m_s, m_e = i, j
					min_len = m_len
				break
			j += 1

		while len(n_hash) == k:
			m_len = j-i + 1
			if m_len < min_len:
				m_s, m_e = i, j
				min_len = m_len

			n_hash[A[i]] -= 1
			if n_hash[A[i]] == 0:
				del n_hash[A[i]]
			i += 1

		j += 1

	return m_s, m_e



n = [0,0,0,1,0,0,1,0,0,0]
# [0,1,1,2,2,3,3,3,4,5,5]

#print findSubarraySum(n, 2)
#
# [0,1,1,2,2,3,3,3,4]
#
# 0-2
# 1-3

A = [2, 2]
k = 2
#print min_subarry_k_ints(A,k)

'''
Given a set of integers, e.g. {1,3,2}, and an array of random integers, e.g. 
[1, 2, 2, -5, -4, 0, 1, 1, 2, 2, 0, 3,3]
Find the shortest continuous subarray that contains all of the values from the set. 
If the subarray can not be found, return an empty array.
Result: [1, 2, 2, 0, 3]
'''


def h_match(src, tgt):
	ln = sum(src.values())
	print src
	return ln == len(tgt) and len(src) == len(set(tgt))


def min_array_w_nums(A, nums):
	l = len(A)
	n_hash = defaultdict(lambda:0)
	idxs = []
	x  = 0
	m_s, m_e = -1, -1
	m_min = 10000

	i = j = 0

	while j < l:
		while j < l:
			if not h_match(n_hash, nums):
				if A[j] in nums:
					n_hash[A[j]] += 1
					idxs.append(j)
			else:
			#if h_len(n_hash, len(nums)) == 0:
				i = idxs[x]
				if j-i+1 < m_min:
					m_s, m_e = i,j
					m_min = j-i+1
				break
			j += 1
		print (i, j)
		while h_match(n_hash, nums):
			if j-i+1 < m_min:
				m_s, m_e = i,j
				m_min = j-i+1

			n_hash[A[i]] -= 1
			if n_hash[A[i]] == 0:
				del (n_hash[A[i]])

			x += 1
			if x < len(idxs):
				i = idxs[x]
			else:
				break
		j += 1
		return m_s, m_e


s = "AAABBCA"
t = "ABC"
print (min_array_w_nums(s, t))
