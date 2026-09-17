
class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # make two hash maps for storing
        # ransomNote and magazine
        need = {}
        have = {}

        n = len(ransomNote)
        m = len(magazine)

        # for the ransomNote
        for i in range(n):
            if ransomNote[i] not in need:
                need[ransomNote[i]] = 1
            else:
                need[ransomNote[i]] += 1

        # for the magazine
        for i in range(m):
            if magazine[i] not in have:
                have[magazine[i]] = 1
            else:
                have[magazine[i]] += 1

        return self.valid(need, have)

    def valid(self, need, have):

        # check every character required by ransomNote
        for char in need:

            # character is not available in magazine
            if char not in have:
                return False

            # available quantity is less than required quantity
            if need[char] > have[char]:
                return False

        # all required characters are available
        return True

