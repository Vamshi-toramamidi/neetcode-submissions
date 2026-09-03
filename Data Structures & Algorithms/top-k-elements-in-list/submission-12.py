class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        dictionary = {}
        for val in nums:
            if val in dictionary:
                dictionary[val] += 1
            else:
                dictionary[val] = 1
        
        sorted_desc = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
        op = list(sorted_desc)
        return op[0:k]
        