def check_if_sum_possible(arr, k):
	def helper(arr, s, rsum, nelems):

		if rsum == 0 and nelems > 0:
			return True

		if s == len(arr):
			return False

		r = helper(arr, s+1, rsum-arr[s], nelems+1)
		if r:
			return r

		return helper(arr, s+1, rsum, nelems)

	return helper(arr, 0, k, 0)


def find_all_well_formed_brackets(n):
	def match(lp, rp, res, o):

		if lp == 0 and rp == 0:
			o.append(res)
		else:
			if lp == rp:
				match(lp - 1, rp, res + '(', o)
			elif rp > lp:
				if lp > 0:
					match(lp - 1, rp, res + '(', o)
				match(lp, rp - 1, res + ')', o)
			return o

	out = []
	return match(n, n, '', out)


a = [-1,-2,3]
k =
print check_if_sum_possible(a,k)