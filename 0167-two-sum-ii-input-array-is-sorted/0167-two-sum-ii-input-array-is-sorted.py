class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lookup = {}
        output = []
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in lookup:
                output = [lookup[diff] + 1, i + 1]
                break
            lookup[num] = i

        return output
        