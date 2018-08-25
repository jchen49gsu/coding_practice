class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        results = []
        for i in xrange(left, right+1): 
            result = self.judge(i)
            if result != None:
                results.append(result)         
        
        return results  
    
    def judge(self,number):       
        number = str(number)
        for digit in number:
            if digit != '0' and int(number) % int(digit) == 0:
                continue
            else:
                return 
        
        return int(number)
            
        
        
                    