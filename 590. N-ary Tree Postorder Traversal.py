class TreeNode(object):
	def __init__(self,x, children):
		self.val = x
		self.children = children

class Solution(object):
	def postorder(self,root):
		res = []
		if root == None:
			return res

		self.recur(root,res)
		return res

	def recur(self,root,res):

		for child in root.children:
			self.recur(child,res)

		res.append(root.val)


children = [TreeNode(2,[]),TreeNode(3,[])]
root = TreeNode(1,children)

#root = TreeNode(3, [TreeNode(2, []),TreeNode(4, [])])

s = Solution()
print s.postorder(root)