

def is_pal(inp):
	i = 0
	j = len(inp)-1

	while i < j:
		if inp[i] != inp[j]:
			return False
		i += 1
		j -= 1

	return True


def expand(s, st, e):
	l = len(s)
	out = []
	while st >= 0 and e < l and s[st] == s[e]:
		out.append(s[st:e+1])
		st -= 1
		e += 1
	return out


def pal_susbtr(s):
	ln = len(s)
	num = 0

	for i in range(ln):
		odd = expand(s,i,i)
		even = expand(s,i,i+1)
		num += len(odd) + len(even)

		#print(odd, even)

	return num


print (pal_susbtr('bbcc'))