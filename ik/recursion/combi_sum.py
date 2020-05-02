import copy


def helper (slate, i, nums, tgt, p):

	if sum(slate) == tgt:
		p.append(slate)
	elif sum(slate) > tgt:
		return
	else:
		if nums:
			helper(slate+[nums[i]], i, nums[i+1:], tgt, p)
			helper(slate+[nums[i]], i, nums, tgt, p)


def combi_helper(results, combo, candidates, target, start_index):

	if target == 0:
		results.append(copy.deepcopy(combo))
		return

	for i in range(start_index, len(candidates)):
		if candidates[i] > target:
			break

		combo.append(candidates[i])
		combi_helper(results, combo, candidates, target-candidates[i], i)
		combo.pop()


def combination_sum(candidates, target):
	out = []
	c = []
	combi_helper(out, c, candidates, target, 0)
	return out


c = [2,3,5, 7]
t = 8
print combination_sum(c,t)

import random


def helper(nums, start, end):
	if start >= end:
		return nums[end]

	p_i = random.randrange(start, end + 1)
	nums[start], nums[p_i] = nums[p_i], nums[start]

	i = start
	j = start + 1
	pivot = nums[start]
	while j <= end:
		if nums[j] < pivot:
			i += 1
			nums[i], nums[j] = nums[j], nums[i]
		j += 1

	nums[start], nums[i] = nums[i], nums[start]
	helper(nums, start, i - 1)
	helper(nums, i + 1, end)

def qs_helper(arr, l, r):
	if l >= r:
		return

	pi = random.randrange(l, r + 1)
	#print(pi)
	p = arr[pi]
	arr[l], arr[pi] = arr[pi], arr[l]
	i = l
	j = l + 1

	while j <= r:
		if arr[j] < p:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
		j += 1

	arr[i], arr[l] = arr[l], arr[i]
	qs_helper(arr, l, i - 1)
	qs_helper(arr, i + 1, r)


def quick_select(arr, k):
	qs_helper(arr, 0, len(arr) - 1)
	print arr

a = [3,2,0,1,5,4]
quick_select(a, 2)