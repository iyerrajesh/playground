import heapq
import math


class Point(object):
	def __init__(self, d, xy):
		self.d = d
		self.xy = xy

	def __eq__(self, other):
		return (self.d == other.d)

	def __ne__(self, other):
		return (self.d != other.d)

	def __lt__(self, other):
		return (self.d < other.d)

	def __le__(self, other):
		return (self.d <= other.d)

	def __gt__(self, other):
		return (self.d > other.d)

	def __ge__(self, other):
		return ((self.d >= other.d)


def nearest_neighbours(p_x, p_y, k, n_points):
	h = []

	count = 0
	for p in n_points:
		d = math.sqrt((p[0] - p_x) ** 2 + (p[1] - p_y) ** 2)
		# print d
		point = Point(-d, p)

		if count < k:
			heapq.heappush(h, point)
		else:
			h_p = h[0]
			if d <= h_p.d * (-1):
				heapq.heapreplace(h, point)
		count += 1

	return [x.xy for x in h]

