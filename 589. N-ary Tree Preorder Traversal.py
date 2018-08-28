class TreeNode(object):
	def __init__(self,x,children):
		self.val = x
		self.children = children

class Solution(object):
	def preorder(self,root):
		res = []
		if root is None:
			return res

		self.recur(root,res)
		return res

	def recur(self,root,res):
		res.append(root.val)
		for child in root.children:
			self.recur(child,res)


children1 = [TreeNode(5,[]),TreeNode(6,[])]
children2 = [TreeNode(3,children1),TreeNode(2,[]),TreeNode(4,[])]
root = TreeNode(1,children2)
s = Solution()
print s.preorder(root)