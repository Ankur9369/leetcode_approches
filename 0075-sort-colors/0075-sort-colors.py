class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # this question is  if you uese the  normal  sort fun but it is  prohbtes for this  quuestion  so  simple  use the  or make the  sort func simpliy 
        # choice the  three pointer  rule :
        
        low =0
        mid=0
        high=len(nums)-1

        while mid <=high:
            if  nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1
        return nums

        