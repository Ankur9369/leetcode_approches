class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        max_depth=0
        for ch in  s:
            if ch =='(':
                stack.append(ch)
                depth=len(stack)
                max_depth=max(max_depth,depth)
            elif ch==')' :
                stack.pop()
        return max_depth