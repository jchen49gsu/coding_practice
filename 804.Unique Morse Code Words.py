import string
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter= string.ascii_lowercase
        map = {}
        
        for i in xrange(len(table)):
            map[letter[i]]=table[i]
        
        
        newwords=[""] * len(words)
        for i in xrange(len (words)):
            word = words[i]
            for l in xrange(len(word)):
                newwords[i]+=(map[word[l]])
        
        newwords= set(newwords)
        return len(newwords)


s = Solution()
words = ["gin", "zen", "gig", "msg"]
s.uniqueMorseRepresentations(words)