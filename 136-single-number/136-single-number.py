class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Occ = {}
        
        for i in range(len(nums)):
            if nums[i] in Occ.keys():
                Occ[nums[i]] += 1
            else:
                Occ[nums[i]] = 1
        
        for k , v in Occ.items():
            if v == 1:
                return k
            
            
        