
class Solution():
	def countEmail(self, emails):
		dic = {}
		res = 0
		local = ''
		for index, email in enumerate (emails):		
			email = email.split("@")
			local = email[0]
			domain = email[1]
			if "+" in local:
				index = local.index("+")
				substring = local[:index].replace(".","")
			else:				
				substring = local.replace(".","")			

			email = substring+"@" + domain

			if email not in dic:
				dic[email] = 1
			else: 
				dic[email] +=1

		for k,v in dic.items():
			if v >= 2:
				res += 1
		return res



s = Solution()

string = ['a.b@example.com','dupli......cate@example.com','d.u.p.l.i.c.a.t.e@example.com','ab+work@example.com']
#string = ['a.b@example.com']
print s.countEmail(string)

nested_value_value=''.join(map(str,nested_value_value))