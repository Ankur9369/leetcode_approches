class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        boloon_need={
        'b': 1,
        'a':1,
        'l':2,
        'o':2,
        'n':1
    }
        have={}
        for  char in text:
            if  char not in have:
                have[char]=1
            else: have[char]+=1
        x=[]
        for value in boloon_need:
            if value   not in have:

                return 0
            else :
                x.append(have[value]//boloon_need[value])
        return min(x)