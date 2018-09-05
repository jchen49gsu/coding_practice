class Solution(object):
	def closest(self,s,queries):
		
		result = []
		for query in queries:
			dic = {}
			for i in xrange(len(s)):
				if s[query] == s[i] and query != i:
					dic[i] = abs(i-query)
			if not dic:
				result.append(-1) 
			else:
				minPair =min(zip(dic.values(),dic.keys()))
				result.append( minPair[1])
		return result


sol = Solution()
s = "hackherrankhhh"
queries = [4, 1, 6, 8,0]
print sol.closest(s,queries)