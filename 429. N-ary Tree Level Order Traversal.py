
from collections import deque
class TreeNode(object):
	def __init__(self,x,children):
		self.val = x
		self.children = children

class Solution(object):
	"""docstring for Solution"""
	def levelOderTraversal(self,root):
		queue = deque()
		res = []
		if root is None:
			return res
		queue.append(root)

		while queue:
			size = len(queue)
			l = []
			for i in xrange(size):
				node = queue.popleft()
				l.append(node.val)
				for child in node.children:
					if child is not None:			
						queue.append(child)
			res.append(l)

		return res


children1 = [TreeNode(5,[]),TreeNode(6,[])]
children2 = [TreeNode(3,children1),TreeNode(2,[]),TreeNode(4,[])] #要是list
root = TreeNode(1,children2)





s = Solution()
print s.levelOderTraversal(root)
