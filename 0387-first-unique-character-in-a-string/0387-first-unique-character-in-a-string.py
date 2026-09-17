class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        hash_f={}
        for i in range(n):
            if s[i] not in hash_f:
                hash_f[s[i]]=1
            else:
                hash_f[s[i]]+=1
        for i in range(n):
            if hash_f[s[i]]==1:
                return i
        return -1   
        