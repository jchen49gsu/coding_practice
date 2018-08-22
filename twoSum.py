###### method 1 ###########3

class Solution:
	
	
	def twoSum(self, nums, target ):
		dic = {}
		for i in xrange(len(nums)):
			if target-nums[i] not in dic:
				dic[nums[i]] = i
			else:
				return [dic[target-nums[i]],i]


s = Solution()
nums = [2,7,8,0]
target = 9
print s.twoSum(nums,target)

####### method 2 ############

class Solution:
	
	
	def twoSum(self, nums, target ):
		for i in xrange(len(nums)):
			for j in xrange(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i,j]



s = Solution()
nums = [2,7,8,0]
target = 9
print s.twoSum(nums,target)