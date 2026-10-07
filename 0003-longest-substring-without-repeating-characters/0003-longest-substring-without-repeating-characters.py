class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        # initialize a set  to store the  characters in the  current  window
        char_set=set()
        left=0
        max_lenght=0
        right=0
        while right<len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_lenght=max(max_lenght,right-left +1)
                right+=1
            else:
                char_set.remove(s[left])
                left+=1
    
        return max_lenght
        