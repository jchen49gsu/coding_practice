class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:].zfill(8)
        print x
        y = bin(y)[2:].zfill(8)
        print y
        count = 0
        for i in xrange(len(x)):
            if x[i] != y[i]:
                count+=1
        return count

s = Solution()
x = 1
y = 4

print s.hammingDistance(x,y)



class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        XOR = x^y
        cnt = 0
        while XOR > 0:
            if XOR & 1 == 1:
                cnt += 1
            XOR = XOR >> 1
        return cnt

s = Solution()
x = 1
y = 4

print s.hammingDistance(x,y)


"""
1 is true, 0 is false
^ : 异或相异为1  0^0=0；   0^1=1；   1^0=1；   1^1=0

再数有多少个1，就是相差多少个1，用 &， 只有是1才能和1与的结果为1
& ： 0&0=0;   0&1=0;    1&0=0;     1&1=1; 只要有一个是0 就为0

>> : 向右移一位，看下一位是不是1

-------------------------------------
其他的：
| ：     0|0=0；   0|1=1；   1|0=1；    1|1=1 只要有一个1 就为1

<< :   左移1位后a = a * 2; 若左移时舍弃的高位不包含1，则每左移一位，相当于该数乘以2。



“”“


