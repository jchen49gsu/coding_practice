class Solution(object):
	def missingWords(self,s,t):
		results = []
		s = s.split()
		t = t.split()
		for i in xrange(len(s)):
			if s[i] not in t:
				results.append(s[i])
		return results
solution = Solution()
s = "I am using HackerRank to improve programming"
t = "am HackerRank to improve"
print solution.missingWords(s,t)