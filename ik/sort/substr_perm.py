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