class Solution(object):
	def electionWinner(self,votes):
		dic = {}
		for vote in votes:
			if vote not in dic:
				dic[vote] = 1
			else:
				dic[vote]+=1
		maxPair =max(zip(dic.values(), dic.keys()))
		maxKey = maxPair[1]
		return maxKey
		

s = Solution()
votes1 = ["victor", "veronica", "ryan", "dave", "maria", "farah", "farah", "ryan", "veronica"]
votes2 = ["Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"]
votes3 = ["c","b","c","b"]
print s. electionWinner(votes1)
print s. electionWinner(votes2)
print s. electionWinner(votes3)

