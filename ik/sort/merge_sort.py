def merge_sort(arr):
	merge(arr, 0, len(arr)-1)
	return arr


def merge(arr, l, r):
	if l >= r:
		return

	m = (l+r)//2
	merge(arr, l, m)
	merge(arr, m+1, r)

	# IMP: create aux array size =[r-l+1]
	# i = l
	# j = m+1
	# loop to compare and merge l,r into aux
	#
	aux = _combine(arr, l, m, r)
	# IMP: copy back aux[l:r] into arr
	x = 0
	j = l
	while x < len(aux):
		arr[j] = aux[x]
		j += 1
		x += 1


def _combine(a, s, m, e):
	out = []
	i = s
	j = m+1
	l1 = m+1
	l2 = e+1

	while i < l1 and j < l2:
		if a[i] == a[j]:
			out.append(a[i])
			out.append(a[j])
			i += 1
			j += 1
		elif a[i] < a[j]:
			out.append(a[i])
			i += 1
		else:
			out.append(a[j])
			j += 1

	while i < l1:
		out.append(a[i])
		i += 1

	while j < l2:
		out.append(a[j])
		j += 1

	return out



a = [4,1,0,10,7,8,1,2,16]
print merge_sort(a)