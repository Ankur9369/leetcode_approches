class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = {}
        count_t = {}

        for i in s:
            if i not in count_s:
                count_s[i] = 1
            else:
                count_s[i] += 1

        for i in t:
            if i not in count_t:
                count_t[i] = 1
            else:
                count_t[i] += 1

        if len(s) == len(t):
            for key in count_s:
                if key not in count_t:
                    return False

                if count_s[key] != count_t[key]:
                    return False

            return True

        return False
        