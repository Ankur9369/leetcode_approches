class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        curr_num=0
        curr_str=""
        for char in s:
            if char.isdigit():
                curr_num=curr_num*10+int(char)
            elif char=="[":
                stack.append((curr_str,curr_num))
                curr_num=0
                curr_str=""

            elif char=="]":
                pre_str, rep_num=stack.pop()
                curr_str=pre_str + curr_str * rep_num
            else:
                curr_str+=char    
        return curr_str