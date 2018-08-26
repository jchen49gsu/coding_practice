class TreeNode(object):
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None


class Solution(object):
	def maxDepthBinaryTree(self,root):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 1

		return max(self.maxDepthBinaryTree(root.left),self.maxDepthBinaryTree(root.right))+1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s = Solution()
print s.maxDepthBinaryTree(root)