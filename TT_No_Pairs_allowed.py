class Solution(object):
	def minimalOperations(self,words):
		results = []
		for word in words:
			print ('current word:', word)
			current = word[0]
			count = 0
			result = 0
			for i in xrange(len(word)):		
				if current == word[i]:
					count +=1
				else:
					result += count / 2
					current = word[i]
					count = 1
			result += count / 2
			results.append(result)
		return results

s = Solution()
words1 = ["ab", "aab", "abb", "abab", "abaaaba"]
print ("final result:", s.minimalOperations(words1))