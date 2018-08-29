class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def searchBST(self,root,val):
		if root is None:
			return root
		if root.val == val:
			return root
		elif root.val > val:
			return self.searchBST(root.left,val)
		else:
			return self.searchBST(root.right,val)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
val = 1

s = Solution()
print s.searchBST(root,val)