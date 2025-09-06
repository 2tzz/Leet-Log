class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        my_dict = {}
        for i in range(0,len(nums)) :
            my_dict[i] = nums[i]

        for i in range(0,len(my_dict)-1):
            if my_dict[i]  == my_dict[i+1] :
                return True      
        return False