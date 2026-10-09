class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # IN this  quesion you  can  use the normal  sort fun to do solve  but  there is majrable edge  case that  you are  prohbited  to use it :
        # so that   if you    solve  by  using  any  sorting technique it also not  accepted because 
        #  any kinda sorting technique is not  optimal for this  problem 
        #  hence  here we are using  three pointing method  , we divind the nums into the three segmented area where  we are puting the  o,1,2  as low mid and high :
        # this  techniuqe  is also   known as  dutch  natioanl flag :
        
        
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

        