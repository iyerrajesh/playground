from collections import defaultdict

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


def is_palin(s):
	i = 0
	j = len(s)-1

	while i < j:
		if s[i] != s[j]:
			return False
		i += 1
		j -= 1
	return True


def pal_helper(s, o, l, r, out):
	if l == len(s):
		out.append('|'.join(o))
	else:
		for i in range(l, r+1):
			if is_palin(s[l:i+1]):
				pal_helper(s, o+[s[l:i+1]], i+1, r, out)


def pal_decomp(s):
	out = []
	o = []
	pal_helper(s, o, 0, len(s)-1, out)
	return out


def equalSubSetSumPartition(nums):
	# Write your code here

    val_n = val_p = 0
    for n in nums:
        if n < 0:
            val_n += n
        else:
            val_p += n
    tot = val_n + val_p

    if tot % 2 != 0:
        return False

    tot //= 2
    n = len(nums)
    dp = [defaultdict(bool) for _ in range(n)]

    for x in range(n):
        dp[x][0] = True

    for i in range(n):
        for j in range(val_n, val_p + 1):
            dp[i][j] = dp[i - 1][j]
            if j == nums[i]:
                dp[i][j] = True
            elif j - nums[i] >= val_n:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

    out = [False] * n

    if not dp[n - 1][tot]:
        return []

    i = n - 1
    j = tot
    c = 0

    while i >= 0:
        if i == 0:
            out[0] = True
            c += 1
        else:
            if dp[i][j] and not dp[i - 1][j]:
                out[i] = True
                tot -= nums[i]
                c += 1
                if not tot:
                    break
        i -= 1

    if c == n:
        return []
    return out


# ==================================================================
# tests...
# a = [-1,-2,3]
# k =
# print check_if_sum_possible(a,k)


# s = 'abracadabra'
# print pal_decomp(s)

nums = [1, 0, -1]
print (equalSubSetSumPartition(nums))



