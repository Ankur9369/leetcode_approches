class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        mapping = {}
        i = 0

        while i < len(s):

            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]

            i += 1

        return True
        