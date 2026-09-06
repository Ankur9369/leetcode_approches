class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        ans={}
        for num in range(len(temperatures)):
            while stack and  temperatures[num]> temperatures[stack[-1]]:
                prev=stack.pop()
                ans[prev]=num-prev
            stack.append(num)
        return [ans.get(num,0) for num in range(len(temperatures))]    
        