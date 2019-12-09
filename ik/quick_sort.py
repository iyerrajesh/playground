import heapq


def q_sort(nums, n):
	heapq.heapify(nums)
	k = 0
	out = []
	r = heapq.nlargest(1, nums)
	return out


def topK(nums, k):
	n = list(set(nums))
	m = n[:k]
	heapq.heapify(m)
	rest = n[k:]

	for r in rest:
		mn = heapq.nsmallest(1,m)
		if r > mn[0]:
			heapq.heapreplace(m,r)

	out = []
	while m:
		out.append(heapq.heappop(m))
	return out


n = [5,4,2,1,5,4,6,3,6]
print topK(n,3)


