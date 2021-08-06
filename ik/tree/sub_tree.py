def _get_match(root, sub):
	if not root:
		return None

	if root.val == sub.val:
		return root

	r = _get_match(root.left, sub)
	if r:
		return r
	return _get_match(root.right, sub)


def traverse_sub(match, sub):
	if not match and not sub:
		return True

	if not match and sub or not sub and match:
		return False

	if match.val != sub.val:
		return False

	r = traverse_sub(match.left, sub.left)
	if not r:
		return False

	return traverse_sub(match.right, sub.right)


def is_sub_tree(root, sub):
	match = _get_match(root, sub)
	if not match:
		return False
	return traverse_sub(match, sub)
