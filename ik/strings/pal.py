

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


def expand_max(s, st, e):
	l = len(s)
	s_max = (-1,-1)
	while st >= 0 and e < l and s[st] == s[e]:
		s_max = (st, e)
		st -= 1
		e += 1
	return s_max


def pal_substr(s):
	ln = len(s)
	l_pal = 0
	l_pal_str = ''

	for i in range(ln):
		x,y = expand_max(s,i,i)
		if l_pal < y-x+1:
			l_pal = y-x+1
			l_pal_str = s[x:y+1]
		x, y = expand_max(s,i,i+1)
		if l_pal < y-x+1:
			l_pal = y-x+1
			l_pal_str = s[x:y+1]
	return l_pal_str


def is_overlap(rec1, rec2):
	recs = [rec1, rec2]
	#recs.sort(key=lambda x:x[0])

	rec1, rec2 = recs
	if rec2[0] == rec1[0]:
		if rec2[1] < rec1[1]:
			rec1, rec2 = rec2, rec1

	if rec2[0] < rec1[2]:
		if rec2[1] < rec1[3]:
			return True

	if rec2[1] < rec1[3]:
		if rec2[0] < rec1[2]:
			return True

	return False


#print (pal_substr("babadaadfudgigbhhbgrt"))
r1 = [-2,1,0,3]
r2 = [-2,0,0,1]

print (is_overlap(r1,r2))