

class Solution:
	companies={'A':0,'B':0,'C':0}
	output = []

	def charityAllocation(self, companies):
		#mini = min(companies['A'], companies['B'], companies['C'])
		mini = min(companies.values())
		if companies['A'] == mini:
			return 'A'
		elif companies['B'] == mini:
			return 'B'
		else:
			return 'C'



	def main(self,input):
		for i in input:
			return_company = self.charityAllocation(self.companies)
			self.output.append(return_company)
			self.companies[return_company] += i
		return self.output

			





s = Solution()
input = [25,8,2,35,15,120,55,42]
print s.main(input)