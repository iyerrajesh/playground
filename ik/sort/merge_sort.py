def merge_sort(arr):
	merge(arr, 0, len(arr)-1)
	return arr


def merge(arr, l, r):
	if l >= r:
		return

	m = (l+r)//2
	merge(arr, l, m)
	merge(arr, m+1, r)

	print l, m, r

	# IMP: create aux array size =[r-l+1]
	# i = l
	# j = m+1
	# loop to compare and merge l,r into aux
	#
	# IMP: copy back aux[l:r] into arr



a = [4,1,0,10,7,8]
print merge_sort(a)