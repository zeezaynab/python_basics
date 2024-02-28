class Solution(object):
    def firstPalindrome(self,words):
        for i in words:
            b=i[::1]
            if i==b:
                return(b)
            return("")