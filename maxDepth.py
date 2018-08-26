
class TreeNode(object):
	def __init__(self,val,children):
		self.val = val
		self.children = children
class Solution(object):
	def maxDepth(self,root):
		if root is None:
			return 0
		if not root.children:
			return 1
		depth = 0
		for child in root.children:
			depth = max(depth, 1+self.maxDepth(child))
		return depth

children = [TreeNode(1,[]), TreeNode(2,[]), TreeNode(3, [])]
t1= TreeNode(1,children)
t0 = TreeNode(0,[t1])

s = Solution()
print s.maxDepth(t1)



#######method two

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        depth = 1 + max(self.maxDepth(child) for child in root.children)
        return depth