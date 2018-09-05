class Solution(object):
    def decode(self,codes, encoded):
        dic = {}
        index = 0
        for code in codes:
            code = code.split("\t")
            if code[0] != '[newline]':
                dic[code[1]]= code[0]
            else:
                dic[code[1]] = "\n" 

        result = ""
    
        while index < len(encoded):
            subEncoded = encoded[index:]
            char, index = decodeChar(dic, index, subEncoded)
            result += char

        return result

    def decodeChar(self, dic, index, subEncoded):
        for key, value in dic.items():
            print "key is: ", key
            print subEncoded
            if subEncoded.startswith(key):
                index += len(key)
                return value, index

codes = ['a 100100','b 100101','c 110001','d 100000','newline 111111','p 111110','q 000001']
encoded = '111110000001100100111111100101110001111110'
s = Solution()
print s.decode(codes,encoded)
