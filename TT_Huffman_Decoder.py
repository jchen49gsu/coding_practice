class Solution(object):
	def __init__(self):
		self.result = ''
		self.index = 0
		self.dic = {}
	def decode(self,codes,encoded):
		for code in codes:
			code = code.split(" ")
			if code[0] != "newline":
				self.dic[code[1]] = code[0]
			else:
				self.dic[code[1]] = "\n"

		print ("dic is:" , self.dic)


		result = ""
		while self.index < (len(encoded)):
			cur = encoded[self.index:]
			result += self.start_with(cur)

		return "result is: ", result

	def start_with(self, s):
		for key, value in self.dic.items():
			if s.startswith(key):
				self.index += len(key)
				return value
   

codes = ['a 100100','b 100101','c 110001','d 100000','newline 111111','p 111110','q 000001']
encoded = '111110000001100100111111100101110001111110'
s = Solution()
print s.decode(codes,encoded)