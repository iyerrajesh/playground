def lca(root, a, b):
	def lca_helper(root, a, b):
		if not root:
			return None, None

		l1, l2 = lca_helper(root.left, a, b)
		r1, r2 = lca_helper(root.right, a, b)

		l = None
		r = None

		if l1 and l2:
			return l1, l2
		if r1 and r2:
			return r1, r2

		if l1 == None and l2 != None or l1 != None and l2 == None:
			l = root

		if r1 == None and r2 != None or r1 != None and r2 == None:
			r = root

		if root.data == a.data:
			if l:
				l = r = root
			else:
				l = root

		if root.data == b.data:
			if r:
				r = l = root
			else:
				r = root
		return l, r

	n1, n2 = lca_helper(root, a, b)
	# print (n1.data, n2.data)
	return n1.data
