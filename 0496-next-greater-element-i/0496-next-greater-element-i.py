class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        stack =[]
        ans={}
        for num in nums2:
            while  stack and num> stack[-1]:
                ans[stack.pop()]=num
            stack.append(num)
        # return :The next greater element for each value of nums1 is
        return [ans.get(num,-1) for num in nums1 ]      
        