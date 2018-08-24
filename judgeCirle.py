class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        orig = [0,0]
        for i in xrange(len(moves)):
            if moves[i] == "U":
                orig[0]+=1
            elif moves[i] =="D":
                orig[0]-=1
            elif moves[i] == "L":
                orig[1] -=1
            elif moves[i] == "R":
                orig[1] +=1
        if orig == [0,0]:
            return True
        else:
            return False
        