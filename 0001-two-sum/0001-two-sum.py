class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(0,len(nums)) :
            for j in range(i+1,len(nums)):
                if target - nums[i] == nums[j] :
                    out.append(i)
                    out.append(j)
                    return out