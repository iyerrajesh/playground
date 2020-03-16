'''
s1 = 'ab'
s2 ='eidbaoo', True

s1 = 'ab'
s2 = 'eidboaoo'

'''
from collections import Counter
def str_perm(s1, s2):

	s1_hash = Counter(s1)
	i = 0
	l = len(s2)
	while i < l:
		if not s2[i] in s1_hash:
			i += 1
			continue

		s2_hash = {s2[i]:1}
		e = i+1
		while e < l and s2[e] in s1_hash:
			x = s2[e]
			if x in s2_hash:
				s2_hash[x] += 1
			else:
				s2_hash[x] = 1
			if not s2_hash[x] <= s1_hash[x]:
				#i = e
				break
			if e-i+1 == len(s1):
				return True
			e += 1
		i += 1


	return False


s1 = 'fools'
s2 = 'heyfurlolsof'
print str_perm(s1,s2)

def min_array_w_nums(A, nums):
	l = len(A)
	n_hash = defaultdict(lambda:0)
	idxs = []
	x  = 0
	m_s, m_e = 0, 0 
	m_min = sys.maxint 

	i = j = 0

	while j < l:
		while j < l:
			if len(n_hash) < len(nums):
				if A[j] in nums:
					n_hash[A[j]] += 1
					idxs.append(j)
			if len(n_hash) == len(nums):
				i = idxs[x]
				if j-i+1 < m_min:
					m_s, m_e = i,j
					m_min = j-i+1
				break
			j += 1

		while len(n_hash) == len(nums):
			if j-i+1 < m_min:
				m_s, m_e = i,j
				m_min = j-i+1

			n_hash[A[i]] -= 1
			if n_hash[A[i]] == 0:
				del (n_hash[A[i]])

			x += 1
			i = idxs[x]
			
		j += 1

	return m_s, m_e


s = {1,3,2}
#A = [1,2,2,3,-4,0,1,1,2,2,0,3,3,2,2,0,1]
A = [4,5,6,7,9,1,2,4,5,6]
A = [1,2,5,8,7,6,2,6,5,3,8,5]
s = s = {5,7}
#print (min_array_w_nums(A,s))

A = 'ANCSNBAXC'
s = 'CN'
print (min_array_w_nums(A, s))
