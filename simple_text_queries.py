class Solution(object):

	def textQueries(self,sentences,queries):
		result = []
		for i in xrange(len(sentences)):
			found = True
			for query in queries:
				try:
					sentences[i].split().index(query)
				except Exception:
					found = False
			if found:
				result.append("sentence[" + str(i) + "]")
		if not result:
			return -1 
		return result	



sentences = ['bob and alice like to text each other', 'bob does not like to ski', 'alice likes to ski']
queries1 = ['bob','will']
queries2 = ['alice']
queries3 = ['like']
s = Solution()
print s.textQueries(sentences,queries1)
print s.textQueries(sentences,queries2)
print s.textQueries(sentences,queries3)


