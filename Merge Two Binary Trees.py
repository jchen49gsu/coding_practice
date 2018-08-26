class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val +=t2.val
        t1.left = self.mergeTrees(t1.left,t2.left) #右边的为null时，直接返回左边的node给新的tree
        t1.right = self.mergeTrees(t1.right,t2.right)

        return t1


s = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t2.right = 3

s. mergeTrees(t1,t2)

