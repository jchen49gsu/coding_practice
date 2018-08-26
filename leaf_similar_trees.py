
class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def leaf_similar_trees(self,t1,t2):
		res1 = []
		res2 = []
		self.find_leaf(t1,res1)
		self.find_leaf(t2,res2)

		return res1 == res2


	def find_leaf(self,root,res):
		if root is None:
			return
		if root.left is None and root.right is None:
			res.append(root.val)
			return

		self.find_leaf(root.left,res)
		self.find_leaf(root.right,res)
		return

s = Solution()
t1 = TreeNode(5)
t1.left = TreeNode(2)
t1.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)

print s.leaf_similar_trees(t1,t2)




