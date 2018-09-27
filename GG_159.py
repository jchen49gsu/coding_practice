class Solution(object):
	def findLength(self,s):
		left = 0
		res = 0
		dic = {}
		s = str(s)
		for right in xrange(len(s)):
			if s[right] in dic:
				dic[s[right]] += 1
			else:
				dic[s[right]] = 1
				while len(dic) > 2:
					dic[s[left]] -=1
					if dic[s[left]] == 0:
						del dic[s[left]]
					left +=1
			res = max(res,right - left +1)
		return res

			

s = Solution()
string1 = 12134
string2  = 1122333

print s.findLength(string1)
print s.findLength(string2)