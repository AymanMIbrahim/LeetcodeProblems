class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        Occ = {}
        
        for i in range(len(nums)):
            if nums[i] in Occ.keys():
                Occ[nums[i]] += 1
            else:
                Occ[nums[i]] = 1
        ML = []
        for k,v in Occ.items():
            if v == 1:
                ML.append(k)
        
        return ML