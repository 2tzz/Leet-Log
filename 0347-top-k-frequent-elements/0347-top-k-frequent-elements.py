class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        my_dict = defaultdict(list)
        for i in nums :
            my_dict[i].append(i)       
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: len(item[1]), reverse=True))
        print(sorted_dict)
        keys = list(sorted_dict.keys())
        for i in range(k) :
            output.append(keys[i])
        return output