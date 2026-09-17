class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for digit in num:
            while stack and k>0 and digit < stack[-1]:
                stack.pop()
                k-=1
            stack.append(digit)
        while k>0 and stack:
            stack.pop()
            k-=1
        return "".join(stack).lstrip("0") or "0"
        