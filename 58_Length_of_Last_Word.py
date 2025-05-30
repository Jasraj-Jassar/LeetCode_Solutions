class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split()
        b = int(len(a)) - 1
        c = (a[b])
        return(len(c))
