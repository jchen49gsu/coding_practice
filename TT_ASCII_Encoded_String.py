class Solution(object):
	def __init__(self):
		self.result = ''
		self.index = 0

	def decode(self,input):
		
		digit = input[::-1]
		while self.index < (len(digit)):
			if self.index + 1 >= len(digit):
				return self.result

			number = digit[self.index] + digit[self.index+1]
			if self.twoDigit(int(number)):
				continue
			elif self.index + 2 < len(digit):
				number += digit[self.index + 2]
				if self.threeDigit(number):
					continue
				return self.result		

		return self.result
	def twoDigit(self, number):
		if int(number) == 32:
			self.result+=" "
			self.index+=2
		elif (int(number) >= 65 and int(number) <= 90) or (int(number) >= 97):
			char = chr(int(number))
			self.result += char
			self.index += 2
		else:
			return False
		return True

	def threeDigit(self, number):
		if int(number) > 122:
			return False
		char = chr(int(number))
		self.result += char
		self.index += 3
		return True
			


# s1 = Solution()
# s2 = Solution()
# s1.num += 10
# s2.num += 5
s = Solution()

input = "01111151101140111147"
print s.decode(input)