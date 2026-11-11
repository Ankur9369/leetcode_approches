class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_sum=0
        sum_map={0:1}
        result=0
        for num in nums:
            total_sum+=num #  update   sum part
            quest=total_sum-k # ask  question  at  each  elmet of  array
            
            if quest in sum_map: # aaply condiron if  exit update  result  then    -1
                result+=sum_map[quest]
            sum_map[total_sum]=sum_map.get(total_sum,0)+1 # update  the   hashmap  so that checking  at  every  part should be  carefully 
        return result
        