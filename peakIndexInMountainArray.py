class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in xrange(len(A)):
            
            if A[i-1] < A[i] and A[i] > A[i+1]:
                return i
            else:
                continue