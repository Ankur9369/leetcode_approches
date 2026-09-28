class Solution(object):
    def  reverseParentheses( self,s):
        stack=[]
        for char in s:
            if  char !=')':
                stack.append(char)
            else:
                temp=""
                while stack[-1] !='(':
                    temp+=stack.pop()
                stack.pop()
                for ch in temp:
                    stack.append(ch)
    

        return "".join(stack)

        



