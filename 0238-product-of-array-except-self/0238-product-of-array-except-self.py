class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        final_product=[1]*n
        
        for i in range(1,n):
            final_product[i]=final_product[i-1]*nums[i-1]
        right=1
        for i in range(n-1,-1,-1):
            final_product[i]*=right
            right*=nums[i]
            
        return final_product