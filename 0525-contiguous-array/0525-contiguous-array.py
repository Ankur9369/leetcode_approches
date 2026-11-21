class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res=0
        hashmap={0:-1}
        one=0
        zero=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else :
                one+=1
            diff=one-zero
            if diff ==0:
                res=max(res,i+1)
                continue
            if  diff not in hashmap:
                hashmap[diff]=i
            else:
                lenght=i-hashmap[diff]
                res=max(lenght,res)
        return res
            

        