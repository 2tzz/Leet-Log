class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in range(0,len(nums)) :
            my_dict[i] = nums[i]
        print(my_dict)

        reverse_multidict = {}
        for key, value in my_dict.items():
            reverse_multidict.setdefault(value, []).append(key)

        duplicate_values_found = {}
        for value, keys in reverse_multidict.items():
            if len(keys) > 1:
                duplicate_values_found[value] = keys
        if len(duplicate_values_found) == 0 :
            return False
        elif len(duplicate_values_found) > 0 :
            return True