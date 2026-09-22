class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups={}
        for value in strs:
            # firstly  sort the each  element
            sort_value=tuple(sorted(value))
             # check the element  is there not?
           
            if sort_value not in groups:
                groups[sort_value]=[]# if not then  make the  key   for it 
                groups[sort_value].append(value)# then  for that key push the value  in the lst  form 
            else : groups[sort_value].append(value) # else if there then  jsut  push  acc to their   keys 
        return list(groups.values())# lst just  retuen the ans in the  form  of  list 
        