class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # initialize  empty  stack , bar_chart and  max_area
        stack=[]
        bar_chart= heights +[0]
        max_area=0
        for index, height in  enumerate(bar_chart):
            while stack and height< bar_chart[stack[-1]]:
                bar_height=bar_chart[stack.pop()]
                left_index=stack[-1] if stack else -1
                width= index -left_index -1
                max_area=max(max_area ,  bar_height * width)
            stack.append(index)
        return max_area
        
        